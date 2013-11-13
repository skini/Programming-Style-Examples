#Shloka Kini
#This is a test for the Intermediate Question. 
#It imports the module and runs the two functions that compare percentages

from electiondatamod import ElectionResultsMod

filename = '2012_US_election_state.csv'
results = ElectionResultsMod(filename)

results.compare_obama_percentage()
results.compare_romney_percentage()
