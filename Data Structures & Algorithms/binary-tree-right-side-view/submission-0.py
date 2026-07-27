# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.dictionary_values = defaultdict(list)
        
        def dfs(node , level):
            if node is None:
                return 

            self.dictionary_values[level].append(node.val)
            left = dfs(node.left , level + 1)
            right = dfs(node.right , level + 1)  

        dfs(root , 0)

        output_list = list(self.dictionary_values.values())

        print(output_list)
        return_list = []
        for val in output_list:
            return_list.append(val[-1])

        return return_list






