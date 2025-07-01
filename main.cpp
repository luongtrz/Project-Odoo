def normalize_phone_number(phone):
    phone = phone.replace('.', '').replace('-', '')
    
    if phone.startswith('0'):
        phone = phone[1:]
    return '+84' + phone[:3] + ' ' + phone[3:6] + ' ' + phone[6:]

# Kiểm thử
if __name__ == "__main__":
    print("Kết quả:", normalize_phone_number("0123.456.789"))
