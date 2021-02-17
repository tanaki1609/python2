import requests
from bs4 import BeautifulSoup


class Parser:
    def __init__(self, url):
        self.url = url

    def get_html_response(self):
        self.response = requests.get(self.url)
        self.html = BeautifulSoup(self.response.text, 'lxml')
        return self.html


class Broadway(Parser):
    def get_images(self):
        soup_data = self.html.find('body').find('section', class_='cs-affiche') \
            .find('div').find('div', class_='ajax_content').find_all('div', class_='one-film uk-grid uk-margin-remove')
        images = []
        for i in soup_data:
            image = 'https://broadway.kg' + \
                    i.find('div', class_='uk-width-1-3@l uk-margin-large-left uk-padding-remove') \
                        .find('div', class_='img-wrapper').find('img')['src'].strip()
            images.append(image)
        return images


class ManasCinema(Parser):
    def get_images(self):
        soup_data = self.html.find('div', class_='container') \
            .find('div', class_='contentBlock') \
            .find('div', id='slider-top').find_all('a')
        images = []
        for i in soup_data:
            images.append('http://manascinema.com' + i.find('img')['src'])
        return images


manas = ManasCinema('http://manascinema.com/')
manas.get_html_response()
print(manas.get_images())
