class FileParser:
    def __init__(self,strfile):
        self.strfile = strfile
        self.enum    = {'ID':0, 'STA':1, 'SUB':2 }
        self.lineId  = {}
        self.idSTA   = {}

    def reader(self): 
        '''
        transverse the strfile one line at a time
        '''
        pass

    def classifyer(self,line):
        '''
        return the line category
        ID, STA , SUB
        '''
        pass

    def strip(self,line):
        ''' 
        remove all the unwanted chars from the line
        like: whitespaces, \\n, ...
        '''
        pass
  

   
