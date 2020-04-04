import os
import json
import control
def main():
    conf = getConf()
    ch = conf['change']
    ad = conf['insert']
    re = conf['remove']
    ma = conf['acceptableMatchDgree']
    topres = conf['topres']
    target = input("the phrase : ")
    print('Enter the subs folder or press Enter\nTo use the current directory:\n\
    {}'.format(os.getcwd()))
    path = input('Path/Entre : ')
    if len(path) == 0:
        path = None
    else:
        if path[0] == '~':
            path = os.path.expanduser(path)
        if not os.path.isdir(path):
            print('directory not found')
            quit
    print('please hold ...')
    res =  control.Control(target,path,change = ch,remove = re,insert=ad,matchdegree = ma)
    mat = min(topres,len(res.res))
    print(f'here are the top {mat} matches')
    while mat:
        mat-=1
        print(res.res.pop())

def getConf():
    with open('conf.txt','r') as f:
        r = f.read()
        return json.loads(r)

main()
