# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Recursive Solution
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0 
        
        self.max_depth = 0       
        self.iterateTree(root, 0)        
        return self.max_depth
    
    def iterateTree(self, root, depth):
        
        if root.val or root.val == 0:
            depth += 1
            if self.max_depth < depth:
                self.max_depth = depth
                
            if root.left or root.left == 0:
                self.iterateTree(root.left, depth)
            
            if root.right or root.right == 0:
                self.iterateTree(root.right, depth)
                
        return True
         
         
         
       
# Solution using Queue ( BFS )
# class Solution:     
#     def maxDepth(self, root: TreeNode) -> int:

#         depth = 0
#         level = [root] if root else []
        
#         while level:
            
#             depth += 1
#             queue = []
            
#             for children in level:
                
#                 if children.left or children.left == 0:
#                     queue.append(children.left)
                    
#                 if children.right or children.right == 0:
#                     queue.append(children.right)
      
#             level = queue
                
#         return depth





# Solution using List ( BFS ) ( shorthand )
# class Solution:     
#     def maxDepth(self, root: TreeNode) -> int:

#         depth = 0
#         level = [root] if root else []
        
#         while level:
#             depth += 1
#             level = [child for node in level for child in (node.left, node.right) if child]
                
#       return depth
            

        
        
