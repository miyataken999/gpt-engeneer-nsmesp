from linebot import LineBot, WebhookHandler
from linebot.models import MessageEvent, TextMessage

class LineWebhookHandler:
    def __init__(self, line_channel_access_token):
        self.line_bot = LineBot(line_channel_access_token)
        self.handler = WebhookHandler(line_channel_access_token)

    def handle_webhook(self, request):
        events = self.handler.handle(request.get_json(), request.headers)
        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    # Handle text message
                    print(f'Received text message: {event.message.text}')
                    # Process message
                    # ...
                    # Respond to user
                    self.line_bot.reply_message(event.reply_token, 'Thank you for your message!')