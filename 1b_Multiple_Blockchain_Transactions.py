import hashlib
import time

# -------------------- Client Class --------------------
class Client:
    def __init__(self):
        self.identity = hashlib.sha256(str(time.time()).encode()).hexdigest()


# -------------------- Transaction Class --------------------
class Transaction:
    def __init__(self, sender, recipient, value):
        self.sender = sender if isinstance(sender, str) else sender.identity
        self.recipient = recipient
        self.value = value
        self.time = time.time()

    def to_dict(self):
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'value': self.value,
            'time': self.time
        }

    def sign_transaction(self):
        pass  # Dummy function


# -------------------- Block Class --------------------
class Block:
    def __init__(self):
        self.verified_transactions = []
        self.previous_block_hash = ""
        self.Nonce = ""

    def compute_hash(self):
        data = (
            str([tx.to_dict() for tx in self.verified_transactions]) +
            str(self.previous_block_hash) +
            str(self.Nonce)
        )
        return hashlib.sha256(data.encode()).hexdigest()


# -------------------- Display Function --------------------
def display_transaction(transaction):
    tx = transaction.to_dict()

    print(f"Sender    : {tx['sender']}")
    print(f"Recipient : {tx['recipient']}")
    print(f"Amount    : {tx['value']}")

    readable_time = time.strftime(
        '%Y-%m-%d %H:%M:%S',
        time.localtime(tx['time'])
    )
    print(f"Time      : {readable_time}")


# -------------------- Create Clients --------------------
Dinesh = Client()
Ramesh = Client()
Seema = Client()
Vijay = Client()


# -------------------- Create Transactions --------------------
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
print("\n========== TRANSACTIONS ==========\n")

for i, transaction in enumerate(transactions, 1):
    print(f"Transaction #{i}")
    display_transaction(transaction)
    print("----------------------------------")


# -------------------- Create Genesis Block --------------------
block0 = Block()
block0.previous_block_hash = None
block0.Nonce = None

t0 = Transaction("Genesis", Dinesh.identity, 500.0)
block0.verified_transactions.append(t0)

digest = block0.compute_hash()
print("\nBlock Hash:", digest)


# -------------------- Blockchain --------------------
TPCoins = [block0]


# -------------------- Display Blockchain --------------------
def dump_blockchain(blockchain):
    print("\n========== BLOCKCHAIN ==========\n")
    print("Total Blocks:", len(blockchain))

    for i, block in enumerate(blockchain):
        print(f"\n🧱 Block #{i}")
        print(f"Previous Hash : {block.previous_block_hash}")
        print(f"Nonce         : {block.Nonce}")
        print(f"Transactions  : {len(block.verified_transactions)}\n")

        for j, transaction in enumerate(block.verified_transactions, 1):
            print(f"  Tx #{j}")
            display_transaction(transaction)
            print("  --------------------------")

        print("=====================================")


dump_blockchain(TPCoins)
