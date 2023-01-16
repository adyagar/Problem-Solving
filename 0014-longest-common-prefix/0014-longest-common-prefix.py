class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        pre = ""
        ex=0
        for i in range(len(strs[0])):
            if ex ==1 :
                break
            pre = strs[0][:i+1]
            for j in range(1,len(strs)):
                if not strs[j].startswith(pre):
                    ex = 1
                    return strs[0][:i]
                    break
        
        if pre:
            return pre
        else:
            return ""
                
