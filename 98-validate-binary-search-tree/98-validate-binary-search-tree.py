# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(self,root,moreThan=float('-inf'),lessThan=float('inf')):
            if not root:
                return True
            elif root.val >= lessThan or root.val <= moreThan:
                return False
            else:
                return isValid(self,root.left,moreThan,root.val) and isValid(self, root.right, root.val, lessThan)
            
        return isValid(self,root,float('-inf'),float('inf'))