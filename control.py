from fileparser import FileParser
from editdis    import EditDis
from heap       import Heap
import operator
import time
import os
class Control:
    def __init__(self,trgt,path=None,matchdegree = 10,change = 1,remove =1 , insert = 1):
        if not path:
            path = os.getcwd()
        print(path)
        self.matchdegree = matchdegree
        self.trgt = trgt
        self.path = path
        self.fpob = FileParser()
        self.edob = EditDis(change,remove,insert)
        self.res  = Heap(max = False)
        self.walker()

    def walker(self):
        reader = self.fpob.reader
        search = self.search
        path   = self.path
        append = self.res.insert
        trgt   = self.trgt
        dist   = self.edob.dist
        lsta   = self.fpob.linesta
        mdeg   = self.matchdegree
        for dire,igno,files in os.walk(path):
            for fil in files:
        # for fil in os.listdir(path):
                if '.srt' in fil:
                    # print(f'{dire}/{fil}')
                    reader(f'{dire}/{fil}')
                    for line in lsta:
                        dis = dist(trgt,line)
                        if dis < mdeg:
                            append((dis,line))

    def search(self):
        append = self.res.append
        trgt   = self.trgt
        dist   = self.edob.dist
        lsta   = self.fpob.linesta
        for line in lsta:
            append((dist(trgt,line),line))
        

