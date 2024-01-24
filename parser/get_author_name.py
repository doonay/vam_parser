import os
import requests
from bs4 import BeautifulSoup
from loguru import logger

@logger.catch
def main(item):
    author = item.find('a', {'class':"username"}).text.replace('*', '-')
    return author
    
if __name__ == '__main__':
    url = f'https://hub.virtamate.com/resources/categories/looks.7/?page=1'
    headers = {
        'cookie': 'vamhubconsent=yes' #добавил укороченные хэдеры! проверить!
    }
    r = requests.get(url, headers=headers) #хэдэры не убирать!!! даже с сессией требуется кук доступа 18+
    soup = BeautifulSoup(r.text, 'lxml')
    items = soup.find('div', {'class': ['structItemContainer']}).find_all('div', {'class': ['structItem', 'structItem--resource', 'is-prefix1', 'js-inlineModContainer']})
    for item in items:
        author = main(item)
        #Логгирование
        current_module = os.path.basename(__file__)
        message = f'Модуль {current_module}: {author}'
        logger.add('debug.log', format='{time:DD:MM:YY hh:mm} | {level} | {message}', level='DEBUG', rotation='1MB', compression='zip')
        logger.debug(f'{message}')
        break