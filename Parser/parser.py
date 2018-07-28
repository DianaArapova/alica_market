import requests
from bs4 import BeautifulSoup
from time import time

class Parser:
    def __init__(self, url='https://www.lamoda.ru/c/369/clothes-platiya/'):
        self.html_page = self._get_html_with_dresses(url)
        self.soup = BeautifulSoup(self.html_page, 'html.parser')

    # todo: учитывать размер и список просмотренного
    def get_dresses(self) -> list:
        return [self._create_dress_by_div_item(item) for item in self._get_all_div_items()]

    def _get_all_div_items(self):
        return self.soup.find_all('div', class_='products-list-item_dyother_dyMonitor')

    def _create_dress_by_div_item(self, products_list_item_div: str):
        soup = BeautifulSoup(products_list_item_div, "html.parser")

        name = soup.find('div', class_="products-list-item__brand").get_text().strip()
        price = soup.find('span', class_="price").get_text().strip()
        sizes = [int(size.get_text()) for size in soup.find_all('a', class_="products-list-item__size-item link")]
        link = soup.find('a', class_="products-list-item__link link").get('href').strip()
        img_preview = soup.find('img', class_="products-list-item__img").get('src').strip()

        return DressInfo(name, price, sizes, link, img_preview)

    def _get_html_with_dresses(self, url: str):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        request = requests.get(url, headers)
        if request.status_code != 200:
            raise Exception(f'Ошибка доступа к {url}. Результат запроса страницы вернул ответ {request.status_code}')
        return request.text


class DressInfo:
    def __init__(self, name, price, sizes, url, img_preview):
        self.name = name
        self.price = price
        self.sizes = sizes
        self.url = url
        self.id = hash(url)
        self.img_preview = img_preview

if __name__ == "__main__":
    a = time()
    parser = Parser().get_dresses()
    print(time()-a)