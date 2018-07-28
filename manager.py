from AliceRequest import AliceRequest
from AliceResponse import AliceResponse
from script import Script
from translator import Translator
from Common.commands import Commands


class Manager:
    def __init__(self):
        self.script = Script().script
        self.first_mes = Script().first_message
        self.translator = Translator()

    def manage(self, aliceRequest:AliceRequest, sessions: dict):
        if aliceRequest.is_new_session:
            return self.first_mes

        session = sessions[aliceRequest.session_id]
        response = AliceResponse(aliceRequest)

        if session.step == 0:
            sessions[aliceRequest.session_id].set_size(self.translator.get_value(aliceRequest.command, Commands.Size))

        if session.step == 1:
            sessions[aliceRequest.session_id].set_style(self.translator.get_value(aliceRequest.command, Commands.Style))

        if session.step == 2:
            sessions[aliceRequest.session_id].set_color(self.translator.get_value(aliceRequest.command, Commands.Color))

        if session.step == 3:
            sessions[aliceRequest.session_id].set_price(self.translator.get_value(aliceRequest.command, Commands.Price))

        if session.step < len(self.script):
            response.set_text(self.script[session.step])
        else:
            response.set_text("Мы подобрали тебе платье, но пока его тебе не покажем")
            response.add_image("213044/662b5dfbdee1189d5fd6", "Title", "123", "http://e1.ru")

        sessions[aliceRequest.session_id].step += 1
        return response.dumps()