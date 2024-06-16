from line_token_manager import LineTokenManager
from line_webhook_handler import LineWebhookHandler

if __name__ == '__main__':
    credentials_file = 'path/to/credentials.json'
    line_channel_access_token = 'your_line_channel_access_token'

    line_token_manager = LineTokenManager(credentials_file, line_channel_access_token)
    line_webhook_handler = LineWebhookHandler(line_channel_access_token)

    # Update Line token
    new_token = 'new_line_token'
    line_token_manager.update_line_token(new_token)

    # Handle webhook
    @app.route('/webhook', methods=['POST'])
    def handle_webhook():
        request = flask.request
        line_webhook_handler.handle_webhook(request)
        return 'OK'

    if __name__ == '__main__':
        app.run(debug=True)