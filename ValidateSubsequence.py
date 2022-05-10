# o(N) Time | o(1) Space
# def validateSeqeunce(array, sequence):
#     seqIdx = 0
#     arrayIdx = 0
#     while  arrayIdx < len(array) and seqIdx < len(sequence):
#         if array[arrayIdx] == sequence[seqIdx]:
#             seqIdx+=1
#         arrayIdx+=1
#     return seqIdx == len(sequence)


# o(N) Time | o(1) Space
def validateSeqeunce(array, sequence):
    seqIdx = 0
    for values in array:
        
        if seqIdx==len(sequence):
            break
        if values == sequence[seqIdx]:
            seqIdx+=1
        print(seqIdx)
    return seqIdx==len(sequence)
            
print(validateSeqeunce([1,4,-5,22,11,9], [-5,9]))
