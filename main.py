from cryptography.fernet import Fernet

# Generate a random encryption key
key = Fernet.generate_key()

def encrypt_text(text, key):
    # Create a Fernet symmetric encryption object with the provided key
    cipher = Fernet(key)

    # Encode the text to bytes
    encoded_text = text.encode()

    # Encrypt the text
    encrypted_text = cipher.encrypt(encoded_text)

    # Return the base64-encoded encrypted text
    return encrypted_text.decode()

def decrypt_text(encrypted_text, key):
    # Create a Fernet symmetric encryption object with the provided key
    cipher = Fernet(key)

    # Decode the base64-encoded encrypted text
    encoded_text = encrypted_text.encode()

    # Decrypt the text
    decrypted_text = cipher.decrypt(encoded_text)

    # Return the decrypted text as a string
    return decrypted_text.decode()

# Example usage
plaintext = input("write text here to encrypt: ")
encrypted = encrypt_text(plaintext, key)
decrypted = decrypt_text(encrypted, key)

print("Original Text:", plaintext)
print("Encrypted Text:", encrypted)
print("Decrypted Text:", decrypted)