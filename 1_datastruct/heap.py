#heap
def downEle(aList,pos,aLen):
    left=2*pos
    right=2*pos+1
    exchange=pos
    if left < aLen and aList[exchange] < aList[left]:
        exchange=left
    if right < aLen and aList[exchange] < aList[right]:
        exchange = right
    if exchange != pos:
        aList[pos], aList[exchange] = aList[exchange], aList[pos]
        downEle(aList,exchange,aLen)


def buildHeap(aList):
    aLen=len(aList)
    for i in range(aLen/2,-1,-1):
        downEle(aList,i,aLen)


def sortHeap(aList):
    aLen=len(aList)
    for i in range(0,aLen):
        aList[0], aList[aLen-i-1] = aList[aLen-i-1], aList[0]
        downEle(aList, 0, aLen-i-1)


def upEle(aList,pos):
    parent=(pos-1)/2
    while pos >= 0 and aList[parent] < aList[pos]:
        aList[pos],aList[parent]=aList[parent],aList[pos]
        pos=parent
        parent=pos/2


def addEle(aList,ele):
    aList.append(ele)
    upEle(aList,len(aList)-1)

aList=[2,4,5,1,7,10,3,6,0,9]
print"rawlist:",aList

buildHeap(aList)
print"afterbuilt:",aList

addEle(aList,8)
print"addelement:",aList

sortHeap(aList)
print"aftersorted:",aList
