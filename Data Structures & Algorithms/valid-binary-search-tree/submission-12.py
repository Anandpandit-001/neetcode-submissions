# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.return_bool = True
        
        # Added nodes_above as a parameter to track ancestors and directions
        def dfs_v1(node, root_node, nodes_above):
            print("dfs_v1_enter")
            if node is None:
                return 

            # NEW FEATURE: Loop through all upper nodes
            for anc_val, direction in nodes_above:
                # If we are in the left subtree of an ancestor, we must be strictly lesser
                if direction == "left" and node.val >= anc_val:
                    self.return_bool = False
                # If we are in the right subtree of an ancestor, we must be strictly greater
                elif direction == "right" and node.val <= anc_val:
                    self.return_bool = False

            if node.left is None and node.right is None:
                print("dfs_v1_enter1")
                if node.val >= root_node.val:
                    self.return_bool =  False
            elif node.left is not None and node.right is None:
                print("dfs_v1_enter2")
                if node.left.val >= node.val and node.val <= root_node.val :
                    print("dfs_v1_enter3")
                    self.return_bool =  False
            elif node.right is not None and node.left is None:
                print("dfs_v1_enter4")
                if node.right.val <= node.val  and node.val <= root_node.val:
                    print("dfs_v1_enter5")
                    self.return_bool =  False
            elif node.right is not None and node.left is not None:
                print("dfs_v1_enter6")
                if node.val <= root_node.val:
                    if node.left.val >= node.val or node.right.val <= node.val:
                        print("dfs_v1_enter7")
                        self.return_bool =  False

            # Pass the current node and direction down to the next level
            left = dfs_v1(node.left, root_node, nodes_above + [(node.val, "left")])
            right = dfs_v1(node.right, root_node, nodes_above + [(node.val, "right")])

        def dfs_v2(node, root_node, nodes_above):
            print("dfs_v2_enter")
            if node is None:
                return 

            # NEW FEATURE: Loop through all upper nodes
            for anc_val, direction in nodes_above:
                if direction == "left" and node.val >= anc_val:
                    self.return_bool = False
                elif direction == "right" and node.val <= anc_val:
                    self.return_bool = False

            if node.left is None and node.right is None:
                print("dfs_v2_enter1")
                if node.val <= root_node.val:
                    self.return_bool =  False
            elif node.left is not None and node.right is None:
                print("dfs_v2_enter2")
                if node.left.val >= node.val and node.val >= root_node.val :
                    print("dfs_v2_enter3")
                    self.return_bool =  False
            elif node.right is not None and node.left is None:
                print("dfs_v2_enter4")
                if node.right.val <= node.val  and node.val >= root_node.val:
                    print("dfs_v2_enter5")
                    self.return_bool =  False
            elif node.right is not None and node.left is not None:
                print("dfs_v2_enter6")
                if node.val >= root_node.val:
                    if node.left.val >= node.val or node.right.val <= node.val:
                        print("dfs_v2_enter7")
                        self.return_bool =  False

            # Pass the current node and direction down to the next level
            left = dfs_v2(node.left, root_node, nodes_above + [(node.val, "left")])
            right = dfs_v2(node.right, root_node, nodes_above + [(node.val, "right")])

        def dfs_original(node, root_node, nodes_above):
            if node is None:
                return 

            # NEW FEATURE: Loop through all upper nodes (empty for root, but catches if you call it elsewhere)
            for anc_val, direction in nodes_above:
                if direction == "left" and node.val >= anc_val:
                    self.return_bool = False
                elif direction == "right" and node.val <= anc_val:
                    self.return_bool = False

            if node.left is None and node.right is None:
                print("enter1")
                pass
            elif node.left is not None and node.right is None:
                print("enter2")
                if node.left.val >= node.val:
                    print("enter3")
                    self.return_bool =  False
            elif node.right is not None and node.left is None:
                print("enter4")
                if node.right.val <= node.val:
                    print("enter5")
                    self.return_bool =  False
            elif node.right is not None and node.left is not None:
                print("enter6")
                
                if node.left.val >= node.val or node.right.val <= node.val:
                    print("enter7")
                    self.return_bool =  False

            # dfs_v1 for the left branch, dfs_v2 for the right branch
            left = dfs_v1(node.left, root_node, nodes_above + [(node.val, "left")])
            right = dfs_v2(node.right, root_node, nodes_above + [(node.val, "right")])

        # Start the traversal with an empty list of upper nodes
        dfs_original(root, root, [])
    
        return self.return_bool