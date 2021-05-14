# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def travel(root):
            if not root:
                return [0,0]
            
            left=travel(root.left)
            right=travel(root.right)
            sel=root.val+left[1]+right[1]
            nsel=max(left)+max(right)
            
            return [sel,nsel]
        return max(travel(root))
