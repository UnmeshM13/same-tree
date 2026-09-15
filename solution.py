# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        r1 = []
        r2 = []
        def IOT1(node):
            if node is None:
                return
            IOT1(node.left)
            r1.append(node.val)
            IOT1(node.right)
        IOT1(p)
        def IOT2(node):
            if node is None:
                return
            IOT2(node.left)
            r1.append(node.val)
            IOT2(node.right)
        IOT2(q)
        return r1 == r2