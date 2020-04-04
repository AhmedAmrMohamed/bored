import os
import pickle
class Cache:
    def __init__(self):
        self.cache = {}      #cache['filenodenumber'] = {(lastmodified, lsta)}
        try:
            self.load()
        except Exception:
            print('cache file not found')
    
    def get(self,file):
        ''' 
        return None if file can't be loaded from
        cache, otherwise
        return cached values
        '''
        ino,mtime =  self.getstats(file)
        cached    =  self.cache.get(ino,None)
        # print(file,end = '')
        if not cached  or cached[0] != mtime:
            # print('not found')
            return False
        # print('found')
        return cached[1]
    
    def getstats(self,filepath):
        ''' return filenodenumber, lastmodifyingtime '''
        st = os.stat(filepath)
        return st.st_ino, st.st_mtime
        

    def put(self,file,val):
        ''' put into cache'''
        ino,mtime = self.getstats(file)
        self.cache[ino] = (mtime,val)
        return val

    def mange(self,file):
        status = os.stat(file)
        status = status.st_ino, status.st_mtime
        return self.get(status)


    def load(self):
        ''' load the cache from file '''
        f = open('cache.bn','rb')
        self.cache = pickle.load(f)
        f.close()
    
    def dump(self):
        ''' write the cache to a file '''
        f = open('cache.bn','wb')
        pickle.dump(self.cache,f)
        f.close()

# import time
# a,b = x.getstats('extra/gen.srt')
# x.put(a,b,'smt')
# print(time.time())
# print(x.getstats('cache.py'))

