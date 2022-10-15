import os

BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    print('BOT_TOKEN not set')
    quit()

APP_NAME = os.getenv('FLY_APP_NAME')

# webhook settings
WEBHOOK_HOST = f'https://{APP_NAME}.fly.dev'
WEBHOOK_PATH = f'/webhook/{BOT_TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = 8080
