from bs4 import BeautifulSoup
import re
import requests

# Parse event data from Bar Loose html
def loose_parser(feed, results):
	soup = BeautifulSoup(feed, "html.parser")
	
	event_date_tags = soup.find_all("time")
	event_dates = []
	
	for date in event_date_tags:
		# Dates have dash character compared to time that have colon
		if str.find(str(date), "-") > 0:
			result = Event()
			
			tmp = date["datetime"].split("-")
			
			day = int(tmp[2])
			month = int(tmp[1])
			
			result.add_date([day, month])
			results.append(result)
			
	# Get event data (div that has class "hero_slider_content"
	event_data = soup.find_all("div", {"class" : "hero_slider_content"})
	for event in event_data:
		# Event data has div field for event date
		date_raw1 = event.div
		
		# Test print contents
		#print(date_raw1.contents[0])
		
		info_tmp = event.h1
		
		info = info_tmp.contents[0]
		print(info)
		
		#date_raw2 = date_raw1.find('div', {"class" : "hero_slide_date"})
		#print(date_raw2)
		#date_raw3 = date_raw2.contents
		
		# First is day, second is month
		date = re.findall(r"\d+", date_raw1.contents[0])
		
		# TODO Save the date data to Data objects
		
		for result in results:
			day, month = result.get_date()
			print("day: " + str(day))
			print("month: " + str(month))
			if month == date[1] and day == date[0]:
				result.add_event(info)
				
	return results

# Parse event data from My Helsinki Open API
def helsinki_open_api():

def main():
	results_loose = []

	#bar_loose_html = requests.get("https://barloose.com/")
	#helsinki_json = requests.get("http://open-api.myhelsinki.fi/v1/events/")
	
	# Read data from already downloaded files
	bar_loose_html = open("loose_data.html", "r")
	helsinki_json = open("helsinki_data.json", "r")
	
	# Handle Bar Loose event data
	feed = bar_loose_html	#.text if using get request
	
	results_loose = loose_parser(feed, results_loose)

main()