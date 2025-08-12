def normalize_phone(phone_number: str) -> str:
    """
    Convert phone numbers from format '0.xxx.xxx.xxx' to '0xxxxxxxxx'
    """
    # Remove any non-digit characters
    return ''.join(ch for ch in phone_number if ch.isdigit())

# Example usage:
print(normalize_phone("0.123.456.789"))  # Output: 0123456789
