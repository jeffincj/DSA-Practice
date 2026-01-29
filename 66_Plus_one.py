class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=0
        for i in range(len(digits)):   #changing the numbers into a single integer
            a=(10*a)+digits[i]
        a+=1                           #plus one
        digits= list(map(int,str(a)))  #changing integer into list
        return digits
