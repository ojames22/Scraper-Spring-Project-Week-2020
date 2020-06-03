import requests

def username():
	username = input("Enter username: ")

	print("Hello " + username + "! Please enter a date for games and starts.")

	date_value = input("Enter date:")
	print("Date: " + date_value)

def getPersonName():
	name = "G"
	return name

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)
print(page)