import subprocess
import requests
import json

# from multiping import MultiPing
# from multiping import multi_ping

if __name__ == "__main__":

    datagram_response = requests.get(
    "https://raw.githubusercontent.com/SteamDatabase/SteamTracking/master/Random/NetworkDatagramConfig.json").json()

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

if datagram_response == 0:
    datagram_response.close()

with open('datagram.json', 'w') as json_datagram:
    json.dump(datagram_response, json_datagram)


def print_datagram():
    with open('datagram.json', 'r') as f:
        d = json.load(f)
    print(json.dumps(d, indent=4))


print("Updated datagram...\n")
print(datagram_response)
