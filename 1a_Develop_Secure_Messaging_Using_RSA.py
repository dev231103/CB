from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import base64


# Function to generate RSA key pairs
def generate_rsa_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key


# Function to serialize keys
def serialize_keys(private_key, public_key):
    priv_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    pub_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return priv_pem, pub_pem


# Encrypt a message using public key
def encrypt_message(public_key, message):
    encrypted = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return base64.b64encode(encrypted).decode()


# Decrypt a message using private key
def decrypt_message(private_key, encrypted_message):
    decrypted = private_key.decrypt(
        base64.b64decode(encrypted_message),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return decrypted.decode()


# Simulating two users: Alice and Bob
print("Generating RSA key pairs for Alice and Bob...")

alice_private, alice_public = generate_rsa_key_pair()
bob_private, bob_public = generate_rsa_key_pair()

# Alice sends a message to Bob
message_from_alice = "Hi Bob, this is Alice. The message is secure!"
print("\nOriginal message from Alice:", message_from_alice)

encrypted_message = encrypt_message(bob_public, message_from_alice)
print("Encrypted message (sent to Bob):", encrypted_message)

# Bob decrypts the message
decrypted_message = decrypt_message(bob_private, encrypted_message)
print("Decrypted message by Bob:", decrypted_message)
