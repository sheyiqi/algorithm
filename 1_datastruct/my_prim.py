import numpy as np
aa = 99 
vexs = np.array([[ 0,10,aa,aa,aa,11,aa,aa,aa],
                 [10, 0,18,aa,aa,aa,16,aa,12],
                 [aa,aa, 0,22,aa,aa,aa,aa, 8],
                 [aa,aa,22, 0,20,aa,aa,16,21],
                 [aa,aa,aa,20, 0,26,aa, 7,aa],
                 [11,aa,aa,aa,26, 0,17,aa,aa],
                 [aa,16,aa,aa,aa,17, 0,19,aa],
                 [aa,aa,aa,16, 7,aa,19, 0,aa],
                 [aa,12,8,21,aa,aa,aa,aa, 0]])

line = vexs[0,:]
line[0]=0
weight = np.zeros(len(vexs))
weight[0]=1
i=0
while (i<9):
    print (line)
    index = (np.argsort(line))[i]
    weight[index]=line[index]
    print (index)
    line[index]=0
    line = np.array(list(map(lambda x,y : x if x<y else y,line,vexs[index,:])))
    i+=1
print (weight)
print (sum(weight))
