import hashlib
import datetime

# Initial account balances
accounts = {
    "Alice": 1000.0,
    "Bob": 800.0,
    "Charlie": 500.0
}

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.tx_id = self.generate_transaction_id()
        self.status = "Pending"

    # Generate unique transaction ID using SHA-256
    def generate_transaction_id(self):
        data = f"{self.sender}|{self.receiver}|{self.amount}|{self.timestamp}"
        return hashlib.sha256(data.encode()).hexdigest()

    # Transfer money from sender to receiver
    def transfer(self):
        if self.sender not in accounts:
            self.status = "Failed - Sender not found"
            print("\nTransaction Failed: Sender account does not exist.")
            return

        if self.receiver not in accounts:
            self.status = "Failed - Receiver not found"
            print("\nTransaction Failed: Receiver account does not exist.")
            return

        if self.amount <= 0:
            self.status = "Failed - Invalid amount"
            print("\nTransaction Failed: Amount must be greater than zero.")
            return

        if accounts[self.sender] >= self.amount:
            accounts[self.sender] -= self.amount
            accounts[self.receiver] += self.amount
            self.status = "Success"
            print("\nTransaction Successful!")
            print(f"{self.amount} transferred from {self.sender} to {self.receiver}.")
        else:
            self.status = "Failed - Insufficient balance"
            print("\nTransaction Failed: Insufficient balance.")

    # Display transaction details
    def display_transaction(self):
        print("\n================ TRANSACTION DETAILS ================")
        print("Transaction ID :", self.tx_id)
        print("Sender         :", self.sender)
        print("Receiver       :", self.receiver)
        print("Amount         :", self.amount)
        print("Timestamp      :", self.timestamp)
        print("Status         :", self.status)


# Input transaction details
sender = input("Enter sender name: ").strip()
receiver = input("Enter receiver name: ").strip()
amount = float(input("Enter amount to transfer: "))

# Create transaction object
tx1 = Transaction(sender, receiver, amount)

# Perform transfer
tx1.transfer()

# Display transaction details
tx1.display_transaction()

# Display updated balances
print("\n================ UPDATED ACCOUNT BALANCES ================")
for user, balance in accounts.items():
    print(f"{user}: {balance:.2f}")
