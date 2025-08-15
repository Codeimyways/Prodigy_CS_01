def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Leave non-alphabet characters unchanged

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)  # Decryption is the reverse of encryption


def main():
    print("=== Caesar Cipher ===")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

    if choice not in ['e', 'd']:
        print("Invalid choice!")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (number): "))
    except ValueError:
        print("Invalid shift value! Please enter a number.")
        return

    if choice == 'e':
        encrypted = encrypt(message, shift)
        print(f"Encrypted message: {encrypted}")
    else:
        decrypted = decrypt(message, shift)
        print(f"Decrypted message: {decrypted}")


if __name__ == "__main__":
    main()
