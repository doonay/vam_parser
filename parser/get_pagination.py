import os
import requests
from bs4 import BeautifulSoup
from loguru import logger
from get_logs import get_logs

# debug thing
current_module = os.path.basename(__file__)

@logger.catch
def get_pagination(url :str) -> int: 
    headers = {
    	'cookie': 'vamhubconsent=yes',
    }
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    navs = soup.find('ul', {'class': 'pageNav-main'}).find_all('li')
    pages = int(navs[-1].get_text())
    get_logs(current_module, pages)
    return pages

if __name__ == '__main__':
	url = 'https://hub.virtamate.com/resources/categories/looks.7/'
	pages: int = get_pagination(url)
	