from AliceRequest import AliceRequest
from AliceResponse import AliceResponse
from script import Script


class Manager:
    def __init__(self):
        self.script = Script().script

    def manage(self, aliceRequest:AliceRequest, sessions: dict):
        session = sessions[aliceRequest.session_id]
        response = AliceResponse(aliceRequest)

        if session.step == 0:
            sessions[aliceRequest.session_id].set_size(aliceRequest.command)

        if session.step == 1:
            sessions[aliceRequest.session_id].set_style(aliceRequest.command)

        if session.step == 2:
            sessions[aliceRequest.session_id].set_color(aliceRequest.command)

        if session.step == 3:
            sessions[aliceRequest.session_id].set_price(aliceRequest.command)

        if session.step < len(self.script):
            response.set_text(self.script[session.step])
        else:
            response.set_text("Мы подобрали тебе платье, но пока его тебе не покажем")

        sessions[aliceRequest.session_id].step += 1
        return response.dumps()