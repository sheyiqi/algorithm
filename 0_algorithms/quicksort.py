#yiqi.she

def part_sort(array, low, high):
    flag=array[low]
    while (low < high):
        while(low < high and array[high] < flag):
            array[low] = array[high]
            low+=1
            array[high] = array[low]
        while(low < high and array[high] >= flag):
            high-=1
        array[low]=flag
    return low

def quick_sort(array, low, high):
    if low < high:
        index = part_sort(array, low, high)
        quick_sort(array, low, index)
        quick_sort(array, index+1, high)

array=[8,14,25,66,1,7,2,24,9,56,3,10,23,56,56,56,42]
print (array)
quick_sort(array,0,len(array)-1)
print (array)
