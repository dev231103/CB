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
    "content-type": "application/json",
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

def call_wallet_rpc(wallet_name, method, params=[]):
    url = rpc_url + f"wallet/{wallet_name}"
    payload = json.dumps({
        "jsonrpc": "1.0",
        "id": "python-client",
        "method": method,
        "params": params
    })
    response = requests.post(
        url,
        headers=headers,
        data=payload
    )
    return response.json()

info = call_rpc("getblockchaininfo")
print("Blockchain Info:\n", json.dumps(info, indent=4))

wallet_name = "student_wallet_2c"
call_rpc("createwallet", [wallet_name])
print("Wallet Created:", wallet_name)

address_resp = call_wallet_rpc(wallet_name, "getnewaddress")
btc_address = address_resp["result"]
print("New BTC Address:", btc_address)

mined_blocks = call_rpc("generatetoaddress", [101, btc_address])
print("Blocks Mined:", len(mined_blocks["result"]))

balance = call_wallet_rpc(wallet_name, "getbalance")
print("Wallet Balance:", balance["result"], "BTC")

recipient_resp = call_wallet_rpc(wallet_name, "getnewaddress")
recipient_address = recipient_resp["result"]
print("Recipient Address:", recipient_address)

send_tx = call_wallet_rpc(
    wallet_name,
    "sendtoaddress",
    [recipient_address, 0.5]
)
print("Transaction ID:", send_tx["result"])

transactions = call_wallet_rpc(
    wallet_name,
    "listtransactions"
)
print(
    "Recent Transactions:\n",
    json.dumps(transactions["result"], indent=4)
)

mempool = call_rpc("getrawmempool")
print("Mempool Transaction IDs:", mempool["result"])