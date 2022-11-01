from kavenegar import *
from config import rules, kavenegar_key




def send(text):
    try:
        api = KavenegarAPI(kavenegar_key)
        params = {'sender': '2000500666',
                  'receptor': rules["notification"]["receiver"],
                  'message': text}
        api.sms_send(params)
    except APIException as e:
        print(e)

    except HTTPException as e:
        print(e)

