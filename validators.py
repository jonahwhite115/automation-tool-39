def validate_input(data):
    if not isinstance(data, dict):
        raise ValueError("Input must be a dictionary.")
    if 'name' not in data or not isinstance(data['name'], str):
        raise ValueError("'name' must be a string.")
    if 'age' not in data or not isinstance(data['age'], int) or data['age'] < 0:
        raise ValueError("'age' must be a non-negative integer.")
    return True

def validate_email(email):
    import re
    email_regex = r'^[\w.-]+@[\w.-]+\.\w{2,}$'
    if not re.match(email_regex, email):
        raise ValueError("Invalid email format.")
    return True
