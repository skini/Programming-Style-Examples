#Shloka Kini
#This is the module for the Advanced Assignment 
#this module scrapes the webpage and contains one method, 
#to put the webpage in a csv file

from beautysoup_adv import BS4Scrape
import unittest
import csv

class BS4Scrape:

  def setUp(self):
  	self.results = BS4Scrape()
  	
  def testLoad(self):
  	assert self.results.page != None
  	assert self.results.soup != None 

  def testParseRows(self):
  	self.results.parse_rows_csv()
  	assert open('advanced3.csv')!=None
  	with open('advanced3.csv', 'rb') as f:
  		reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
  		count = 0
  		for row in reader:
  			count = count + 1
  			if(count ==1):
  				assert row == ['State,Democratic Party(Obama\xc2\xa0/ Biden),Republican Party(Romney\xc2\xa0/ Ryan),Libertarian Party(Johnson\xc2\xa0/ Gray),Green Party(Stein\xc2\xa0/ Honkala*),\xc2\xa0 \xc2\xa0 \xc2\xa0 \xc2\xa0Others\xc2\xa0\xc2\xa0 \xc2\xa0 \xc2\xa0(all other listed partiesand candidates),\xc2\xa0 \xc2\xa0 \xc2\xa0Total Votes\xc2\xa0 \xc2\xa0 \xc2\xa0']
  			if(count == 52):
  				assert row == ['Totals,65446032,60589084,1273168,464510,781053,128556837']
  		assert count == 53
  			
  			
    
    

# if this file is run directly, run the tests
if __name__ == "__main__":
	unittest.main()