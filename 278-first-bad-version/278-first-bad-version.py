# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        s = 0
        e=n-1
        
        while s != e:
            m = (s+e)//2
            if isBadVersion(m+1):
                e = m 
            else:
                s = m +1
        if isBadVersion(s+1):
            return s+1
        else:
            return s +2
        
                
            
            