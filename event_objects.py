# Class for handling data
# Setting event data
# Reading event data
class Event():
	def __init__(self):
		# Date of the event
		self.date = []
		# Information about the event
		self.event_data = "No data"
		
	def add_date(self, date):
		self.date = date
		
	def add_event(self, event_data):
		self.event_data = event_data
		
	def get_date(self):
		return self.date
		
	def get_event_data(self):
		return self.event_data
		
	def print_data(self):
		for i in self.date:
			print(i)
			
# Class for handling whole data read by program
# TODO: search for event
class Data():
	def __init__(self):
		self.data = []
		
	def add_event(self, event):
		self.data.append(event)
		
	# send data to database