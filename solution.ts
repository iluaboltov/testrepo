class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}

function maxDepth(root: TreeNode | null): number {
    // Базовий випадок: якщо вузол порожній, повертаємо 0
    if (!root) {
        return 0;
    }
    
    // Рекурсивно обчислюємо глибину для лівого і правого піддерев
    const leftDepth = maxDepth(root.left);
    const rightDepth = maxDepth(root.right);
    
    // Повертаємо максимум з глибин + 1 (поточний рівень)
    return Math.max(leftDepth, rightDepth) + 1;
}
