class DocDis:
    def buildVector(self,line):
        vic = {}
        for word in line.split():
            word = word.lower()
            vic[word] = vic.get(word,0)+1
        return vic
    
    def dotproduct(self,fv,sv):
        val = 0
        for word in fv:
            val += fv[word]*sv.get(word,0)
        return val

    def absolute(self,fv):
        val = 0
        for word in fv:
            val+= fv[word]**2
        return val**0.5
    
    def dist(self,firstLine,secondLine):
        fv  = self.buildVector(firstLine)
        sv  = self.buildVector(secondLine)
        pr  = self.dotproduct(fv,sv)
        ab  = self.absolute(fv)*self.absolute(sv)
        return pr/ab
import sys
a = sys.argv[1:]
a = ' '.join(a)
a = a.split(',')
x = DocDis() 
print(a[0],a[1],x.dist(a[0],a[1]))
