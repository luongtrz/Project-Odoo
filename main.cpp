def to_hashtag_format(name):
    return '#' + ''.join(c for c in name if c != ' ')

# Kiểm thử
if __name__ == "__main__":
    print(to_hashtag_format("Tran Luong"))
