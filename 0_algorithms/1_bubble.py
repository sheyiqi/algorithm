def bubble(array):
    arraylen = len(array)
    while arraylen > 0:
        for i in range(arraylen-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        arraylen-=1
    return array

if __name__ == '__main__':
    array=[3,6,1,6,8,8,32,236,1,16,71,13,13]
    print (bubble(array))
