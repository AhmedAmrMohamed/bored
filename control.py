from fileparser import FileParser
from editdis    import EditDis
from heap       import Heap
from cache      import Cache
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
        self.caob = Cache()
        self.res  = Heap(max = False)
        self.walker()

    def walker(self):
        reader = self.fpob.reader
        search = self.search
        path   = self.path
        append = self.res.insert
        trgt   = self.trgt
        dist   = self.edob.dist
        mdeg   = self.matchdegree
        for dire,igno,files in os.walk(path):
            for fil in files:
                if '.srt' in fil:
                    fill = f'{dire}/{fil}'
                    lsta = self.caob.get(fill)
                    if not lsta:
                        lsta = reader(fill)
                        self.caob.put(fill,lsta)
                    for line in lsta:
                        dis = dist(trgt,line)
                        if dis < mdeg:
                            append((dis,line,lsta[line],fill))
        self.caob.dump()

    def search(self):
        append = self.res.append
        trgt   = self.trgt
        dist   = self.edob.dist
        lsta   = self.fpob.linesta
        for line in lsta:
            append((dist(trgt,line),line))
        

