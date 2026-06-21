import requests
import json
from base64 import b64encode

rpc_user = "admin"
rpc_password = "admin1234"
rpc_url = "http://127.0.0.1:18443/"

credentials = b64encode(
    f"{rpc_user}:{rpc_password}".encode()
).decode("utf-8")

headers = {
    "Content-type": "application/json",
    "Authorization": f"Basic {credentials}"
}

def call_rpc(method, params=[]):
    payload = json.dumps({
        "jsonrpc": "1.0",
        "id": "python-client",
        "method": method,
        "params": params
    })

    response = requests.post(
        rpc_url,
        headers=headers,
        data=payload
    )

    return response.json()

print("Blockchain Info:", call_rpc("getblockchaininfo"))
print("Create Wallet:", call_rpc("createwallet", ["student_wallet_NEW"]))
print("New Address:", call_rpc("getnewaddress"))
print("Get Balance:", call_rpc("getbalance"))
print("List Transactions:", call_rpc("listtransactions"))