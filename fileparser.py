import re
class FileParser:
    def __init__(self):
        self.enum    = {'ID':0, 'STA':1, 'SUB':2 }
        self.linesta = {}
        # self.idSTA   = {}
        self.idmatch = re.compile('[\\d]+')
        self.stamatch= re.compile('-->')
        # self.reader()

    def reader(self,strfile): 
        '''
        transverse the strfile one line at a time
        '''
        subline   = []
        timestamp = None
        fil = open(strfile,'r')
        for line in fil:
            line = line.rstrip()
            gen = self.classify(line)
            # print(gen)
            if gen == self.enum['ID']:
                self.procline(int(line),subline,timestamp)
                subline = []
            elif gen == self.enum['STA']:
                timestamp = line
            else:
                subline.append(line)
        fil.close()

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

    def procline(self,iden,subline,timestamp):
        ''' 
        remove all the unwanted chars from the line
        like: whitespaces, \\n, ...
        '''
        line  = ' '.join(subline)
        self.linesta[line]  = timestamp
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
