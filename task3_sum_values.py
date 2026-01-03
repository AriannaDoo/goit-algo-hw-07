class Node:
    """
    Вузол двійкового дерева пошуку.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def sum_tree(root: Node):
    """
    Функція знаходить суму всіх значень у дереві.
    
    Використовується рекурсивний обхід дерева.
    сума = значення вузла + сума лівого піддерева + сума правого піддерева
    """
    if root is None:
        return 0

    return root.value + sum_tree(root.left) + sum_tree(root.right)


#  ТЕСТ 
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(20)
    root.left.left = Node(3)
    root.left.right = Node(7)

    print("Сума всіх значень у дереві:", sum_tree(root))
