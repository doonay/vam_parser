import os
from loguru import logger

# debug thing
current_module = os.path.basename(__file__)

def get_logs(current_module, message):
	message = f'{current_module}: {message}'
	logger.add('debug.log', format='{time:DD:MM:YY hh:mm} | {level} | {message}', level='DEBUG', rotation='1MB', compression='zip')
	logger.debug(f'{message}')

if __name__ == '__main__':
	get_logs(current_module, 'Hello, loguru!')