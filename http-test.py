import requests
from bs4 import BeautifulSoup

# Class for handling event data
class Data():
	def __init__(self):
		self.date = []
		
	def add_data(self, data):
		self.date.append(data)
		
	def print_data(self):
		for i in self.date:
			print(i)

def main():
	results = Data()

	bar_loose_html = requests.get('https://barloose.com/')
	helsinki_json = requests.get('http://open-api.myhelsinki.fi/v1/events/')
	
	# Handle Bar Loose event data
	feed = bar_loose_html.text
	
	soup = BeautifulSoup(feed, 'html.parser')
	
	event_date_tags = soup.find_all('time')
	event_dates = []
	
	for date in event_date_tags:
		# Dates have dash character compared to time that have colon
		if str.find(str(date), "-") > 0:
			results.add_data(date['datetime'])
	

main()