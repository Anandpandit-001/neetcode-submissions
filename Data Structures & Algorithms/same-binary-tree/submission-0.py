# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.First_list = []
        self.Second_list = []

        def dfs(node , list_of_val):
            if node is None:
                list_of_val.append(node)
                return 

            list_of_val.append(node.val)
            left = dfs(node.left ,list_of_val )
            right = dfs(node.right , list_of_val)

        dfs(p , self.First_list )
        dfs(q , self.Second_list )

        if tuple(self.First_list) == tuple(self.Second_list):
            return True
        else:
            return False
            

        















