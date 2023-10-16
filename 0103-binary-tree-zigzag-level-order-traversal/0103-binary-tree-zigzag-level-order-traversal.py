# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        q = collections.deque([root])
        res = []
        flag=0
        while q:
            cr,n=[],len(q)
            flag+=1
            for i in range(n):
                node = q.popleft()
                cr.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if flag%2==0:
                res.append(cr[::-1])
            else:
                res.append(cr)
                
        return res