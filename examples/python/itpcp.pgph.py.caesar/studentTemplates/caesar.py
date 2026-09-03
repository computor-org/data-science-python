import string

# Reserved characters
reserved_chars = "!*'();:@&=+$,/?%#[]"

# Unreserved characters
unreserved_chars = string.ascii_letters + string.digits + "-._~"

# All characters
all_chars = unreserved_chars + reserved_chars
print(all_chars)


def caesar_encrypt(text: str, key: int, alphasize: int = 85) -> str:
    # Your code here
    pass


def caesar_decrypt(text: str, key: int, alphasize: int = 85) -> str:
    # Your code here
    pass
