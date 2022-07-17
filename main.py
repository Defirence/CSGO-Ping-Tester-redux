"""csgo-ping-tester-redux-v0.0.2-dev"""

import sys
from io import open
import json
import requests

if __name__ == "__main__":

    datagram_response = requests.get("https://tinyurl.com/steamdatagram").json()
    if datagram_response == 200:
        datagram_response.close()
# TODO: Implement a better error handing function.
#    else:
#        print("Error retrieving datagram from specified URL...")
#        sys.exit(1)
# FIXME: Implement a better class for different keywords and methods.
keywords = [
    "revision", "certs", "p2p_share_ip",
    "revoked_keys", "relay_public_key", "typical_pings"
]

for x in keywords:
    if x in keywords:
        del datagram_response[x]

# FIXME: Using open without explicit json encoding.
with open('datagram.json', mode='w') as json_datagram_dump:
    json.dump(datagram_response, json_datagram_dump)


def print_datagram():
    # TODO: Missing function docstring, I really don't care less about docstrings.
    with open('datagram.json', mode='r', encoding='json') as json_datagram:
        load_datagram = json.load(json_datagram)
    print(json.dumps(load_datagram, indent=4))


for key, value in datagram_response.items():
    print(f'{key} : {value}')

# FIXME: Print the entire json response, but only values needed.
# print(datagram_response)
print("\nPulled updated datagram response successfully...")

sys.exit(0)
