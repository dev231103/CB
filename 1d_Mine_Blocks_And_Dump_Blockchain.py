import hashlib
import json
import datetime

# -------------------------------
# Block Class
# -------------------------------
class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = {
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }
        block_string = json.dumps(block_data, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


# -------------------------------
# Blockchain (Miner) Class
# -------------------------------
class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, ["Genesis Block"], "0")
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]

    def add_transaction(self, sender, receiver, amount):
        if amount <= 0:
            print("Invalid transaction amount. Amount must be greater than 0.")
            return

        transaction = {
            "sender": sender,
            "receiver": receiver,
            "amount": amount,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.pending_transactions.append(transaction)
        print("Transaction added successfully to pending transaction pool.")

    def add_block_to_miner(self):
        if not self.pending_transactions:
            print("\nNo pending transactions available to mine.")
            return

        new_block = Block(
            index=len(self.chain),
            transactions=self.pending_transactions.copy(),
            previous_hash=self.get_last_block().hash
        )

        self.chain.append(new_block)
        self.pending_transactions.clear()

        print(f"\nBlock {new_block.index} added successfully by miner!")
        print(f"Block Hash: {new_block.hash}")

    def dump_blockchain(self):
        print("\n==================== BLOCKCHAIN DUMP ====================")

        for block in self.chain:
            print("\n--------------------------------------------------------")
            print(f"Block Index     : {block.index}")
            print(f"Timestamp       : {block.timestamp}")
            print("Transactions    :")

            if isinstance(block.transactions, list):
                for tx in block.transactions:
                    if isinstance(tx, dict):
                        print(f"   Sender   : {tx['sender']}")
                        print(f"   Receiver : {tx['receiver']}")
                        print(f"   Amount   : {tx['amount']}")
                        print(f"   Time     : {tx['timestamp']}")
                        print("   --------------------------------")
                    else:
                        print(f"   {tx}")
            else:
                print(f"   {block.transactions}")

            print(f"Previous Hash   : {block.previous_hash}")
            print(f"Nonce           : {block.nonce}")
            print(f"Current Hash    : {block.hash}")

        print("\n========================================================")


# -------------------------------
# Main Program (Menu Driven)
# -------------------------------
miner = Blockchain()

while True:
    print("\n========== BLOCKCHAIN MINER MENU ==========")
    print("1. Add Transaction")
    print("2. Mine Pending Transactions (Add New Block)")
    print("3. Dump Blockchain")
    print("4. View Pending Transactions")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        sender = input("Enter sender name: ").strip()
        receiver = input("Enter receiver name: ").strip()
        amount = float(input("Enter amount: "))
        miner.add_transaction(sender, receiver, amount)

    elif choice == '2':
        miner.add_block_to_miner()

    elif choice == '3':
        miner.dump_blockchain()

    elif choice == '4':
        print("\n========== PENDING TRANSACTIONS ==========")
        if not miner.pending_transactions:
            print("No pending transactions.")
        else:
            for i, tx in enumerate(miner.pending_transactions, start=1):
                print(f"\nTransaction {i}")
                print(f"Sender   : {tx['sender']}")
                print(f"Receiver : {tx['receiver']}")
                print(f"Amount   : {tx['amount']}")
                print(f"Time     : {tx['timestamp']}")

    elif choice == '5':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")