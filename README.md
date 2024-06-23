# CryptoKit
![Screenshot 2024-06-23 135030](https://github.com/nayera540/CryptoKit/assets/69148381/6f90b343-d44a-4989-9d11-cb36ed9ad832)

# AES-Symmetric Cipher
This project offers encryption and decryption functions using the AES algorithm, supporting ECB and CBC modes to enhance data security during transmission.
![Screenshot 2024-06-23 135220](https://github.com/nayera540/CryptoKit/assets/69148381/351a0b72-0487-4139-814a-b8ffbe98e940)

## Features
- **Encryption Function (`encrypt_aes`)**: Encrypts plaintext with AES, supports ECB and CBC modes, applies PKCS7 padding.
- **Decryption Function (`decrypt_aes`)**: Decrypts ciphertext back to plaintext, supports ECB and CBC modes, removes PKCS7 padding.

## Usage
### ECB Mode
1. Choose "AES encryption and Decryption" with ECB mode.
2. Enter file path and key, encrypt, and save the encrypted file.
3. Decrypt using the same key to retrieve the original message.
4. Handles errors for incorrect file paths or empty files.
![Screenshot 2024-06-23 135121](https://github.com/nayera540/CryptoKit/assets/69148381/fa3b5381-1666-4bb5-8f47-f4f1046fa793)

### CBC Mode
1. Choose "AES encryption and Decryption" with CBC mode.
2. Enter file path, IV, and key, encrypt, and save the encrypted file.
3. Decrypt using the correct path and key to retrieve the original message.
![Screenshot 2024-06-23 135138](https://github.com/nayera540/CryptoKit/assets/69148381/c7a55dcd-aa56-4bc9-bdd2-6fcc38453033)

# Secure Communication Widget with Authentication and Confidentiality
This code ensures secure communication using AES for confidentiality and RSA for authentication, guaranteeing data integrity and privacy.
![Screenshot 2024-06-23 135503](https://github.com/nayera540/CryptoKit/assets/69148381/2146e22e-511e-4c43-a276-c319bc7afa62)

## Features
- **RSA Key Pair Generation**: Creates private and public keys for authentication.
- **Authentication Functions (`auth_source_a`, `auth_destination_b`)**: Authenticates messages by hashing and encrypting/decrypting the hash using RSA.
- **RSA Encryption/Decryption**: Encrypts and decrypts messages using RSA with OAEP padding.
- **Hashing**: Computes and compares hash values using SHA-512.
- **Confidentiality Authentication**: Extends authentication with AES encryption for confidentiality.

## Expected Results
- **Authentication**: `perform_authentication` returns True if successful, False otherwise.
- **Confidentiality and Authentication**: `confidentiality_authentication` returns True if both processes are successful, False otherwise.

## Usage
### Authentication
1. Choose the `Authentication` option.
2. Enter the same message at source and destination, provide a valid public key, and run.
3. Authentication fails if messages at source and destination differ.
