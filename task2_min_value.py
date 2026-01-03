class Node:
    """
    Вузол двійкового дерева пошуку.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_min(root: Node):
    """
    Функція знаходить найменше значення у BST.
    
    У двійковому дереві пошуку найменше значення
    завжди знаходиться у крайньому лівому вузлі.
    """
    if root is None:
        return None

    current = root
    while current.left is not None:
        current = current.left

    return current.value


#  ТЕСТ 
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(20)
    root.left.left = Node(2)
    root.left.right = Node(7)

    print("Найменше значення в дереві:", find_min(root))
