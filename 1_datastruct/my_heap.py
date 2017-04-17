def heapBuild(data):
    dataLen = len(data)
    for flag in range(dataLen//2,-1,-1):
        heapAdjust(data,flag,dataLen)

def heapAdjust(data,flag,dataLen):
    left = 2*flag
    right = 2*flag+1
    index = flag
    if left < dataLen and data[left] > data[index]:
        index = left
    if right < dataLen and data[right] > data[index]:
        index = right
    if flag != index:
        data[flag],data[index] = data[index],data[flag]
        flag=index
        heapAdjust(data,flag,dataLen)

def heapSort(data):
    dataLen = len(data)
    for i in range(dataLen-1,-1,-1):
        data[0],data[i]=data[i],data[0]
        heapAdjust(data,0,i)

data=[1,3,5,8,10,2,9,7,6,4]
print data
heapBuild(data)
print data
heapSort(data)
print data
