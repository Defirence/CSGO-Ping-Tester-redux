"""csgo-ping-tester-redux-v0.0.1-dev"""

from io import open
import json
import requests

if __name__ == "__main__":

    datagram_response = requests.get("https://tinyurl.com/steamdatagram").json()
    if datagram_response == 0:
        datagram_response.close()

keywords = [
    "revision", "certs", "p2p_share_ip",
    "revoked_keys", "relay_public_key", "typical_pings"
]
for x in keywords:
    if x in datagram_response:
        del datagram_response[x]


def pull_keyvalues():
    datagram_response.get("ams")


print(pull_keyvalues)
# PyCharm and Python3.9.6 on Windows 11 v21H2 OS Build 22000.739 breaks with an error:
# with open('datagram.json', mode='w', encoding='json') as json_datagram_dump:
# LookupError: unknown encoding: json
# This is possibly due to the .json() method being called on L9

# Pylint will warn about using `open` here without specifying `json` encoding.

# with open('datagram.json', mode='w', encoding='json') as json_datagram_dump:
#    json.dump(datagram_response, json_datagram_dump)

with open('datagram.json', mode='w') as json_datagram_dump:
    json.dump(datagram_response, json_datagram_dump)


def print_datagram():
    """dumps and then opens the datagram json"""
    with open('datagram.json', mode='r', encoding='json') as json_datagram:
        load_datagram = json.load(json_datagram)
    print(json.dumps(load_datagram, indent=4))


print("Updated datagram...\n")
print(datagram_response)
