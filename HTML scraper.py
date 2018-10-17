# import libraries
from bs4 import BeautifulSoup
import csv
from urllib.request import urlopen


def page_scrape(args):
	c = 0
	i = 0
	while c <= 200:
		
		str, = args[i]
		html = urlopen(str)
		soup = BeautifulSoup(html, 'html.parser')
		name_box = soup.find('h1', attrs={'id': 'event-heading'})
		details_box = soup.find('div', attrs={'class': 'text-format'}).find('p')
		date_box = soup.find('h1', attrs={'id': 'event-heading'})
		location_box = soup.find('h1', attrs={'id': 'event-heading'})
		eventname = name_box.text.strip()
		eventdetails = details_box.text.strip() 
		print (eventname)
		print (eventdetails)
		i = i +1
		c = c + 1


f = open("events.csv")
csv_f = list(csv.reader(f))
page_scrape(csv_f)
	

# 	# specify the url
# #quote_page = 'http://www.belfastcity.gov.uk/events/Event-97944.aspx'

# # query the website and return the html to the variable ‘page’
# #page = urllib3.urlopen(quote_page)

# # parse the html using beautiful soup and store in variable `soup`
# soup = BeautifulSoup(html, 'html.parser')

# # Take out the <div> of name and get its value
# name_box = soup.find('h1', attrs={'id': 'event-heading'})

# #Finding the value for time, date and location
# details_box = soup.find('div', attrs={'class': 'text-format'}).find('p')
# date_box = soup.find('h1', attrs={'id': 'event-heading'})
# location_box = soup.find('h1', attrs={'id': 'event-heading'})

# # strip() is used to remove starting and trailing

# eventname = name_box.text.strip()
# eventdetails = details_box.text.strip() 

# print (eventname)
# print (eventdetails)
