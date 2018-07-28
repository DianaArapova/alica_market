import unittest
from translator import Translator
from Common.commands import Commands


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.translator = Translator()

    def test_something(self):
        print(self.translator.get_value("Мой саймый любимый цвет коралловый", Commands.Color))


if __name__ == '__main__':
    unittest.main()
