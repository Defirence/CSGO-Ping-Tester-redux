"""csgo-ping-tester-redux-v0.0.3-dev"""

import json
import sys
from io import open

import requests

datagram_response = requests.get('https://tinyurl.com/steamdatagram').json()

if __name__ == "__main__":
    datagram_response: requests.get('https://tinyurl.com/steamdatagram', verify=True, allow_redirects=True, timeout=60)
    if datagram_response == 200:
        datagram_response.close()
elif datagram_response != 200:
    datagram_response.close()
    print(f"Error: Response code did not return a 200 status code.{sys.exit(1)}")
elif datagram_response is None:
    print(f"Error: NoneType was returned in the response.{sys.exit(1)}")

keywords = [
    "revision", "certs", "p2p_share_ip",
    "revoked_keys", "relay_public_key", "typical_pings"
]

for x in keywords:
    if x in keywords:
        del datagram_response[x]

with open('datagram.json', mode='w', encoding='utf-8') as json_datagram_dump:
    json.dump(datagram_response, json_datagram_dump)


def print_datagram():
    """Opens the datagram response in json encoding"""
    with open('datagram.json', mode='r', encoding='json') as json_datagram:
        load_datagram = json.load(json_datagram)
    print(json.dumps(load_datagram, indent=4))


for key, value in datagram_response.items():
    print(f'{key} : {value}')

print(datagram_response.items())
print("\nPulled updated datagram response successfully...")

sys.exit(0)
