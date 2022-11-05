import requests

Base_Path = \
    "http://api.apilayer.com/fixer/latest?base=USD"

import json

payload = {}


def get_rates(api_key):
    """
    This function send a get request to the fixer.io api and get live
    rates
    Args:
        Not Argument
    Raises:
        ...
    Returns:
        list rates
    """
    HEADERS = {
        "apikey": api_key
    }
    response = requests.request("GET", Base_Path,
                                headers=HEADERS, data=payload)

    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None
