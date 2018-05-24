	
#import the libraries
import urllib2
from bs4 import BeautifulSoup
import csv
#read in csv item
f = open("districtNiche.csv")
csv_f = csv.reader(f)

#setup array for data
city_webs=[]

#analyze each row
#district soup is the html for each website

for row in csv_f:
	
	district_soup = BeautifulSoup(urllib2.urlopen(row[0]), 'html.parser')
	# taking out specific tag for school district website
	
	
	for city_info in district_soup.find_all('a', class_='profile__website__link'):
	
		if city_info.has_attr('href'):
			city_webs.append(str(city_info.attrs['href'].encode("utf-8")))
			
f.close()

#create csv list
resultFile = open("districtWebsitesComplete.csv",'w')
for r in city_webs:
	resultFile.write(r+"\n")
resultFile.close()

