#we take in the array and sequence
def isValidSubsequence(array, sequence):
    #tracking our index by init it to 0
    seqIdx = 0
    #for each value in the array
    for value in array:
        # if our seqidx equals the len of sequence, then stop looping
        if seqIdx == len(sequence):
            break
        #if the sequence continues to match the value of the array, keep going
        if sequence[seqIdx] == value:
            seqIdx += 1
        # you can now return the the answer once its looped over all values
    return seqIdx == len(sequence)

print(isValidSubsequence([1,2,3,4], [2,4]))
print(isValidSubsequence([1,2,3,4], [4, 2]))