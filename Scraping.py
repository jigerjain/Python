# Web Scraping
# Aim is to list down top 250 movies from IMDB site
# Courtesy: www.eureka.co

from bs4 import BeautifulSoup

import requests
import sys

url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')

# print(response.text)
# print(soup)

tr = soup.findChildren("tr")
tr = iter(tr)

next(tr)


for movie in tr:
	#print(movie)
	check = movie.find('td',{'class':'titleColumn'})
	if(check != None):
		#print(movie)
		title = check.find('a').contents[0]
		#print(title)
		year = check.find('span',{'class':'secondaryInfo'}).contents[0]
		#print(year)
		rating = movie.find('td',{'class':'ratingColumn imdbRating'}).find('strong').contents[0]
		row = title + '-' + year + '-' + rating
		print(row)
