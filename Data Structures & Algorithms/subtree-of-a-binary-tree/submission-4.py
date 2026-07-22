# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.exist = []
        self.First_list = []
        self.Second_list = []

        def element_list(node , list_to_append):
            if node is None:
                list_to_append.append(node)
                return 

            list_to_append.append(node.val)
            element_list(node.left, list_to_append)
            element_list(node.right, list_to_append)
            

        def dfs(root , subroot):
            if root is None:
                return 0 

            
            if root.val == subroot.val :
                element_list(root , self.First_list)
            
                element_list(subroot , self.Second_list)
                if self.First_list == self.Second_list:
                    
                    self.exist.append(True)
                self.First_list = []
                self.Second_list = []
                        
            left = dfs(root.left , subroot)
            right = dfs(root.right , subroot)

    
            return max(left, right) + 1

        dfs(root , subRoot)
        for val in self.exist:
            if val == True:
                return True
        
        return False









