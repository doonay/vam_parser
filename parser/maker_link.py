import os
from win32com.client import Dispatch
import requests
from loguru import logger

@logger.catch
def main(package_name: str, item_detail_url: str):
	litera = package_name[0].upper()
	link_path = os.path.join('links', litera)

	if not os.path.exists(link_path):
		os.mkdir(link_path)

	link_fullname = package_name.replace('.var', '.url')

	link_full_path = os.path.join(link_path, link_fullname)
	
	if not os.path.exists(link_full_path):
		shell = Dispatch('WScript.Shell')
		shortcut = shell.CreateShortCut(link_full_path)
		shortcut.TargetPath = item_detail_url
		shortcut.save()
	return link_full_path

if __name__ == '__main__':
	package_name = 'IAmAFox.Isabella.1.var'
	item_detail_url = 'https://hub.virtamate.com/resources/sara.43021/'
	if not os.path.exists('links'):
		os.mkdir('links')
	link_full_path = main(package_name, item_detail_url)
	#Логгирование
	current_module = os.path.basename(__file__)
	if os.path.exists(link_full_path):
		message = f'Модуль {current_module}: Файл {link_full_path} создан'
		logger.add('debug.log', format='{time:DD:MM:YY hh:mm} | {level} | {message}', level='DEBUG', rotation='1MB', compression='zip')
		logger.debug(f'{message}')
	else:
		message = f'Модуль downloader_image: Файл {link_full_path} отсутствует!'
		logger.add('debug.log', format='{time:DD:MM:YY hh:mm} | {level} | {message}', level='DEBUG', rotation='1MB', compression='zip')
		logger.debug(f'{message}')