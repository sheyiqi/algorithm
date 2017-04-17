def Heapify(a, start, alen):  
    left = start * 2 
    right = start * 2 + 1 
    maxv = start 
    if left < alen and a[maxv] < a[left]:
        maxv = left
    if right < alen and a[maxv] < a[right]:
        maxv = right
    if start != maxv:  
        a[maxv],a[start] = a[start],a[maxv]  
        Heapify(a, maxv, alen)
              
def BuildHeap(a):  
    size = len(a)  
    for i in range(size//2,-1,-1):
        Heapify(a, i, size)  

def HeapSort(a):  
    alen = len(a) 
    for i in range(0,alen):
        a[0],a[alen-1-i] = a[alen-i-1],a[0]  
        Heapify(a, 0, alen-i-1)  

a = [4,1,3,2,16,9,10,14,8,7]  
BuildHeap(a)
print 'after build', a
HeapSort(a)  
print 'after sorted', a
