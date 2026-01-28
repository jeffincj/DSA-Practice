class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n= (len(nums)-1)
        for i in range(len(nums)):
            if target == nums[i]:
                return i
        for j in range(n):
            if nums[j]<target and nums[j+1]>target:
                return j+1
        if nums[n]<target:
            return n+1
        if nums[0]>target:
            return 0
