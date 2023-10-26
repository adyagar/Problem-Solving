# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = collections.deque([[root]])
        result = []
        while queue:            
            level = queue.popleft()
            vals = []
            nextlvl = []
            for node in level:
                if node:
                    vals.append(node.val)  
                    nextlvl.append(node.left)
                    nextlvl.append(node.right)

            if vals:
                result.append(vals)
            if nextlvl:
                queue.append(nextlvl)
            
            
        return result