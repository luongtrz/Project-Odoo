import re

def normalize_phone(phone_number: str) -> str:
    """
    Convert a phone number from '0.xxx.xxx.xxx' format to '0xxxxxxxxx' format.
    
    Args:
        phone_number (str): Phone number containing digits and possible separators (dots, spaces, dashes).
    
    Returns:
        str: Phone number with only digits.
    
    Raises:
        ValueError: If the result is not a valid 10-digit number starting with 0.
    """
    cleaned = re.sub(r'\D', '', phone_number)  # Remove all non-digit chars
    
    if not (len(cleaned) == 10 and cleaned.startswith('0')):
        raise ValueError(f"Invalid phone number: {phone_number}")
    
    return cleaned


# ✅ Test cases
print(normalize_phone("0.123.456.789"))  # 0123456789
print(normalize_phone("0-987-654-321"))  # 0987654321
print(normalize_phone("0123 456 789"))   # 0123456789

try:
    print(normalize_phone("123456789"))  # ❌ Missing leading 0
except ValueError as e:
    print(e)

try:
    print(normalize_phone("abc.def.ghi"))  # ❌ Invalid input
except ValueError as e:
    print(e)
