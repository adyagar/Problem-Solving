class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a=[]
        count = 0
       
        for i,j in enumerate(nums):
            if i<1:
                a.append(nums[0])
            else:
                a.append(a[i-1]+j)
        return a
                