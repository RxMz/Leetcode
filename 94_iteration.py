# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack  = []
        to_ret =[]
        cur_node = root
        while(cur_node !=None or stack):
            while(cur_node !=None):
                stack.append(cur_node)
                cur_node = cur_node.left
            cur_node = stack.pop()
            to_ret.append(cur_node.val)
            cur_node = cur_node.right
        return to_ret
        