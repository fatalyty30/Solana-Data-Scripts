import requests

endpoint = "https://bnbsmartchain-mainnet.infura.io/v3/2df9c43a1a0a472da29126ca32af74ff"
contract_address = "0x45c54210128a065de780C4B0Df3d16664f7f859e"
func_signature = "0xc48d6d5e"


def print_locked_amount(block_number):
  data = {
    "jsonrpc":
    "2.0",
    "method":
    "eth_call",
    "params": [{
      "to": contract_address,
      "data": func_signature
    }, "0x" + format(int(block_number))],
    "id":
    1
  }

  response = requests.post(endpoint, json=data)

  total_locked_amount = int(response.json()["result"], ) / 10**9
  print(
    f"Total locked amount: {total_locked_amount} CAKES were locked at block {block_number}"
  )
