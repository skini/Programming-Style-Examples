#Shloka Kini
#This is the module for the Advanced Assignment 
#this module scrapes the webpage and contains one method, 
#to put the webpage in a csv file

from bs4 import BeautifulSoup
import urllib2
import csv

class BS4Scrape:
  def __init__(self):
  	self.page = urllib2.urlopen('http://www.archives.gov/federal-register/electoral-college/2012/popular-vote.html').read()
  	self.soup = BeautifulSoup(self.page)

  def parse_rows_csv(self):
    table = self.soup.find(lambda tag: tag.name=='table')
    rows = table.table.findAll(lambda tag: tag.name=='tr')
    with open('advanced3.csv', 'wb') as csvfile:
    	csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    	for r in rows:
    		vals = r.findAll(lambda tag: tag.name=='td' or tag.name=='th')
    		if(len(vals) != 0):
    		  array = []
    		  for v in vals:
    		    array.append(v.get_text().encode('utf-8'))
    		  csvwriter.writerow(array)
    #print rows