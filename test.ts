// Створюємо тестове дерево [3,9,20,null,null,15,7]
const root = new TreeNode(3);
root.left = new TreeNode(9);
root.right = new TreeNode(20);
root.right.left = new TreeNode(15);
root.right.right = new TreeNode(7);

// Перевіряємо різні випадки:
console.log(`Максимальна глибина: ${maxDepth(root)}`);          // Виведе: Максимальна глибина: 3
console.log(`Глибина для одного вузла: ${maxDepth(singleNode)}`); // Виведе: Глибина для одного вузла: 1
console.log(`Глибина порожнього дерева: ${maxDepth(null)}`);       // Виведе: Глибина порожнього дерева: 0