import requests
from config import URL, HEADERS
import json

payload = {}


def get_rate():
    response = requests.request("GET", URL, headers=HEADERS, data=payload)

    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None


def archive(filename, rates):

    with open(f'archive/{filename}.json', 'w') as f:
        f.write(json.dumps(rates))



if __name__ == "__main__":
    res = get_rate()
    archive(res["timestamp"], res["rates"])
