# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p != None and q != None:
            if self.helper(p.left, q.left) == False:
                return False
            
            if p.val != q.val:
                return False
            
            if self.helper(p.right, q.right) == False:
                return False
        
        if p == None and q != None:
            return False
        if p != None and q == None:
            return False
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if self.helper(p, q) == False:
            return False
        
        return True
