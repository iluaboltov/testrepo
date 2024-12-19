from collections import deque

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        Find the maximum depth of a binary tree using an iterative approach (BFS).

        :param root: The root node of the binary tree.
        :return: The maximum depth of the binary tree.
        """
        if not root:
            return 0

        queue = deque([(root, 1)])  # Initialize a queue with the root node and its depth.
        max_depth = 0

        while queue:
            node, depth = queue.popleft()
            max_depth = max(max_depth, depth)  # Update the max depth if the current depth is greater.

            if node.left:
                queue.append((node.left, depth + 1))  # Add left child node and its depth to the queue.
            if node.right:
                queue.append((node.right, depth + 1))  # Add right child node and its depth to the queue.

        return max_depth