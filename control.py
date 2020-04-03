from fileparser import FileParser
from editdis    import EditDis
import operator
import time
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
        reader = self.fpob.reader
        search = self.search
        path   = self.path
        append = self.res.append
        trgt   = self.trgt
        dist   = self.edob.dist
        lsta   = self.fpob.linesta
        getitem= operator.getitem
        for fil in os.listdir(path):
            if '.srt' in fil:
                reader(f'{path}/{fil}')
                for line in lsta:
                    dis = dist(trgt,line)
                    # t1 = time.time()
                    if dis < 10:
                        append((dis,line))
        self.res.sort(key = lambda x:x[0])

    def search(self):
        append = self.res.append
        trgt   = self.trgt
        dist   = self.edob.dist
        lsta   = self.fpob.linesta
        for line in lsta:
            append((dist(trgt,line),line))
        

