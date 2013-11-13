#Shloka Kini
#This is the module for the Intermediate Assignment
#It contains one function, which returns the list of Pop12 values and their corresponding 
#state names, in a tuple list

class Census:
  
  def __init__(self):
  	self.filename = 'NST_EST2012_ALLDATA.csv'
  	self.file = open(self.filename, 'r')
  	self.all_lines = self.file.readlines()

  def popestimate(self):
    all_vals = []
    for line in self.all_lines:
      columns = line.split(',')
      all_vals.append((columns[4],columns[9]))
    return all_vals
