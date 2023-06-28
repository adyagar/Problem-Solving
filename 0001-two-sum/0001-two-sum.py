class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        sums = {}
        
        for i,j in enumerate(nums):
            if target - j in sums:
                
                return [sums[target-j],i]
            else:
                sums[j] = i