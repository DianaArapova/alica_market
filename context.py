class Context:
    def __init__(self):
        self.size = None
        self.style = None
        self.price = None
        self.color = None
        self.step = 0

    def set_size(self, size):
        self.size = size

    def set_style(self, style):
        self.style = style

    def set_color(self, color):
        self.color = color

    def set_price(self, price):
        self.price = price

    def build_url(self):
        url = "https://www.lamoda.ru/c/369/clothes-platiya/?"
        res = []
        if self.size is not None:
            res.append(f"size_values={self.size}")
        if self.style is not None:
            res.append(f"property_style={self.style}")
        if self.price is not  None:
            res.append(f"price={self.price[0]}%2C{self.price[1]}")
        if self.color is not None:
            res.append(f"colors={self.color}")

        url += "&".join(res)
        return url

if __name__ == "__main__":
    context = Context()
    context.set_color(3865)
    context.set_size(42)
    context.set_price((799,3112))
    context.set_style(5924)
    print(context.build_url())
