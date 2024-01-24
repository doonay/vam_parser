import os
import requests
from loguru import logger

@logger.catch
def main(button_url):
  session = requests.Session()
  headers = {
    'cookie': 'vamhubconsent=yes',
  }
  #переходим по ссылке с кнопки
  r = session.get(button_url, headers=headers, allow_redirects=False) #allow_redirects=False важный параметр!
  #затем получаем Location - https://1387905758.rsc.cdn77.org/internal_data/attachments/326/326917-fbcbee8422a118d508003b19ec634bbe.data
  cdn_url = r.headers['Location']
  
  #после чего переходим по ссылке локэйшен, что бы узнать имя пакета - IAmAFox.Isabella.1.var
  r = session.get(cdn_url, headers=headers, allow_redirects=False)
  filename = r.headers['content-disposition'][10:-2]
  #print('filename:', filename, cdn_url)
  package_data = {}
  package_data['package_name'] = filename
  package_data['package_url'] = cdn_url

  return package_data

if __name__ == '__main__':
  button_url = 'https://hub.virtamate.com/resources/the-barista.43014/download'
  package_data = main(button_url)
  #Логгирование
  current_module = os.path.basename(__file__)
  message = f'Модуль {current_module}: {package_data}'
  logger.add('debug.log', format='{time:DD:MM:YY hh:mm} | {level} | {message}', level='DEBUG', rotation='1MB', compression='zip')
  logger.debug(f'{message}')
