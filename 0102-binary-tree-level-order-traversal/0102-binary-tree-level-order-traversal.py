# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        if not root:
            return []
        
        ans = []
        
        queue = collections.deque()
        
        queue.append([root])
        
        while queue:
            t=[]
            a=[]
            node = queue.popleft()
            if len(node)>0:
                for i in node:
                    if i.left:
                        t.append(i.left)
                    if i.right:
                        t.append(i.right)

                    a.append(i.val)
                queue.append(t)
                    
            if a and a is not None:
                ans.append(a)
            
        return ans
                