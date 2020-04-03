import os
import control
def main():
    target = input("the phrase : ")
    print('Enter the subs folder or press Enter\nTo use the current directory:\n\
    {}'.format(os.getcwd()))
    path = input()
    if len(path) == 0:
        path = None
    else:
        if path[0] == '~':
            path = os.path.expanduser(path)
        if not os.path.isdir(path):
            print('directory not found')
            quit
    print('please hold ...')
    res =  control.Control(target,path)
    mat = min(5,len(res.res))
    print(f'here are the top {mat} matches')
    while mat:
        mat-=1
        print(res.res.pop())

main()
