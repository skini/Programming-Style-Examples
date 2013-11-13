#Shloka Kini
#This is a test for the advanced question
#It imports the module that appropriately scrapes the 
#HTML from the website, and then puts the data into a csv file

from beautysoup_adv import BS4Scrape

soup = BS4Scrape()
soup.parse_rows_csv()