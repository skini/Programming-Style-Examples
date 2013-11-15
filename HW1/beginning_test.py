#TEST 
#Print out all the state names from the csv
#Showing the "functional" style
#Shloka Kini
#Modified Code
#11/14/13

import unittest

f = open('election_results_test_file.csv', 'r')
print "Opened file:"

all_lines = f.readlines()

obama = [line.split(",")[3] for line in all_lines]
obama.pop(0)

romney = [line.split(",")[5] for line in all_lines]
romney.pop(0)

obama_total = 0
for o in obama:
  obama_total = obama_total + int(o)
  
  
romney_total =0
for r in romney:
  romney_total = romney_total + int(r)

#print "done ("+str(len(all_lines))+" lines)"

assert obama_total == 885316

assert romney_total == 1373687


if __name__ == "__main__":
	unittest.main()
