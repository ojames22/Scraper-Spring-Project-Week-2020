import requests
from bs4 import BeautifulSoup

def username():
	username = input("Enter username: ")

	print("Hello " + username + "! Please enter a date for games and starts.")

	date_value = input("Enter date:")
	print("Date: " + date_value)

def getPersonName():
	name = "G"
	return name

def scrape_jobs(location=None):
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
        URL = 'https://www.basketball-reference.com/boxscores/?month&day&year'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="ResultsContainer")
    return results

def find_elements():
	results = soup.find(id='month')

	results = soup.find(id='day')

	results = soup.find(id='year')

	return results

def print_games(results):
	game_elems = results.find_all("section", class_="index")

	for game_elem in game_elems:
    month_elem = game_elem.find('h2', class_='month')
    day_elem = game_elem.find('div', class_='day')
    year_elem = game_elem.find('div', class_='year')
    print(month_elem.text)
    print(day_elem.text)
    print(year_elem.text)
    print()

#print(page)
''' Evidently, I am missing an interface in which the month, day, and year can be entered into.
Unless I further behind in the process
'''

#https://www.basketball-reference.com/boxscores/?month=1&day=1&year=2000

#class