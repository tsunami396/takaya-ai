from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('fqugOgWKg2o1kDKRl3NVdlrnYeXizBFijBvFdZwTnJvVL7FYYJmSMJl0IHisKlREuxBGKc6UzL77/O8nanL6ilcUeS3zUPixBF7rPQT0HVmuViRIQjpqFkGj5Ubc3YzJGEy818kBaAjEqyX9kI4xuAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ee1e21eecd3bc1253241f9e13de3f953')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()