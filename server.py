from flask import Flask, request
from AliceRequest import AliceRequest
from AliceResponse import AliceResponse
from manager import Manager
from context import Context


server = Flask(__name__)
manager = Manager()


sessions = dict()


@server.route("/", methods=['POST'])
def get_message():
    print("Kek")
    print(request.get_json())
    requestDict = AliceRequest(request.get_json())

    if requestDict.session_id not in sessions:
        sessions[requestDict.session_id] = Context()

    response = manager.manage(requestDict, sessions)

    return response, 200
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