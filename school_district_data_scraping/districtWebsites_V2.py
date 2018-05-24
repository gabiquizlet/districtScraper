	
#import the libraries
import urllib2
from bs4 import BeautifulSoup
import csv
#read in csv item
f = open("districtNiche.csv")
csv_f = csv.reader(f)

#setup array for data
city_webs={}

#analyze each row
#district soup is the html for each website
i = 0
for row in csv_f: 
	print i
	if i ==900:
		break
	district_soup = BeautifulSoup(urllib2.urlopen(row[0]), 'html.parser')
	# taking out specific tag for school district website
	
	
	citywebsite = district_soup.find('a', class_='profile__website__link')
	if citywebsite is not None:
		if citywebsite.has_attr('href'):
			city_webs[str(citywebsite.attrs['href'].encode("utf-8"))] = district_soup.find('a', class_='entity-name__link').text
			i += 1
      
	
f.close()

#create csv list

with open('my_file.csv', 'w') as resultFile:
    [resultFile.write('{0},{1}\n'.format(value, key)) for key, value in city_webs.items()]


