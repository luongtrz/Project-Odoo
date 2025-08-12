import re

def normalize_phone(phone_number) -> str:
    """
    Convert a phone number from '0.xxx.xxx.xxx' format to '0xxxxxxxxx' format.
    
    Args:
        phone_number (str): Phone number containing digits and possible separators (dots, spaces, dashes).
    
    Returns:
        str: Phone number with only digits.
    
    Raises:
        ValueError: If the result is not a valid 10-digit number starting with 0.
        TypeError: If the input is not a string.
    """
    # Input validation for non-string
    if not isinstance(phone_number, str):
        raise TypeError(f"phone_number must be a string, got {type(phone_number).__name__}")

    cleaned = re.sub(r'\D', '', phone_number)  # Remove all non-digit chars
    
    if not (len(cleaned) == 10 and cleaned.startswith('0')):
        raise ValueError(f"Invalid phone number: {phone_number}")
    
    return cleaned
# ✅ Valid cases
print(normalize_phone("0.123.456.789"))      # 0123456789
print(normalize_phone("0-987-654-321"))      # 0987654321
print(normalize_phone("0123 456 789"))       # 0123456789
print(normalize_phone("  0.111.222.333  "))  # 0111222333 (trim spaces)
print(normalize_phone("+84.123.456.789"[2:])) # Remove country code manually

# ❌ Invalid cases
for test in [
    "123456789",       # missing leading 0
    "0.123.456.789.0", # more than 10 digits
    "abcdefghij",      # no digits
    "+84 123456789",   # contains country code without trimming
    None,              # non-string
    1234567890         # non-string
]:
    try:
        print(normalize_phone(test))
    except Exception as e:
        print(f"{test!r} -> {e}")
