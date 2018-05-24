#import the libraries
import urllib2
import helpers
import math
from bs4 import BeautifulSoup

#specify the URL, this is the initial URL search page, and specify starting 'soup'
page_number = 1
starter_link = 'https://www.niche.com/k12/search/largest-school-districts/?page='
soup = BeautifulSoup(urllib2.urlopen(starter_link + str(page_number)),'html.parser')

#arrays to hold data
all_districts=[]

#grab max number of pages, see helper method below
max_number = helpers.maxPage(soup, 'value', 'select','pagination__pages__selector')

#while the current page is less than max number of pages....
#parsed is an array that holds all of the a fields with class 'search-result__link'
#then run for loop, so each district info link is extracted and re-encoded
#increase page number by one while still less than max page number
#reset soup to be the next page, redo loop
#ending with the all_districts array with niche links for all districts over all pages
while(page_number <= max_number):
	parsed = soup.find_all('a', class_='search-result__link')
	for district_info in parsed:
		all_districts.append(str(district_info.attrs['href'].encode("utf-8")))
		
	if page_number != max_number:
		page_number+=1
		newLink = starter_link+str(page_number)
		soup = BeautifulSoup(urllib2.urlopen(newLink),'html.parser')
	else:
		break

#create csv list

resultFile = open("districtNiche.csv",'w')
for r in all_districts:
	resultFile.write(r + "\n")
resultFile.close()