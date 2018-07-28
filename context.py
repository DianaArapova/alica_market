
class Context:
    def __init__(self):
        self.size = 42
        self.style = ""
        self.price = (0,180000)
        self.color = "red"
        self.step = 0

    def set_size(self, size):
        self.size = size

    def set_style(self, style):
        self.style = style

    def set_color(self, color):
        self.color = color

    def set_price(self, lower_price):
        self.price = (lower_price, self.price[1])

    def build_url(self):
        return ""