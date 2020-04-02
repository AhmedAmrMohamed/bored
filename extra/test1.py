# import docdis as ds
import editdis as ds


def main(inp):
    # x    = ds.DocDis()
    x    = ds.EditDis(1,1,1) 
    fil = open('gen.srt','r')
    li  = []
    for line in fil:
        # print(line)
        li.append((x.dist(line,inp),line))
    li.sort(key = lambda x:x[0])
    fil.close()
    return li

# li = main('when the lion is hungry')  # 0 , -18
# li = main('when the lion\'s hungry')  # 0 , -21
# li = main('he is a fox')  #fail their are two possible results
# li = main('ofcourse darling')  # 0 , -2
# li = main('silver')  # f
# li = main('the silverback')  # 0 , -2
li = main('silverback')  #f 30-50
print(li[0:20])
    

    

