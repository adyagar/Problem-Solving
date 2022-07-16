class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        tot_sum = sum(nums)
        run_sum = 0
        
        for i,j in enumerate(nums):
            if j + run_sum * 2 == tot_sum:
                return i
            else:
                run_sum  = run_sum +  j
        
        return -1
            