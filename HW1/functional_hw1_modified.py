# Print out all the state names from the csv# Showing the "functional" style#Shloka Kini#Modified Code#10/11/13f = open('2012_US_election_state.csv', 'r')print "Opened file:"all_lines = f.readlines()obama = [line.split(",")[3] for line in all_lines]obama.pop(0)romney = [line.split(",")[5] for line in all_lines]romney.pop(0)obama_total = 0for o in obama:  obama_total = obama_total + int(o)    romney_total =0for r in romney:  romney_total = romney_total + int(r)#print "done ("+str(len(all_lines))+" lines)"print "Obama total: " + str(obama_total)+ " votes"print "Romney total: " + str(romney_total)+ " votes"