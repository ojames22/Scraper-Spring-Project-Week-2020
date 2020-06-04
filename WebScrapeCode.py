import requests
from bs4 import BeautifulSoup

def username():
	username = input('Enter username: ')

	print('Hello ' + username + '! Please enter a date for games and starts.')

	date_value = input('Enter date:')
	print('Date: ' + date_value)

def get_date():
	month = input('Enter month: ')
	day = input('Enter day: ')
	year = input('Enter year: ')

	URL = 'https://www.basketball-reference.com/boxscores/?month=' + month + '&day=' + day +'&year=' + year
	page = requests.get(URL)
	print(URL)

def scrape_games(location=None):
	month = input('Enter month: ')
	day = input('Enter day: ')
	year = input('Enter year: ')

	"""Notes from RealPython.com:
	:param location: Where the job is located
	:type location: str
	:return: all job postings from first page that match the search results
	:rtype: BeautifulSoup object
	"""
	if location:
		URL = (
			'https://www.basketball-reference.com/boxscores/'
			'?month&day&year{location}'
		)
	else:
		URL = 'https://www.basketball-reference.com/boxscores/?month=' + month + '&day=' + day +'&year=' + year
	page = requests.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')
	results = soup.find('div', {'class": "game_summaries'})
	return results

#def find_elements(data):
	#results = soup.find(id='month')


	#return results

def print_games(results):
	game_elems = results.find('div', {'class": "game_summary'})

	for game_elem in game_elems:
		#print(game_elem, end='\n'*2)
		winner_elem = game_elem.find('div', class_='winner')
		winnerScore_elem = game_elem.find('td', class_='right')
		loser_elem = game_elem.find('div', class_='loser')
		loserScore_elem = game_elem.find('td',class_='right')
		#if None in (winner_elem,winnerScore_elem,loser_elem,loserScore_elem):
	else:
		print('No games were played on this date.')
		print(winner_elem.text.strip)#Previously month_elem.text
		print(winnerScore_elem.text.strip)#Previously day_elem.text
		print(loser_elem.text.strip)#Previously year_elem.text
		print(loserScore_elem.text.strip)#Previously game_elem.text
		print()

#Call scrape games
results = scrape_games()
print_games(results)
#print(print_games)
#Pass results to print_games
#print(results)

#https://www.basketball-reference.com/boxscores/?month=1&day=1&year=2000