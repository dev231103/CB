import binascii
import Crypto
import Crypto.Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256

# Define Client class
class Client:
    def __init__(self, name):
        self.name = name

        # Generate secure random bytes
        rand_func = Crypto.Random.new().read

        # Generate RSA private key (2048 bits for better security)
        self._private_key = RSA.generate(2048, rand_func)

        # Generate corresponding public key
        self._public_key = self._private_key.publickey()

        # Create signer object
        self._signer = PKCS1_v1_5.new(self._private_key)

    @property
    def identity(self):
        # Return public key in hexadecimal format
        return binascii.hexlify(
            self._public_key.exportKey(format='DER')
        ).decode('ascii')

    @property
    def public_key(self):
        return self._public_key

    @property
    def private_key(self):
        return self._private_key

    # Sign a message
    def sign_message(self, message):
        h = SHA256.new(message.encode('utf-8'))
        signature = self._signer.sign(h)
        return signature


# Function to encrypt message using receiver's public key
def encrypt_message(message, receiver_public_key):
    cipher = PKCS1_OAEP.new(receiver_public_key)
    encrypted = cipher.encrypt(message.encode('utf-8'))
    return encrypted


# Function to decrypt message using receiver's private key
def decrypt_message(encrypted_message, receiver_private_key):
    cipher = PKCS1_OAEP.new(receiver_private_key)
    decrypted = cipher.decrypt(encrypted_message)
    return decrypted.decode('utf-8')


# Function to verify sender's signature
def verify_signature(message, signature, sender_public_key):
    h = SHA256.new(message.encode('utf-8'))
    verifier = PKCS1_v1_5.new(sender_public_key)
    return verifier.verify(h, signature)


# Create two clients
sender = Client("Alice")
receiver = Client("Bob")

# Display client identities
print("Sender Name:", sender.name)
print("Sender Identity (Public Key):", sender.identity)

print("\nReceiver Name:", receiver.name)
print("Receiver Identity (Public Key):", receiver.identity)

# Input message from sender
message = input("\nEnter message to send securely: ")

# Encrypt message with receiver's public key
encrypted_message = encrypt_message(message, receiver.public_key)

# Sign message with sender's private key
signature = sender.sign_message(message)

# Decrypt message with receiver's private key
decrypted_message = decrypt_message(encrypted_message, receiver.private_key)

# Verify sender's signature using sender's public key
is_verified = verify_signature(decrypted_message, signature, sender.public_key)

# Display results
print("\n--- Secure Message Exchange ---")
print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)

if is_verified:
    print("Signature Verification: Successful (Message is authentic)")
else:
    print("Signature Verification: Failed (Message may be tampered)")