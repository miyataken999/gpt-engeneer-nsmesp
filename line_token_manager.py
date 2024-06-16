import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from linebot import LineBot

class LineTokenManager:
    def __init__(self, credentials_file, line_channel_access_token):
        self.credentials_file = credentials_file
        self.line_channel_access_token = line_channel_access_token
        self.service_account_credentials = service_account.Credentials.from_service_account_file(
            self.credentials_file, scopes=['https://www.googleapis.com/auth/script.projects']
        )
        self.service = build('script', 'v1', credentials=self.service_account_credentials)
        self.line_bot = LineBot(line_channel_access_token)

    def update_line_token(self, new_token):
        # Update Line token in Google Apps Script properties
        request_body = {
            'requests': [
                {
                    'updateScriptProperty': {
                        'resource': {
                            'scriptId': 'your_script_id',
                            'property': {
                                'key': 'LINE_TOKEN',
                                'value': new_token
                            }
                        }
                    }
                }
            ]
        }
        response = self.service.scripts().batchUpdate(body=request_body).execute()
        print(f'Updated Line token in Google Apps Script properties: {new_token}')

        # Update Line Webhook
        self.line_bot.set_webhook_url('https://your-webhook-url.com')

    def get_line_token(self):
        # Get Line token from Google Apps Script properties
        response = self.service.scripts().getScriptProperties(scriptId='your_script_id').execute()
        for prop in response.get('properties', []):
            if prop['key'] == 'LINE_TOKEN':
                return prop['value']
        return None