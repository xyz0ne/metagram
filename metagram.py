import pickle

class Index:
    def __init__(self):
        self.unitdata = []
        self.metadata = []
    def add_unit(self,unit):
        self.unitdata.append(unit)
    def add_holon(self,holon):
        self.holondata.appen(holon)
    def importfile(self,filepath):
        filedata = open(filepath+'.txt','r')
        for line in filedata:
            print line
    def save(self):
        savefile = open('metagramDATA','w')
        for n in range(6):
            savefile.write(str(n)+'\n')
        savefile.close()
    def load(self):
        pass
    
class Unit:
    def __init__(self,a,b):
        self.gram = [a,b]
        
class Holon:
    def __init__(self,a,b):
        self.gram = []
    def add(self,unit):
        self.gram.append([bt,unit])

INDEX = Index()
INDEX.save()




        
