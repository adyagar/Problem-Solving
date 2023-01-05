class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        mapp = {}
        
        for ele in nums:
            if ele in mapp:
                return True
            else:
                mapp[ele]=1
        
        return False