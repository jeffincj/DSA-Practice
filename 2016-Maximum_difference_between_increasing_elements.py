class Solution(object):
    def maximumDifference(self, nums):
        min_num=nums[0]
        max_diff=-1
        for num in nums:
            if num>min_num:
                max_diff=max(max_diff,num-min_num)
            else:
                min_num=num
        return max_diff
