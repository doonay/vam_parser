import os
import requests
from loguru import logger

@logger.catch
def main(package_data):
	litera = package_data['package_name'][0].upper()

	package_path = os.path.join('packages', litera)
	
	if not os.path.exists(package_path):
		os.mkdir(package_path)

	package_filename = package_data['package_name']
	package_url = package_data['package_url']
	package_full_path = os.path.join(package_path, package_filename)
	
	if not os.path.exists(package_full_path):
		r = requests.get(package_url)
		with open(package_full_path, 'wb') as file:
			file.write(r.content)
	return package_full_path

if __name__ == '__main__':
	package_data = {'package_name': 'IAmAFox.Isabella.1.var', 'package_url': 'https://1387905758.rsc.cdn77.org/internal_data/attachments/326/326917-fbcbee8422a118d508003b19ec634bbe.data'}
	if not os.path.exists('packages'):
		os.mkdir('packages')
	package_full_path = main(package_data)
	#Логгирование
	current_module = os.path.basename(__file__)
	if os.path.exists(package_full_path):
		message = f'Модуль {current_module}: Файл {package_full_path} скачан.'
		logger.add('debug.log', format='{time:DD:MM:YY hh:mm} | {level} | {message}', level='DEBUG', rotation='1MB', compression='zip')
		logger.debug(f'{message}')
	else:
		message = f'Модуль downloader_image: Файл {package_full_path} отсутствует!'
		logger.add('debug.log', format='{time:DD:MM:YY hh:mm} | {level} | {message}', level='DEBUG', rotation='1MB', compression='zip')
		logger.debug(f'{message}')

	