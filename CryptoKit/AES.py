from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def encrypt_aes(secret_key, plaintext, encryption_mode, initialization_vector=None):
    # Check the encryption mode and create a cipher accordingly
    if encryption_mode == 'ECB (electronic code book)':
        cipher = Cipher(algorithms.AES(secret_key), modes.ECB(), backend=default_backend())
    elif encryption_mode == 'CBC (cipher block chaining)':
        # Check if IV is provided for CBC mode
        if initialization_vector is None:
            raise ValueError("Initialization Vector (IV) is required for CBC mode")
        cipher = Cipher(algorithms.AES(secret_key), modes.CBC(initialization_vector), backend=default_backend())
    else:
        raise ValueError("Invalid encryption mode. Supported modes are ECB and CBC.")

    # Encrypt the plaintext
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded_message = padder.update(plaintext) + padder.finalize()
    ciphertext = encryptor.update(padded_message) + encryptor.finalize()
    return ciphertext

def decrypt_aes(secret_key, ciphertext, encryption_mode, initialization_vector=None):
    # Check the encryption mode and create a cipher accordingly
    if encryption_mode == 'ECB (electronic code book)':
        cipher = Cipher(algorithms.AES(secret_key), modes.ECB(), backend=default_backend())
    elif encryption_mode == 'CBC (cipher block chaining)':
        # Check if IV is provided for CBC mode
        if initialization_vector is None:
            raise ValueError("Initialization Vector (IV) is required for CBC mode")
        cipher = Cipher(algorithms.AES(secret_key), modes.CBC(initialization_vector), backend=default_backend())
    else:
        raise ValueError("Invalid encryption mode. Supported modes are ECB and CBC.")

    # Decrypt the ciphertext
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(ciphertext) + decryptor.finalize()

    # Manually remove PKCS7 padding
    padding_length = decrypted_message[-1]
    original_message = decrypted_message[:-padding_length]

    return original_message


