import unittest
from solution_iterative import Solution

class TestSolutionIterative(unittest.TestCase):
    def test_max_depth(self):
        solution = Solution()

        # Test empty tree
        self.assertEqual(solution.maxDepth(None), 0)

        # Test single node tree
        single_node = TreeNode(1)
        self.assertEqual(solution.maxDepth(single_node), 1)

        # Test regular tree
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(solution.maxDepth(root), 3)

        # Test unbalanced tree
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        root.left.left.left.left = TreeNode(5)
        self.assertEqual(solution.maxDepth(root), 5)

if __name__ == '__main__':
    unittest.main()
