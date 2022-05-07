# o(n^2) Time | o(1) Space

# def target(list, target):
#     for i in range(len(list)-1):
#         for j in range(i+1, len(list)):
#             if list[i] + list[j] ==target:
#                 return [list[i],list[j]]
#     return [].


# o(n) Time | o(n) Space

# def target(list, target):

#     hashset={}
#     for i in range(len(list)):
#         if target - list[i] in hashset:
#             return [target-list[i],list[i],]
#         else:
#             hashset[list[i]]=True
#     return []

# o(nlogn) Time | o(1) Space   

def target(list,target):
    list.sort()
    left=0
    right=len(list)-1
    while left<right:
        if list[left]+list[right] == target:
            return [list[left],list[right]]
        elif list[left]+ list[right]< target:
            left+=1
        elif list[left]+ list[right] > target:
            right-=1
    return []
            
print(target([-4,-1,1,3,5,6,8,11],19))
