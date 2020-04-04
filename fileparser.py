import re
class FileParser:
    def __init__(self):
        self.enum    = {'ID':0, 'STA':1, 'SUB':2 }
        # self.linesta = {}
        self.idmatch = re.compile('[\\d]+')
        self.stamatch= re.compile('-->')

    def reader(self,strfile): 
        '''
        transverse the strfile one line at a time
        '''
        # self.linesta.clear()
        linesta   = {}
        subline   = []
        timestamp = None
        classify  = self.classify
        enum      = self.enum
        procline  = self.procline
        fil = open(strfile,'r')
        for line in fil:
            line = line.rstrip()
            gen  = classify(line)
            if gen == enum['ID']:
                procline(int(line),subline,timestamp,linesta)
                subline = []
            elif gen == enum['STA']:
                timestamp = line
            else:
                subline.append(line)
        fil.close()
        return linesta

    def classify(self,line):
        '''
        return the line category
        ID, STA , SUB
        '''
        if self.idmatch.fullmatch(line):
            return self.enum['ID']
        if self.stamatch.search(line):
            return self.enum['STA']
        return self.enum['SUB']

    def procline(self,iden,subline,timestamp,linesta):
        ''' 
        remove all the unwanted chars from the line
        like: whitespaces, \\n, ...
        '''
        line  = ' '.join(subline)
        linesta[line]  = timestamp
        # self.idSTA[iden]   = timestamp


# x = FileParser('extra/gen.srt')
# x.reader()
# print(x.classify('1'))
# print(x.classify('9231'))
# print(x.classify('09213asd'))
# print(x.classify('1848'))
# print(x.classify('01:36:34,420 --> 01:36:38,390'))
# print(x.classify('it is very much your business,'))
# print(x.classify('and certainly your concern'))
