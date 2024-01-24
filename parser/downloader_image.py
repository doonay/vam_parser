import os
import requests
from loguru import logger

@logger.catch
def main(package_name: str, image_url: str):
	litera = package_name[0].upper()
	image_path = os.path.join('images', litera)
	image_good_path = os.path.join('images', f'{litera}_GOOD')
	image_bad_path = os.path.join('images', f'{litera}_BAD')

	if not os.path.exists(image_path):
		os.mkdir(image_path)

	if not os.path.exists(image_bad_path):
		os.mkdir(image_good_path)

	if not os.path.exists(image_bad_path):
		os.mkdir(image_bad_path)

	image_filename = package_name.replace('.var', '')
	image_extension = image_url.split('.')[-1]
	image_fullname = f'{image_filename}.{image_extension}'

	image_full_path = os.path.join(image_path, image_fullname)
	image_full_good_path = os.path.join(image_good_path, image_fullname)
	image_full_bad_path = os.path.join(image_bad_path, image_fullname)

	if not os.path.exists(image_full_path) or not os.path.exists(image_full_good_path) or not os.path.exists(image_full_bad_path):
		r = requests.get(image_url)
		with open(image_full_path, 'wb') as file:
			file.write(r.content)
	return image_full_path

if __name__ == '__main__':
	package_name = 'IAmAFox.Isabella.1.var'
	image_url = 'https://1387905758.rsc.cdn77.org/data/resource_icons/43/43014.jpg'
	if not os.path.exists('images'):
		os.mkdir('images')
	image_full_path = main(package_name, image_url)
	#Логгирование
	current_module = os.path.basename(__file__)
	if os.path.exists(image_full_path):
		message = f'Модуль {current_module}: Файл {image_full_path} скачан'
		logger.add('debug.log', format='{time:DD:MM:YY hh:mm} | {level} | {message}', level='DEBUG', rotation='1MB', compression='zip')
		logger.debug(f'{message}')
	else:
		message = f'Модуль downloader_image: Файл {image_full_path} отсутствует!'
		logger.add('debug.log', format='{time:DD:MM:YY hh:mm} | {level} | {message}', level='DEBUG', rotation='1MB', compression='zip')
		logger.debug(f'{message}')
	