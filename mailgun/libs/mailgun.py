import requests
from dotenv import load_dotenv
import os

load_dotenv()


class Mailgun:
    DOMAIN = os.environ.get('MAILGUN_DOMAIN')
    API_KEY = os.environ.get('MAILGUN_API')
    TO_ADDR = os.environ.get('TO_ADDRESS')
    FROM_NAME = 'kferenc'

    @classmethod
    def send_email(cls):
        return requests.post(
            f'https://api.mailgun.net/v3/{cls.DOMAIN}/messages',
            auth=("api", f'{cls.API_KEY}'),
            data={"from": f'{cls.FROM_NAME} <mailgun@{cls.DOMAIN}>',
                "to": [f"{cls.TO_ADDR}"],
                "subject": "Hello",
                "text": "Testing 5"})

