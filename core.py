import time

def get_user_input():
    return input("Enter action sequence (e.g., '1,2,3'): ")

def validate_sequence(sequence):
    try:
        parts = [int(x.strip()) for x in sequence.split(',')]
        return parts if all(0 < x < 10 for x in parts) else None
    except ValueError:
        return None

def run_automation():
    """Main processing loop for automation-tool-39"""
    print("Starting gaming automation sequence...")
    
    while True:
        user_data = get_user_input()
        if user_data.lower() == 'quit':
            break
            
        sequence = validate_sequence(user_data)
        if sequence:
            print(f"Executing sequence: {sequence}")
            time.sleep(1)
            print("Execution complete.")
        else:
            print("Invalid input: please enter comma-separated numbers 1-9")

if __name__ == "__main__":
    run_automation()