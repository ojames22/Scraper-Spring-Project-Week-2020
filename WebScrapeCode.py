import requests
from bs4 import BeautifulSoup

def username():
	username = input('Enter username: ')

	print('Hello ' + username + '! Please enter values for month, day, and year for games and stats.')

	#date_value = input('Enter date:')
	#print('Date: ' + date_value)

#def get_date():
#	month = input('Enter month: ')
#	day = input('Enter day: ')
#	year = input('Enter year: ')

#	URL = 'https://www.basketball-reference.com/boxscores/?month=' + month + '&day=' + day +'&year=' + year
#	page = requests.get(URL)
#	print(URL)

def scrape_games():
	month = input('Enter month (--): ')
	day = input('Enter day (--): ')
	year = input('Enter year (----): ')

	"""Notes from RealPython.com:
	:param location: Where the job is located
	:type location: str
	:return: all job postings from first page that match the search results
	:rtype: BeautifulSoup object
	"""
	URL = 'https://www.basketball-reference.com/boxscores/?month=' + month + '&day=' + day +'&year=' + year
	print(URL)
	page = requests.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')
	results = soup.find('div', class_='game_summaries')
	return results

#def find_elements(data):
	#results = soup.find(id='month')


	#return results

def print_games(results):
	game_elems = results.find_all('div', class_='game_summary')

	for game_elem in game_elems:

		winner_elem = game_elem.find('tr', class_='winner')
		winner_name = winner_elem.find('a').get_text()
		winner_score = winner_elem.find('td', class_='right').get_text()

		loser_elem = game_elem.find('tr', class_='loser')
		loser_name = loser_elem.find('a').get_text()
		loser_score = loser_elem.find('td', class_='right').get_text()

		print('\nW: '+winner_name)
		print(winner_score)
		print('L: '+loser_name)
		print(loser_score)
		if None in (winner_elem,winner_score,loser_elem,loser_score):
			print('No games were played on this date.')


#Call scrape games
username()
results = scrape_games()
print_games(results)
#print(print_games)
#Pass results to print_games
#print(results)