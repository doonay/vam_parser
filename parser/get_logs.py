import os
from loguru import logger

# debug thing
current_module = os.path.basename(__file__)
# logging
def get_logs(message):
	message = f'{current_module}: {message}'
	logger.add('debug.log', format='{time:DD:MM:YY hh:mm} | {level} | {message}', level='DEBUG', rotation='1MB', compression='zip')
	logger.debug(f'{message}')

if __name__ == '__main__':
	logging('Hello, loguru!')