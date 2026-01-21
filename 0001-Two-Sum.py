class Solution:
  def(self,nums: List[int], target: int) ->List[int]:
    #dictionary to store seen numbers and their indices
    seen={}
    for i,num in enumerate(nums):
      #Calculate what we need to reach the target
      remaining= target-num
      if remaining in seen:
        #Found the pair, return indices
        return [seen[remaining],i]
      #store the current number and to the index
      seen[num]= i
