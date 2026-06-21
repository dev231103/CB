import datetime
import hashlib
import json


# -------------------- Client --------------------
class Client:
    def __init__(self, name):
        self.name = name
        self.identity = name

    def __str__(self):
        return self.name


# -------------------- Transaction --------------------
class Transaction:
    def __init__(self, sender, recipient_identity, value):
        self.sender = sender
        self.recipient = recipient_identity
        self.value = value
        self.time = datetime.datetime.now()

    def sign_transaction(self):
        # Placeholder (no real crypto yet)
        pass

    def to_dict(self):
        return {
            'sender': str(self.sender),
            'recipient': str(self.recipient),
            'value': self.value,
            'time': str(self.time)
        }


# -------------------- Display Function --------------------
def display_transaction(transaction):
    d = transaction.to_dict()
    print("sender:", d['sender'])
    print("recipient:", d['recipient'])
    print("value:", d['value'])
    print("time:", d['time'])
    print('-----')


# -------------------- Create Clients --------------------
Dinesh = Client("Dinesh")
Ramesh = Client("Ramesh")
Seema = Client("Seema")
Vijay = Client("Vijay")


# -------------------- Transactions --------------------
transactions = []

t1 = Transaction(Dinesh, Ramesh.identity, 15.0)
t2 = Transaction(Dinesh, Seema.identity, 6.0)
t3 = Transaction(Ramesh, Vijay.identity, 2.0)
t4 = Transaction(Seema, Ramesh.identity, 4.0)
t5 = Transaction(Vijay, Seema.identity, 7.0)
t6 = Transaction(Ramesh, Seema.identity, 3.0)
t7 = Transaction(Seema, Dinesh.identity, 8.0)
t8 = Transaction(Seema, Ramesh.identity, 1.0)
t9 = Transaction(Vijay, Dinesh.identity, 5.0)
t10 = Transaction(Vijay, Ramesh.identity, 3.0)

# Sign and store
for t in [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]:
    t.sign_transaction()
    transactions.append(t)


# -------------------- Display Transactions --------------------
for transaction in transactions:
    display_transaction(transaction)
    print('------------------')


# -------------------- Block --------------------
class Block:
    def __init__(self):
        self.verified_transactions = []
        self.previous_block_hash = ""
        self.Nonce = ""

    def compute_hash(self):
        block_data = {
            "transactions": [t.to_dict() for t in self.verified_transactions],
            "previous_hash": self.previous_block_hash,
            "nonce": self.Nonce
        }
        encoded = json.dumps(block_data).encode()
        return hashlib.sha256(encoded).hexdigest()


# -------------------- Genesis Block --------------------
TPCoins = []

t0 = Transaction("Genesis", Dinesh.identity, 500.0)

block0 = Block()
block0.previous_block_hash = "0"
block0.Nonce = 0

block0.verified_transactions.append(t0)

# Compute hash
last_block_hash = block0.compute_hash()

TPCoins.append(block0)


# -------------------- Blockchain Display --------------------
def dump_blockchain(chain):
    print("\nNumber of blocks in the chain:", len(chain))
    for i, block in enumerate(chain):
        print("\nBlock #", i)
        print("Previous Hash:", block.previous_block_hash)
        print("Nonce:", block.Nonce)

        for transaction in block.verified_transactions:
            display_transaction(transaction)

    print('=====================================')


# -------------------- Show Blockchain --------------------
dump_blockchain(TPCoins)
