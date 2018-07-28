import json


class AliceResponse(object):
    def __init__(self, alice_request):
        print(type(alice_request))
        self._response_dict = {
            "version": alice_request.version,
            "session": alice_request.session,
            "response": {
                "end_session": False
            }
        }

    def dumps(self):
        return json.dumps(
            self._response_dict,
            ensure_ascii=False,
            indent=2
        )

    def set_text(self, text):
        self._response_dict['response']['text'] = text[:1024]

    def set_buttons(self, buttons):
        self._response_dict['response']['buttons'] = buttons

    def end(self):
        self._response_dict["response"]["end_session"] = True

    def __str__(self):
        return self.dumps()

    def add_image(self, im_id, title, description, url):
        if "card" not in self._response_dict["response"]:
            self._response_dict["response"]["card"] = {}
            self._response_dict["response"]["card"]["type"] = "ItemsList"
            self._response_dict["response"]["card"]["items"] =[]

        card = self._response_dict["response"]["card"]

        im_dict = {"image_id": im_id,
                   "title": title,
                   "description": description,
                   "button": {
                       "text": "платье",
                       "url": url
                   }
                   }
        card["items"].append(im_dict)

        # self._response_dict["response"]["card"]["image_id"] = "213044/662b5dfbdee1189d5fd6"
        # self._response_dict["response"]["card"]["title"] = "Заголовок"
        # self._response_dict["response"]["card"]["description"] = "Описание"
        # self._response_dict["response"]["card"]["button"] = {}
        # self._response_dict["response"]["card"]["button"]["text"] = "платье"
        # self._response_dict["response"]["card"]["button"]["url"] = "http://e1.ru"
        #  self._response_dict["card"]["button":] {
        #               "text": "какой то текст",
        #               "url": "http://mysite.com/",
        #               "payload": < any
        # json
        # object >,
