# o(N) Time  | o(N) Space

def sortedSquaredArray(array):
    sortedArr = [0 for _ in array]
    endPtr  = len(array) -1
    startPtr = 0
    for idx in reversed(range(len(array))):
        if abs(array[startPtr]) > abs(array[endPtr]):
            sortedArr[idx] = array[startPtr]**2
            startPtr+=1
        else:
            sortedArr[idx] = array[endPtr]**2
            endPtr-=1
    return sortedArr
            

print(sortedSquaredArray([-7,-5,-4,3,6,8,9]))
