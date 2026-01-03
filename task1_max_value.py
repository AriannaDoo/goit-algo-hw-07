class Node:
    """
    Вузол двійкового дерева пошук
    Кожен вузол містить значення та посилання на лівого і правого нащадка.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_max(root: Node):
    """
    Функція знаходить найбільше значення у BST.
    
    У двійковому дереві пошуку найбільше значення
    завжди знаходиться у крайньому правому вузлі.
    """
    if root is None:
        return None

    current = root
    while current.right is not None:
        current = current.right

    return current.value


# ТЕСТ 
if __name__ == "__main__":
    # Створюємо приклад дерева
    root = Node(10)
    root.left = Node(5)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(25)

    print("Найбільше значення в дереві:", find_max(root))
