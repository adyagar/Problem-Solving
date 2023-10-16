class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def feasible(n):
            d = 0
            total = 0
            for i in nums:
                total += i
                if total > n:
                    total = i
                    d += 1
                    if d >= k:
                        return False
            return True
        
        
        l=max(nums)
        r=sum(nums)        
        
        while l < r:
            mid = l + (r-l)//2
            print(mid)
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
                
        return l