class EditDis:
    def __init__(self, change, remove, insert):
        self.change = change
        self.remove = remove
        self.insert = insert
    
    def proc(self,line):
        line = line.lower()
        line = line.split()
        line = ' '.join(line)
        return line

    def dist(self,firstLine,secondLine):
        firstLine,secondLine = self.proc(firstLine),self.proc(secondLine)
        firstlen,secondlen = len(firstLine),len(secondLine)
        def core(fidx, sidx):
            if fidx == firstlen:
                return self.insert * (secondlen - sidx)
            if sidx == secondlen:
                return self.remove * (firstlen  - fidx)

            if firstLine[fidx] == secondLine[sidx]:
                return core(fidx+1,sidx+1)

            add = core(fidx+1,sidx  ) + self.remove
            rem = core(fidx  ,sidx+1) + self.insert
            cha = core(fidx+1,sidx+1) + self.change
            return min(add,rem,cha)
        return core(0,0)


import sys
a = sys.argv[1:]
a = ' '.join(a)
a = a.split(',')
x = EditDis(1,2,2) 
print(a[0],a[1],x.dist(a[0],a[1]))
                

