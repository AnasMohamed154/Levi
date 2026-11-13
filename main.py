.
def encode(text: str, shift: int) -> str:
    text = text.upper()
    result = ""

    for char in text:
        if 'A' <= char <= 'Z':
            new_char = chr(
                (ord(char) - ord('A') + shift) % 26 + ord('A')
            )
            result += new_char
        else:
            result += char

    return result


def decode(text: str, shift: int) -> str:
    return encode(text, -shift)


# Easy Testing
message = input("Enter your message: ")
move = int(input("Move (1, 2, 3...): "))

print("Encrypted:", encode(message, move))
print("Decrypted:", decode(encode(message, move), move))
