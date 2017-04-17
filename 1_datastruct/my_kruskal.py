#Kruskal.py

from numpy import *

aa = 65535 
vexs = array([[0,10,aa,aa,aa,11,aa,aa,aa],
              [10,0,18,aa,aa,aa,16,aa,12],
              [aa,18,0,22,aa,aa,aa,aa,8],
              [aa,aa,22,0,20,aa,aa,16,21],
              [aa,aa,aa,20,0,26,aa,7,aa],
              [11,aa,aa,aa,26,0,17,aa,aa],
              [aa,16,aa,24,aa,17,0,19,aa],
              [aa,aa,aa,16,7,aa,19,0,aa],
              [aa,12,8,21,aa,aa,aa,aa,0]])

lengthVex = len(vexs)    
beginEdge = []
endEdge = []
weight = []
group = []
for i in arange(lengthVex):     
    group.append([i])
    for j in arange(i+1,lengthVex):
        if(vexs[i, j]>0 and vexs[i, j]<aa):
            beginEdge.append(i)   
            endEdge.append(j)      
            weight.append(vexs[i, j])
lengthEdge = len(weight)
sum = 0
for i in arange(lengthEdge):
    I = (argsort(weight))[0]
    for j in arange(lengthVex):
        if(beginEdge[I]) in group[j]:
            m = j
        if(endEdge[I]) in group[j]:
            n = j
    if m != n:
        group[m] = group[m] + group[n]
        group[n] = []
        sum = sum + weight[I]
        print(weight[I])
    del weight[I]
    del beginEdge[I]
    del endEdge[I]
print("The length of the minimum cost spanning tree is: ",sum)
