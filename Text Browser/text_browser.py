# Text Browser

from os import mkdir
from bs4 import BeautifulSoup
from collections import deque
from colorama import Style, Fore
import requests


class TextBasedBrowser:
    def __init__(self, directory):
        self.tabs = {}
        self.directory = directory
        self.cache = deque()
        try:
            mkdir(self.directory)
        except FileExistsError:
            pass

    def open_site(self, url):
        with open(self.tabs[url], 'r') as tab:
            return tab.read()

    def cache_site(self, name, content):
        namesList = name.split('.')
        if len(namesList) > 1 and not self.tabs.get(namesList[1]):
            with open(f'{self.directory}/{namesList[0]}.txt', 'w') as tab:
                tab.write(content)
            self.tabs[namesList[0]] = f'{self.directory}/{namesList[0]}.txt'
            self.cache.appendleft(namesList[0])

    @staticmethod
    def get_tags(content):
        tags = ['p', 'a', 'ul', 'ol', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
        soup = BeautifulSoup(content, 'html.parser').body.descendants
        page = ""
        for descendant in soup:
            if descendant.name in tags:
                if descendant.name == 'a':
                    page += Fore.BLUE + descendant.get_text().strip() + '\n'
                else:
                    page += Style.RESET_ALL + descendant.get_text().strip() + '\n'
        return page

    def check_url(self, url):
        try:
            if url.startswith('http'):
                return self.request(url)
            return self.request('https://' + url)
        except requests.exceptions.RequestException:
            return 'Something wrong with connection'

    def request(self, url):
        request = requests.get(url)
        clean_page = self.get_tags(request.content)
        self.cache_site(url.lstrip('https://'), clean_page)
        return clean_page

    def back_button(self):
        if len(self.cache) == 1:
            return 'History is Empty'
        try:
            with open(self.cache.pop(), 'r') as cached:
                return cached.read()
        except FileNotFoundError:
            return 'Error'
        except IndexError:
            return 'History is already empty'

def main(folder='sites'):
    browser = TextBasedBrowser(folder)
    while True:
        print(Fore.LIGHTRED_EX + '')
        url = input('Input site URL:\n> ')
        if '.' in url:
            print(browser.check_url(url))
        elif url in browser.tabs:
            print(browser.open_site(url))
        elif url == 'back':
            print(browser.back_button())
        elif url == 'exit':
            break
        else:
            print('Error')

if __name__ == '__main__':
    main()

