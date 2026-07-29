# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.List_values = []

        def dfs(node):
            if node is None:
                return 

            left = dfs(node.left)
            self.List_values.append(node.val)
            right = dfs(node.right)

        dfs(root)
        print(self.List_values)

        return self.List_values[k-1]











