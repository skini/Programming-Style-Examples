#Shloka Kini
#This is my modified module for Intermediate, with the added functions
#for obama and romney populations and comparisons


class ElectionResultsMod:
  
  
  def __init__(self, filename):
    self.filename = filename
    self.file = open(self.filename, 'r')
    self.all_lines = self.file.readlines()

  def states(self):
    all_names = []
    for line in self.all_lines:
      columns = line.split(',')
      all_names.append(columns[1])
    return all_names

  #Function returns a list of lists for obama vote for each state
  # values in single list [state name, vote count, vote %]
  def obama_pops(self):
    all_names = []
    for line in self.all_lines:
      columns = line.split(',')
      all_names.append([columns[1], columns[3], columns[4]])
    return all_names
  
  #Function returns a list of lists for romney vote for each state
  # values in single list [state name, vote count, vote %]
  def romney_pops(self):
    all_names = []
    for line in self.all_lines:
      columns = line.split(',')
      all_names.append([columns[1], columns[5], columns[6]])
    return all_names
  
  def state_count(self):
    return len(self.all_lines)
    
   #Uses second CSV and compares percentages for Obama
   #prints out each percentage, name of state, and comparison 
  def compare_obama_percentage(self):
    from census import Census #Imports my other module
    census = Census()
    obama = self.obama_pops()
    pop_list = census.popestimate()
    print 'Obama'
    for o in obama:
      for p in pop_list:
        if(o[0] == p[0]):
          x = round((int(o[1])/float(p[1]))*100, 1)
          print o[0]
          print x
          print o[2]
          print x== o[2]
    print '***********'
          
          
    #Uses second CSV and compares percentages for Romney
   #prints out each percentage, name of state, and comparison        
  def compare_romney_percentage(self):
    print 'Romney'
    from census import Census
    census = Census()
    romney = self.romney_pops()
    pop_list = census.popestimate()
    for r in romney:
      for p in pop_list:
        if(r[0] == p[0]):
          x = round((int(r[1])/float(p[1]))*100, 1)
          print r[0]
          print x
          print r[2]
          print x== r[2]
    print '*************'