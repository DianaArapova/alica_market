import os
import unittest

from .parser import Parser


class TestParser(unittest.TestCase):

    def setUp(self):
        with open(os.path.join('Parser', 'test_page.html'), 'r', encoding='utf8') as f:
            self.html_page = f.read()
        with open(os.path.join('Parser', 'test_item.html'), 'r', encoding='utf8') as f:
            self.test_item = f.read()

    def test_item_parsingCorrectly(self):
        parser = Parser()
        dress = parser._create_dress_by_div_item(self.test_item)
        self.assertEqual(dress.name, "Wallis / Платье")
        self.assertEqual(dress.price, '3 999 руб')
        self.assertEqual(dress.sizes, [44, 46, 48, 50, 52, 54, 56])
        self.assertEqual(dress.link, '/p/wa007ewccuk1/clothes-wallis-plate/')
        self.assertEqual(dress.img_preview, '//a.lmcdn.ru/pi/img236x341/W/A/WA007EWCCUK1_6966195_1_v1.jpg')


if __name__ == "__main__":
    unittest.main()