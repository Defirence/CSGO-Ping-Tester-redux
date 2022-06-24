import json
import requests
from io import open

# from multiping import multi_ping
# from multiping import MultiPing

'''csgo-ping-tester-redux-v0.0.1'''
if __name__ == "__main__":

    datagram_response = requests.get("https://tinyurl.com/steamdatagram").json()

if datagram_response == 0:
    datagram_response.close()

if "certs" in datagram_response:
    del datagram_response["certs"]

if "p2p_share_ip" in datagram_response:
    del datagram_response["p2p_share_ip"]

if "revoked_keys" in datagram_response:
    del datagram_response["revoked_keys"]

if "relay_public_key" in datagram_response:
    del datagram_response["relay_public_key"]

if "typical_pings" in datagram_response:
    del datagram_response["typical_pings"]

with open('datagram.json', mode='w', encoding="json") as json_datagram_dump:
    json.dump(datagram_response, json_datagram_dump)

'''Dumps the json data from the tinyurl var and then opens the .json file for reading'''


def print_datagram():
    with open('datagram.json', mode='r', encoding="json") as json_datagram:
        load_datagram = json.load(json_datagram)
    print(json.dumps(load_datagram, indent=4))


print("Updated datagram...\n")
print(datagram_response)
