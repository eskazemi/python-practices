import requests
from config import URL, HEADERS, rules
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


def send_email(date, rates):
    subject = f"{date} rates"
    if rules["preferred"] is not None:
        tmp = dict()
        for exc in rules["preferred"]:
            tmp = dict()
            tmp[exc] = rates[exc]
        rates = tmp
    body = json.dumps(rates)


if __name__ == "__main__":
    res = get_rate()
    if rules["archive"]:
        archive(res["timestamp"], res["rates"])
    if rules["send_email"]:
        send_email(res["timestamp"], res["rates"])
