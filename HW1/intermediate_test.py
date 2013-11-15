#Shloka Kini
#This is my modified Test Module for Intermediate, with the added functions
#for obama and romney populations and comparisons

import unittest
from electiondatamod import ElectionResultsMod



class ElectionResultsModTest(unittest.TestCase):
  
  
  def setUp(self):
    self.results = ElectionResultsMod('election_results_test_file.csv')

  def testLoad(self):
  	assert self.results!=None
  	assert self.results.file!=None
  	assert self.results.all_lines!=None


  def testObamaPops(self):
  	pop = self.results.obama_pops()
  	assert pop[1] ==['Alaska', '91696', '41.6']
  

  def testRomneyPops(self):
  	pop = self.results.romney_pops()
  	assert pop[2] == ['Alabama', '1252453', '60.7\n']
  	
  def testStateCount(self):
  	state_count = self.results.state_count()
  	assert state_count==3
  	
  def testStates(self):
  	names = self.results.states()
  	assert len(names)==3
  	assert names[1]=='Alaska'
  	assert names[2]=='Alabama'
    

  def testObamaPercentage(self):
  	percentage = self.results.compare_obama_percentage()
  	assert percentage == ['Alabama', 16.5, '38.4']
  	

  def testRomneyPercentage(self):
  	percentage = self.results.compare_romney_percentage()
  	assert percentage == ['Alabama', 26.0, '60.7\n']
    
    

# if this file is run directly, run the tests
if __name__ == "__main__":
	unittest.main()