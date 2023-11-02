# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0,0,0)
            left, right = dfs(node.left), dfs(node.right)
            subtree_sum = left[0]+right[0]+node.val
            nodes_in_subtree = left[1]+right[1]+1
            nodes_eq_to_avg = left[2]+right[2]+(subtree_sum//nodes_in_subtree == node.val)
            return (subtree_sum, nodes_in_subtree, nodes_eq_to_avg)
        return dfs(root)[2]