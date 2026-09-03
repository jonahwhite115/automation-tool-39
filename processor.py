import logging
from typing import Dict, Any, List

logger = logging.getLogger(__name__)


class ValidationError(Exception):
    """Raised when input action payload fails validation rules."""
    pass


def validate_action_payload(payload: Dict[str, Any]) -> bool:
    """Validate game action payload structure and coordinate values."""
    if not isinstance(payload, dict):
        raise ValidationError("Payload must be a dictionary.")

    action_type = payload.get("action_type")
    if not action_type or not isinstance(action_type, str):
        raise ValidationError("Invalid or missing 'action_type'.")

    valid_actions = {"click", "keypress", "drag", "wait"}
    if action_type not in valid_actions:
        raise ValidationError(f"Unsupported action_type: '{action_type}'.")

    if action_type in ("click", "drag"):
        coords = payload.get("coordinates")
        if not isinstance(coords, (tuple, list)) or len(coords) != 2:
            raise ValidationError("Coordinates must be a (x, y) tuple or list.")
        x, y = coords
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            raise ValidationError("Coordinates (x, y) must be numeric.")
        if x < 0 or y < 0:
            raise ValidationError("Coordinates cannot be negative.")

    if action_type == "wait":
        duration = payload.get("duration", 0)
        if not isinstance(duration, (int, float)) or duration <= 0:
            raise ValidationError("Wait duration must be a positive number.")

    return True


def process_action_queue(action_queue: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Main processing loop with robust input validation for game commands."""
    processed_results = []

    for index, item in enumerate(action_queue):
        try:
            validate_action_payload(item)
            logger.info(f"Executing action #{index + 1}: {item['action_type']}")
            
            result = item.copy()
            result["status"] = "executed"
            processed_results.append(result)
        except ValidationError as err:
            logger.warning(f"Skipping invalid task at index {index}: {err}")
            failed_item = item if isinstance(item, dict) else {"raw": item}
            failed_item["status"] = "rejected"
            failed_item["error"] = str(err)
            processed_results.append(failed_item)

    return processed_results
