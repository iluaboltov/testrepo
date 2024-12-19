class Program {
    static void Main(string[] args) {
        // Create test tree [3,9,20,null,null,15,7]
        TreeNode root = new TreeNode(3) {
            left = new TreeNode(9),
            right = new TreeNode(20) {
                left = new TreeNode(15),
                right = new TreeNode(7)
            }
        };

        Solution solution = new Solution();
        int result = solution.MaxDepth(root);
        Console.WriteLine($"Maximum depth: {result}"); // Outputs: Maximum depth: 3
    }
}
