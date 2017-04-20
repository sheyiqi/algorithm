#sheyiqi

def merge(l1, l2):
    # algorithm complexity 
    l=[]
    while len(l1)>0 and len(l2)>0:
        if l1[0] < l2[0]:
            l.append(l1[0])
            del l1[0]
        else:
            l.append(l2[0])
            del l2[0]
    l.extend(l1)
    l.extend(l2)
    return l
l1 = [1,3,5,7,9]
l2 = [0,2,4,6,8]
l=merge(l1,l2)
print (l)

