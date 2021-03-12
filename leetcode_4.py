'''Unpack the given lists to a new list, find the length of the new list, divide the length by 2,\
if it's not divisible then the value in quotient's index is the result, else find the average of \
the value in quotient's index and of the value in quotient's index -1'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedArray = sorted([*nums1, *nums2])
        length = len(mergedArray)
        if length%2 != 0:
            return mergedArray[length//2]
        return (mergedArray[length//2-1]+mergedArray[length//2])/2