import os
import requests
from bs4 import BeautifulSoup
from loguru import logger

@logger.catch
def main(url :str) -> int: 
    headers = {
    	'cookie': 'vamhubconsent=yes',
    }
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    navs = soup.find('ul', {'class': 'pageNav-main'}).find_all('li')
    pages = int(navs[-1].get_text())
    return pages

if __name__ == '__main__':
	url = 'https://hub.virtamate.com/resources/categories/looks.7/'
	pages: int = main(url)
	print(pages)
	#Логгирование
	current_module = os.path.basename(__file__)
	message = f'Модуль {current_module}: {pages}'
	logger.add('debug.log', format='{time:DD:MM:YY hh:mm} | {level} | {message}', level='DEBUG', rotation='1MB', compression='zip')
	logger.debug(f'{message}')