class Solution:
    def isValid(self, s: str) -> bool:
        
        q = collections.deque()
        dic = {'[':']',
              '{':'}',
              '(':')'}
        count = 0
        if len(s)%2:
            return False
        for i in s:
            
            
            if i == '(' or i=='[' or i == '{':
                count+=1
                q.append(dic[i])
            elif q:
                count-=1
                st = q.pop()
                if st != i:
                    return False
            else:
                count-=1
        if len(s) < 2 or len(q)!=0 or count!=0:
            return False
        return True
                    
        