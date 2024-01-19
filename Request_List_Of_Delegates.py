import requests
import json

endpoint = "https://side-solemn-scion.solana-mainnet.discover.quiknode.pro/accc22bd5e34979d58d147a2de4f6ce0c7b7def8/"

rpc_data = {
  "jsonrpc":
  "2.0",
  "id":
  1,
  "method":
  "getTokenAccountsByDelegate",
  "params": [
    'Awes4Tr6TX8JDzEhCZY2QVNimT6iD1zWHzf1vNyGvpLM', {
      "programId": 'Stake11111111111111111111111111111111111111'
    }, {
      "encoding": "jsonParsed"
    }
  ]
}

headers = {"Content-Type": "application/json"}
response = requests.post(url=endpoint,
                         data=json.dumps(rpc_data),
                         headers=headers)
json_response = response.json()

delegates = []
for result in json_response["result"]["value"]["account"]["data"]:
  delegates.append(result["delegate"])
print(f"The list of the delegates is {delegates}")
