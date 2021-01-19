from bs4 import BeautifulSoup
import urllib.request
import os

#  https://pypi.org/project/beautifulsoup4/


class Parser:
    raw_html = ''
    html = ''
    results = []
    path = ''

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = urllib.request.urlopen(self.url)
        self.raw_html = req.read()
        self.html = BeautifulSoup(self.raw_html, 'html.parser')
        print(self.html)

    def parsing(self):
        news = self.html.findAll('li', class_='liga-news-item')
        for item in news:
            title = item.find('span', class_='d-block').get_text(strip=True)
            description = item.find('span', class_='name-dop').get_text(strip=True)
            href = item.a.get('href')
            self.results.append({
                'title': title,
                'description': description,
                'href': href
            })

        print(self.results)

        self.url = self.url[12:23]
        f = open(self.url + '.txt', 'w', encoding='UTF-8')
        i = 1
        for item in self.results:
            f.write(
                f"News #{i}\n\ntitle: {item['title']}\n\ndescription: {item['description']}\n\nimage: {item['href']}\n\n***************************************")
        f.close()

    def run(self):
        self.get_html()
        self.parsing()
