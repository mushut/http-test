import requests
#from html.parser import HTMLParser
from bs4 import BeautifulSoup

class Data():
	def __init__(self):
		self.data = []
		
	def add_data(self, data):
		self.data.append(data)
		
	def print_data(self):
		for i in self.data:
			print(i)

#class HTML_parser(HTMLParser):
#	def handle_starttag(self, tag, attrs):
#		#print("Encountered a start tag:", tag)
#		pass
#
#	def handle_endtag(self, tag):
#		#print("Encountered an end tag :", tag)
#		pass
#
#	def handle_data(self, data):
#		#print("Encountered some data  :", data)
#		
#		if self.get_starttag_text() == "<h1 class=\"hero_slide_name\">":
#			pass

def main():
	bar_loose_html = requests.get('https://barloose.com/')
	
	# Print data for testing
	# print(x.text)
	
	#results = Data()
	
	# parse html
	#parser = HTML_parser(results)
	
	feed = bar_loose_html.text
	
	soup = BeautifulSoup(feed, 'html.parser')
	

	
	# Testing parser
	#parser.feed(bar_loose_html.text)
	
	results = soup.find_all("div", "hero_slide_date")
	
	for result in results:
		print(result)
	
	# search for tag that marks the event data

main()