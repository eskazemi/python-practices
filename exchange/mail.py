from config import MJ_APIKEY_PUBLIC
from config import MJ_APIKEY_PRIVATE
from mailjet_rest import Client

api_key = MJ_APIKEY_PUBLIC
api_secret = MJ_APIKEY_PRIVATE
mailjet = Client(auth=(api_key, api_secret), version='v3.1')


def generate_date(subject : str, body):
    data = {
        'Messages': [
            {
                "From": {
                    "Email": "ksm182014@gmail.com",
                    "Name": "Me"
                },
                "To": [
                    {
                        "Email": "smk182018@gmail.com",
                        "Name": "You"
                    }
                ],
                "Subject": subject,
                "TextPart": "Greetings from Mailjet!",
                "HTMLPart": f"rates list {body}"
            }
        ]
    }
    return data
