'''if target - value is in the given list and the if the index of the difference \
   is not the current index, then return the current index and index of the result\
    of difference'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, value in enumerate(nums):
            if target - value in nums and nums.index(target-value) != index:
                return [index, nums.index(target-value)]
        return None


'''Commonly found solution using dictionary'''
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
      result = {}
      for index, value in enumerate(nums):
          if target - value in result:
              return [index, result[target - value]]
          else:
              result[value] = index            
      return None