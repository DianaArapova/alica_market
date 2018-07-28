from Common.commands import Commands


class Translator:
    def __init__(self):
        self.words_for_price = {"дешев": (0, 1000), "средн": (0, 3000), "миллио": (30000, 400000)}
        self.words_for_style = {"Вечер": "5924", "красив" : "5924", "дел": "5926", "повседнев": "5922", "спорт": "5925"}
        self.words_for_color = {
            "розов" : "623",
            "белый" : "615",
            "бежевый": "647",
            "кораллов": "30859",
            "желтый": "613",
            "жёлтый": "613",
            "зел": "637",
            "бирюзов": "30862",
            "голуб": "859",
            "оранже": "629",
            "сереб": "3843"
        }

    def get_value(self, text, command):
        if command == Commands.Price:
            return self.get_value_to_price(text.lower())
        if command == Commands.Style:
            return self.get_value_to_style(text.lower())
        if command == Commands.Size:
            sizes = self.get_ints_from_text(text.lower())
            if len(sizes) >= 1:
                return sizes[0]
            return None
        if command == Commands.Color:
            for word_for_color in self.words_for_color:
                if text.find(word_for_color) != -1:
                    return self.words_for_color[word_for_color]
            return None

    def get_value_to_style(self, text):
        for word_for_style in self.words_for_style:
            if text.find(word_for_style) != -1:
                return self.words_for_style[word_for_style]
        return None

    def get_value_to_price(self, text):
        for word_for_price in self.words_for_price:
            price = self.words_for_price[word_for_price]
            if text.find(word_for_price) != -1:
                return price
        prices = self.get_ints_from_text(text)
        if len(prices) == 1:
            if text.find("до") != -1:
                return (prices[0], 100000)
            return (0, prices[0])
        if len(prices) >= 2:
            return (prices[0], prices[1])
        return None

    def get_ints_from_text(self, text):
        ints = []
        for word in text.split():
            if self.is_int(word):
                ints.append(int(word))
        ints.sort()
        return ints

    @staticmethod
    def is_int(text):
        for w in text:
            if not w.isnumeric():
                return False
        return True