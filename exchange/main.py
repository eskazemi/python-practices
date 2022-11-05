from datetime import datetime
from config import rules, API_KEY
from mail import mailjet, generate_date
from notification import send
from khayyam import JalaliDatetime
from fixer import get_rates
import json



def archive(filename, rates):
    """
    This function get filename and rates , save them to the specific directory
    rates
    Args:
        filename
        rates
    Raises:
        TypeError
    Returns:
        ...
    """
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


def check_rules_notif(rates):
    preferred = rules["notification"]["preferred"]
    message = ''
    for exc in preferred.keys():
        if rates[exc] <= preferred[exc]["min"]:
            message = f"{exc} reached min {preferred[exc]['min']} \n"
        elif rates[exc] >= preferred[exc]["max"]:
            message = f"{exc} reached max {preferred[exc]['max']} \n"
    return message


def send_notif(text=None):
    now = JalaliDatetime(datetime.now()).strftime('%y-%B-%d  %A  %H:%M')
    text = text + now
    send(text)


if __name__ == "__main__":
    res = get_rates(API_KEY)
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
