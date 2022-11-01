URL = \
    "http://api.apilayer.com/fixer/latest?base=USD"

HEADERS = {
    "apikey": "YmdgCmACaGFPQcwTU8KhMtaMuz5X4ZrN"
}

kavenegar_key ='54325078707872505A6A654168745145656B39335544484A55774670715947666846616C3730636E6F796B3D'

MJ_APIKEY_PUBLIC = 'b74c89f61cbe7864da3f07da85e30224'
MJ_APIKEY_PRIVATE = '4fac0ec73a7d8c532b5b0a1a40278c65'

rules = {
    "archive": True,
    "email": {
        "enable": False,
        "receiver": "",
        # preferred default is None
        "preferred": ["BTC", "IRR", "USD", "CAD", "IQD"]

    },
    "notification": {
        "enable": True,
        "receiver": "09027818262",
        # preferred default is None
        "preferred": {
            "BTC": {"min": 0.000101, "max": 0.000110},
            "ETB": {"min": 53.58, "max": 59}
        }
    },
}
