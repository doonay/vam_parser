def main(item):
	container = item.find('div', {'class': 'structItem-iconContainer'})
	return container
		
if __name__ == '__main__':
	main()