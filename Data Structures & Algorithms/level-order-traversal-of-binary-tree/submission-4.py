# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def treeTraversal(self, node: Optional[TreeNode], nodes: List, level:int):
        
        if node:
            if level <= len(nodes)-1:
                nodes[level].append(node.val)
            else:
                nodes.append([node.val])
            self.treeTraversal(node.left, nodes, level+1)
            self.treeTraversal(node.right, nodes, level+1)
        else:
            return

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = [0]
        if root:
            nodes[0] = [root.val]
        else:
            return []
        
        self.treeTraversal(root.left, nodes, 1)
        self.treeTraversal(root.right, nodes, 1)

        return nodes