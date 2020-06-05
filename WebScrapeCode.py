import requests
from bs4 import BeautifulSoup

def username():
	username = input('Enter username: ')

	print('Hello ' + username + '! Please enter values for month, day, and year for NBA games and scores.')

def scrape_games():
	month = input('Enter month (--): ')
	day = input('Enter day (--): ')
	year = input('Enter year (----): ')

	try:
		val = int(month)
		val = int(day)
		val = int(year)
		print("Inputs are integers. Inputs/Given Date: = " + month+"/"+day+"/"+year)
	except ValueError:
		try:
			val = float(month)
			val = float(day)
			val = float(year)
			print("Inputs are float values. Inputs/Given Date: = " + month+"/"+day+"/"+year)
		except ValueError:
			print("Unable to process. Input is not a number, it's a string. Please try again.")

	URL = 'https://www.basketball-reference.com/boxscores/?month=' + month + '&day=' + day +'&year=' + year
	#print(URL)
	page = requests.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')
	results = soup.find('div', class_='game_summaries')
	return results

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
		if None in (results, game_elems):
			print('No games were played on this date.')

username()
results = scrape_games()
print_games(results)
print('\nSource: basketball-reference.com')