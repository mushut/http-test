import requests
from html.parser import HTMLParser

class HTML_parser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print("Encountered a start tag:", tag)

	def handle_endtag(self, tag):
		print("Encountered an end tag :", tag)

	def handle_data(self, data):
		print("Encountered some data  :", data)

def main():
	bar_loose_html = requests.get('https://barloose.com/')
	
	# Print data for testing
	# print(x.text)
	
	# parse html
	parser = HTML_parser()
	
	# Testing parser
	parser.feed(bar_loose_html)
	
	# search for tag that marks the event data

main()