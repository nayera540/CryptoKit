from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
import AES

# Function to generate an RSA key pair
def generate_rsa_key_pair():
    """
    Generates an RSA key pair (private and public keys).

    Returns:
    - Tuple[bytes, bytes]: A tuple containing the private key in PEM format and the public key in PEM format.
    """
    # Generate an RSA private key with a specified public exponent and key size
    private_key_obj = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    # Convert the private key to PEM format with TraditionalOpenSSL encoding and no encryption
    private_key_pem = private_key_obj.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )

    # Extract the corresponding public key from the private key
    public_key_obj = private_key_obj.public_key()

    # Convert the public key to PEM format with SubjectPublicKeyInfo format
    public_key_pem = public_key_obj.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Return a tuple containing the private key PEM and public key PEM
    return private_key_pem, public_key_pem



# Function to encrypt a message using RSA
def encrypt_message_rsa(public_key_pem, plaintext_message):
    """
    Encrypts a plaintext message using RSA with OAEP padding.

    Parameters:
    - public_key_pem (bytes): The public key in PEM format.
    - plaintext_message (bytes): The plaintext message to be encrypted.

    Returns:
    - bytes: The encrypted ciphertext.
    """
    # Load the provided public key PEM encoded string and create a public key object
    recipient_public_key = serialization.load_pem_public_key(public_key_pem, backend=default_backend())

    # Encrypt the plaintext message using RSA with OAEP padding
    encrypted_message = recipient_public_key.encrypt(
        plaintext_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Return the encrypted ciphertext
    return encrypted_message


def decrypt_message_rsa(private_key_pem, ciphertext):
    """
    Decrypts a ciphertext message using RSA with OAEP padding.

    Parameters:
    - private_key_pem (bytes): The private key in PEM format.
    - ciphertext (bytes): The ciphertext message to be decrypted.

    Returns:
    - bytes: The decrypted plaintext message.
    """
    # Load the provided private key PEM encoded string and create a private key object
    private_key = serialization.load_pem_private_key(private_key_pem, password=None, backend=default_backend())

    # Decrypt the ciphertext message using RSA with OAEP padding
    decrypted_message = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Return the decrypted plaintext message
    return decrypted_message


def compute_hash(data):
    """
    Computes the hash value of data using the SHA-512 algorithm.

    Parameters:
    - data (bytes or str): The data to be hashed.

    Returns:
    - bytes: The hash value.
    """
    # Encode the data if it is a string
    encoded_data = data.encode() if isinstance(data, str) else data

    # Create a SHA-512 hash object
    hash_object = hashes.Hash(hashes.SHA512(), backend=default_backend())

    # Update the hash object with the data
    hash_object.update(encoded_data)

    # Finalize the hash computation and get the hash value
    hash_value = hash_object.finalize()

    # Return the hash value
    return hash_value


# Function to compare two hash values
def compare_hashes(original_hash, new_data):
    """
    Compares the hash of new data with an original hash.

    Parameters:
    - original_hash (bytes): The original hash to compare against.
    - new_data (bytes or str): The new data for which to compute the hash and compare.

    Returns:
    - bool: True if the hashes match, False otherwise.
    """
    # Compute the hash of the new data
    new_data_hash = compute_hash(new_data)

    # Compare the computed hash with the original hash
    return new_data_hash == original_hash


# Generate RSA key pair
private_key, public_key = generate_rsa_key_pair()

# Function for Source A in the authentication process
def auth_source_a(input_message):
    """
    Generates authenticated source A data.

    Parameters:
    - input_message (bytes or str): The input message for authentication.

    Returns:
    - bytes: The concatenated data containing message size, input message, and encrypted hash.
    """
    # Compute the hash of the input message
    hashed_message = compute_hash(input_message)

    # Encrypt the hash using RSA with OAEP padding
    encrypted_hash = encrypt_message_rsa(public_key, hashed_message)

    # Calculate the message size
    message_size = str(len(input_message))

    # Concatenate the message size, input message, and encrypted hash
    concatenated_data = message_size.encode('utf-8') + input_message + encrypted_hash

    return concatenated_data


# Function for Destination B in the authentication process
def auth_destination_b(concatenated_data, received_message):
    """
    Performs authentication at destination B.

    Parameters:
    - concatenated_data (bytes): The concatenated data containing message size, input message, and encrypted hash.
    - received_message (bytes or str): The received message for authentication.

    Returns:
    - bool: True if the authentication is successful, False otherwise.
    """
    # Extract the message size from the concatenated data
    message_size = int(chr(concatenated_data[0]))

    # Extract the ciphertext from the concatenated data
    ciphertext = concatenated_data[message_size + 1:]

    # Decrypt the ciphertext to obtain the hash
    decrypted_hash = decrypt_message_rsa(private_key, ciphertext)

    # Compare the decrypted hash with the received message's hash
    result = compare_hashes(decrypted_hash, received_message)

    return result


def perform_authentication(sent_message, received_message):
    """
    Performs authentication between source A and destination B.

    Parameters:
    - sent_message (bytes or str): The message sent by source A.
    - received_message (bytes or str): The message received by destination B.

    Returns:
    - bool: True if the authentication is successful, False otherwise.
    """
    # Generate authenticated data at source A
    concatenated_data = auth_source_a(sent_message)

    # Perform authentication at destination B
    result = auth_destination_b(concatenated_data, received_message)

    return result


# Function to perform confidentiality and authentication
def confidentiality_authentication(sent_message, received_message, encryption_key):
    """
    Performs confidentiality and authentication between source A and destination B.

    Parameters:
    - sent_message (bytes or str): The message sent by source A.
    - received_message (bytes or str): The message received by destination B.
    - encryption_key (bytes): The key used for AES encryption and decryption.

    Returns:
    - bool: True if both confidentiality and authentication are successful, False otherwise.
    """
    # Generate authenticated data at source A
    concatenated_data = auth_source_a(sent_message)

    # Encrypt the concatenated data using AES with ECB mode
    encrypted_concatenated_data = AES.encrypt_aes(encryption_key, concatenated_data, "ECB (electronic code book)")

    # Decrypt the encrypted data using AES with ECB mode
    decrypted_concatenated_data = AES.decrypt_aes(encryption_key, encrypted_concatenated_data, "ECB (electronic code book)")

    # Perform authentication at destination B using the decrypted data
    result = auth_destination_b(decrypted_concatenated_data, received_message)

    return result

