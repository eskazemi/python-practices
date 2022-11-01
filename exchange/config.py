URL = \
    "http://api.apilayer.com/fixer/latest?base=USD"

HEADERS = {
    "apikey": "YmdgCmACaGFPQcwTU8KhMtaMuz5X4ZrN"
}


rules = {
    "archive": True,
    "send_email": True,
    # preferred default is None
    "preferred": ["BTC", "IRR", "USD", "CAD", "IQD"]
}
