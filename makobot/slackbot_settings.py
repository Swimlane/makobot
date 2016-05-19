import os

API_TOKEN = os.getenv('SLACK_TOKEN')

default_reply = "Sorry, I didn't understand you"

PLUGINS = ['makobot.bots']

THREATCONNECT_ACCESS_ID = os.getenv('THREATCONNECT_ACCESS_ID')
THREATCONNECT_SECRET_KEY = os.getenv('THREATCONNECT_SECRET_KEY')
THREATCONNECT_DEFAULT_ORG = os.getenv('THREATCONNECT_DEFAULT_ORG')
THREATCONNECT_BASE_URL = os.getenv('THREATCONNECT_BASE_URL',
                                   'https://api.threatconnect.com')

VIRUSTOTAL_API_KEY = os.getenv('VIRUSTOTAL_API_KEY')

XFORCE_API_KEY = os.getenv('XFORCE_API_KEY')
XFORCE_PASSWORD = os.getenv('XFORCE_PASSWORD')
