from flask import Flask, request
from AliceRequest import AliceRequest
from AliceResponse import AliceResponse
from manager import Manager
server = Flask(__name__)
manager = Manager()



@server.route("/", methods=['POST'])
def get_message():
    requestDict = AliceRequest(request.stream.read().decode("utf-8"))
    response = manager.manage(requestDict)

    return AliceResponse(response), 200
    return '''{
  "response": {
    "text": "Здравствуйте! Это мы, хороводоведы.",
    "tts": "Здравствуйте! Это мы, хоров+одо в+еды.",
    "buttons": [
        {
            "title": "Надпись на кнопке",
            "payload": {},
            "url": "https://example.com/",
            "hide": true
        }
    ],
    "end_session": false
  },
  "session": {
    "session_id": "2eac4854-fce721f3-b845abba-20d60",
    "message_id": 4,
    "user_id": "AC9WC3DF6FCE052E45A4566A48E6B7193774B84814CE49A922E163B8B29881DC"
  },
  "version": "1.0"
}''', 200

if __name__ == "__main__":

    server.run("127.0.0.1", 8000)