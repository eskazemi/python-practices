import requests
from config import URL, HEADERS, rules
from mail import mailjet, generate_date
from notification import send
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
    if rules["email"].get("preferred") is not None:
        tmp = dict()
        for exc in rules["email"].get("preferred"):
            tmp = dict()
            tmp[exc] = rates[exc]
        rates = tmp
    data = generate_date(subject, json.dumps(rates))
    result = mailjet.send.create(data=data)
    print(result)


def check_rules_notif(rates):
    preferred = rules["notification"]["preferred"]
    message = ''
    for exc in preferred.keys():
        if rates[exc] <= preferred[exc]["min"]:
            message = f"{exc} reached min {preferred[exc]['min']}"
        elif rates[exc] >= preferred[exc]["max"]:
            message = f"{exc} reached max {preferred[exc]['max']}"
    return message


def send_notif(text=None):
    send(text)


if __name__ == "__main__":
    res = get_rate()
    if rules["archive"]:
        archive(res["timestamp"], res["rates"])
    if rules["email"].get("enable"):
        send_email(res["timestamp"], res["rates"])

    if rules["notification"].get("enable"):
        msg = check_rules_notif(res["rates"])
        if msg:
            send_notif(msg)
        else:
            print("Not event")
