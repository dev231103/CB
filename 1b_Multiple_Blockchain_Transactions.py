import hashlib
import datetime

# List to store all transactions (Transaction Pool)
transactions = []

# Function to generate unique transaction ID using SHA-256
def generate_transaction_id(sender, receiver, amount, timestamp):
    data = f"{sender}|{receiver}|{amount}|{timestamp}"
    return hashlib.sha256(data.encode()).hexdigest()

# Input number of transactions
n = int(input("Enter the number of transactions: "))

# Create multiple transactions
for i in range(n):
    print(f"\nEnter details for Transaction {i + 1}")

    sender = input("Enter sender name: ").strip()
    receiver = input("Enter receiver name: ").strip()

    # Amount validation
    while True:
        amount = float(input("Enter amount: "))
        if amount > 0:
            break
        else:
            print("Amount must be greater than 0. Please re-enter.")

    # Generate timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Generate unique transaction ID
    tx_id = generate_transaction_id(sender, receiver, amount, timestamp)

    # Store transaction details in dictionary
    transaction = {
        "tx_id": tx_id,
        "sender": sender,
        "receiver": receiver,
        "amount": amount,
        "timestamp": timestamp,
        "status": "Pending"
    }

    # Add transaction to transaction pool
    transactions.append(transaction)

# Display transactions in organized format
print("\n==================== TRANSACTION POOL ====================")
print("{:<5} {:<15} {:<15} {:<10} {:<20} {:<10}".format(
    "No.", "Sender", "Receiver", "Amount", "Timestamp", "Status"
))
print("-" * 85)

for i, tx in enumerate(transactions, start=1):
    print("{:<5} {:<15} {:<15} {:<10.2f} {:<20} {:<10}".format(
        i,
        tx["sender"],
        tx["receiver"],
        tx["amount"],
        tx["timestamp"],
        tx["status"]
    ))

# Display transaction IDs
print("\n==================== TRANSACTION IDs ====================")
for i, tx in enumerate(transactions, start=1):
    print(f"Transaction {i} ID: {tx['tx_id']}")