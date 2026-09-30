[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# automation-tool-39

`automation-tool-39` is a lightweight Python automation framework designed to streamline resource harvesting and inventory management in modern PC RPGs. By combining real-time computer vision with randomized input simulation, it automates repetitive gameplay routines safely and efficiently.

## Features

- **OCR Inventory & Market Scanning:** Automatically parses item stats, stack quantities, and vendor prices directly from the game UI using OpenCV.
- **Humanized Input Emulation:** Generates natural Bezier curve mouse movements and randomized micro-delays to prevent pattern detection.
- **State-Aware Fail-Safes:** Triggers immediate system pause or logout upon detecting lower health thresholds, player trade requests, or disconnected servers.
- **Multi-Client Session Handling:** Supports running independent automation profiles across multiple concurrently running game instances.

## Installation

Ensure you have Python 3.9 or higher installed alongside Tesseract OCR on your system.

```bash
git clone https://github.com/Developer/automation-tool-39.git
cd automation-tool-39
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Basic Usage

Run a pre-configured crafting loop on an active game process:

```python
from automation_tool_39 import GameBot, WindowManager

# Bind to the target game window
window = WindowManager.find_window("FantasyRPG Client")
bot = GameBot(target_window=window, capture_fps=30)

# Execute automated loop
@bot.on_frame
def crafting_routine(frame):
    if bot.vision.find("craft_button.png", confidence=0.88):
        bot.input.click("craft_button.png")
        bot.vision.wait_until_present("craft_complete.png", timeout=5)
        bot.input.press_key("e")

if __name__ == "__main__":
    bot.start()
```

## License

Distributed under the MIT License. See `LICENSE` for more information.