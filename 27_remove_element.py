class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        expected =[]
        a=0
        for n in range(len(nums)):
            if nums[n]!=val :
                nums[a]=nums[n]
                a=a+1
        return a
