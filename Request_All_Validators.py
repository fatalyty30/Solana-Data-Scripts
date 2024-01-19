
import requests
import json

endpoint = "https://side-solemn-scion.solana-mainnet.discover.quiknode.pro/accc22bd5e34979d58d147a2de4f6ce0c7b7def8/"

data = {
  "jsonrpc": "2.0",
  "id": 1,
  "method": "getVoteAccounts",
}

headers = {"Content-Type": "application/json"}
response = requests.post(url=endpoint, data=json.dumps(data), headers=headers)
json_response = response.json()

validators = []
for result in json_response["result"]["current"]: 
    validators.append(result["nodePubkey"])
print(f"The list of the validators is {validators}")
