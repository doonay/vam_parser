import os
import requests
from bs4 import BeautifulSoup
from loguru import logger

@logger.catch
def main(item_detail_url):
	item_id = item_detail_url.split('/')[-2].split('.')[-1]
	return item_id

if __name__ == '__main__':
	item_detail_url = 'https://hub.virtamate.com/resources/the-barista.43014/'
	item_id = main(item_detail_url)
	#Логгирование
	current_module = os.path.basename(__file__)
	message = f'Модуль {current_module}: {item_id}'
	logger.add('debug.log', format='{time:DD:MM:YY hh:mm} | {level} | {message}', level='DEBUG', rotation='1MB', compression='zip')
	logger.debug(f'{message}')
