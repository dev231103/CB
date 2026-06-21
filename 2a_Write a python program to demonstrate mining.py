import hashlib 
import time 
 
# Define the mining function 
def mine_block(block_data, difficulty): 
    prefix_str = '0' * difficulty 
    nonce = 0 
    start_time = time.time() 
 
    print("Starting mining...") 
 
    while True: 
        text = f"{block_data}{nonce}" 
        hash_result = hashlib.sha256(text.encode()).hexdigest() 
 
        # Check if hash meets difficulty condition 
        if hash_result.startswith(prefix_str): 
            end_time = time.time() 
            print("Block mined successfully!") 
            print(f"Nonce: {nonce}") 
            print(f"Hash: {hash_result}") 
            print(f"Time taken: {end_time - start_time:.2f} seconds") 
            break 
 
        nonce += 1 
 
# Example usage 
block_data = "Alice pays Bob 10 BTC" 
difficulty = 4  # Number of leading zeros required 
mine_block(block_data, difficulty) 