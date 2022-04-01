class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        
        a=set(list(range(1,n+1)))
        return list(a-set(nums))
                
            