import datetime
import hashlib
import json

# -------------------- Client --------------------
class Client:
    def __init__(self, name, balance=100):
        self.name = name
        self.identity = name
        self.balance = balance

    def __str__(self):
        return self.name


# -------------------- Transaction --------------------
class Transaction:
    def __init__(self, sender, recipient, value):
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.time = datetime.datetime.now()

    def sign_transaction(self):
        pass

    def to_dict(self):
        return {
            'sender': str(self.sender),
            'recipient': str(self.recipient),
            'value': self.value,
            'time': str(self.time)
        }

    def execute_transaction(self):
        if self.sender.balance >= self.value:
            self.sender.balance -= self.value
            self.recipient.balance += self.value
            print("Transaction successful")
        else:
            print("Insufficient balance")


# -------------------- Display Function --------------------
def display_transaction(transaction):
    d = transaction.to_dict()
    print("sender:", d['sender'])
    print("recipient:", d['recipient'])
    print("value:", d['value'])
    print("time:", d['time'])
    print("-----")


# -------------------- Create Clients --------------------
Dinesh = Client("Dinesh")
Ramesh = Client("Ramesh")
Seema = Client("Seema")
Vijay = Client("Vijay")


# -------------------- Transactions --------------------
transactions = []

t1 = Transaction(Dinesh, Ramesh, 15.0)
t2 = Transaction(Dinesh, Seema, 6.0)
t3 = Transaction(Ramesh, Vijay, 2.0)
t4 = Transaction(Seema, Ramesh, 4.0)
t5 = Transaction(Vijay, Seema, 7.0)
t6 = Transaction(Ramesh, Seema, 3.0)
t7 = Transaction(Seema, Dinesh, 8.0)
t8 = Transaction(Seema, Ramesh, 1.0)
t9 = Transaction(Vijay, Dinesh, 5.0)
t10 = Transaction(Vijay, Ramesh, 3.0)

# Execute + store
for t in [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]:
    t.execute_transaction()
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


# -------------------- Add Block Function --------------------
def add_block(transactions, previous_hash):
    block = Block()
    block.previous_block_hash = previous_hash
    block.Nonce = 0

    for tx in transactions:
        block.verified_transactions.append(tx)

    return block


# -------------------- Genesis Block --------------------
TPCoins = []

t0 = Transaction("Genesis", Dinesh, 500.0)

block0 = Block()
block0.previous_block_hash = "0"
block0.Nonce = 0

block0.verified_transactions.append(t0)

last_block_hash = block0.compute_hash()
TPCoins.append(block0)


# -------------------- Add New Block --------------------
block1 = add_block(transactions, last_block_hash)
last_block_hash = block1.compute_hash()
TPCoins.append(block1)


# -------------------- Blockchain Display --------------------
def dump_blockchain(chain):
    print("\nNumber of blocks in the chain:", len(chain))

    for i, block in enumerate(chain):
        print("\nBlock #", i)
        print("Previous Hash:", block.previous_block_hash)
        print("Nonce:", block.Nonce)

        for transaction in block.verified_transactions:
            display_transaction(transaction)

    print("=====================================")


# -------------------- Show Blockchain --------------------
dump_blockchain(TPCoins)
