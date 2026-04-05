# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def dfs(self, node, max_val:float):

        if node.val >= max_val:
            self.count += 1

        if node.left:
            self.dfs(node.left, max_val if max_val > node.val else node.val)
        if node.right:
            self.dfs(node.right, max_val if max_val > node.val else node.val)
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        if not root:
            return []
        self.dfs(root, float('-inf'))
        return self.count
        