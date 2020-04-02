from fileparser import FileParser
from editdis    import EditDis
import os
class Control:
    def __init__(self,trgt,path=None):
        if not path:
            path = os.getcwd()
        print(path)
        self.trgt = trgt
        self.path = path
        self.fpob = FileParser()
        self.edob = EditDis(1,1,1)
        self.res  = []
        self.walker()

    def walker(self):
        for fil in os.listdir(self.path):
            if '.srt' in fil:
                print(fil)
                self.fpob.reader(self.path+'/'+fil)
                self.search()
        self.res.sort(key = lambda x:x[0])

    def search(self):
        for line in self.fpob.linesta:
            self.res.append((self.edob.dist(self.trgt,line),line))
        

