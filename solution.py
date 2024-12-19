class Solution(object):
    def maxDepth(self, root):
        # Base case: if root is None, return 0
        if not root:
            return 0
        
        # Recursively calculate the depth of left and right subtrees
        # and return the maximum plus 1 (for the current node)
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
# Test case
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.maxDepth(root))  # Should output: 3