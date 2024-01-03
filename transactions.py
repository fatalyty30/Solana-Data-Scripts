import requests

endpoint = "https://bnbsmartchain-mainnet.infura.io/v3/2df9c43a1a0a472da29126ca32af74ff"
deposit_method = "0xe2bbb158"
contract_address = "0x45c54210128a065de780C4B0Df3d16664f7f859e"

data = {
    "jsonrpc": "2.0",
    "method": "eth_getLogs",
    "params": [
      {"address": contract_address, 
       "fromBlock": 0, 
       "toBlock": "latest", 
       "topics": [[deposit_method]]
      }
    ],
    "id": 1
}

response = requests.post(endpoint, json=data)
deposit_events = response.json()["result"]

for event in deposit_events:
    tx_hash = event["transactionHash"]
    print(f"- Deposit transaction hash: {tx_hash}")

