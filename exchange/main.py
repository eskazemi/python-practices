import requests
from config import URL, HEADERS

payload = {}


def get_rate():
    response = requests.request("GET", URL, headers=HEADERS, data=payload)

    status_code = response.status_code
    result = response.text
    return result


if __name__ == "__main__":
    print(get_rate())
