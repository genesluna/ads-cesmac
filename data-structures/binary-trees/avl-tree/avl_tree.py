class AVLTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            self.height = 1

    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self.__insert(self.root, value)

    def __insert(self, node, value):
        if node is None:
            return self.Node(value)
        elif value < node.value:
            node.left = self.__insert(node.left, value)
        else:
            node.right = self.__insert(node.right, value)

        node.height = 1 + max(self.__get_height(node.left), self.__get_height(node.right))

        balance_factor = self.__get_balance_factor(node)

        if balance_factor > 1 and value < node.left.value:
            return self.__rotate_right(node)

        if balance_factor < -1 and value > node.right.value:
            return self.__rotate_left(node)

        if balance_factor > 1 and value > node.left.value:
            node.left = self.__rotate_left(node.left)
            return self.__rotate_right(node)

        if balance_factor < -1 and value < node.right.value:
            node.right = self.__rotate_right(node.right)
            return self.__rotate_left(node)

        return node

    def delete(self, value):
        self.root = self.__delete(self.root, value)

    def __delete(self, node, value):
        if node is None:
            return node
        elif value < node.value:
            node.left = self.__delete(node.left, value)
        elif value > node.value:
            node.right = self.__delete(node.right, value)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            temp = self.__get_min_value_node(node.right)
            node.value = temp.value
            node.right = self.__delete(node.right, temp.value)

        if node is None:
            return node

        node.height = 1 + max(self.__get_height(node.left), self.__get_height(node.right))

        balance_factor = self.__get_balance_factor(node)

        if balance_factor > 1 and self.__get_balance_factor(node.left) >= 0:
            return self.__rotate_right(node)

        if balance_factor < -1 and self.__get_balance_factor(node.right) <= 0:
            return self.__rotate_left(node)

        if balance_factor > 1 and self.__get_balance_factor(node.left) < 0:
            node.left = self.__rotate_left(node.left)
            return self.__rotate_right(node)

        if balance_factor < -1 and self.__get_balance_factor(node.right) > 0:
            node.right = self.__rotate_right(node.right)
            return self.__rotate_left(node)

        return node

    def __get_min_value_node(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    def __get_height(self, node):
        if node is None:
            return 0
        else:
            return node.height

    def __get_balance_factor(self, node):
        if node is None:
            return 0
        else:
            return self.__get_height(node.left) - self.__get_height(node.right)

    def __rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        node.height = 1 + max(self.__get_height(node.left), self.__get_height(node.right))
        new_root.height = 1 + max(self.__get_height(new_root.left), self.__get_height(new_root.right))
        return new_root

    def __rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        node.height = 1 + max(self.__get_height(node.left), self.__get_height(node.right))
        new_root.height = 1 + max(self.__get_height(new_root.left), self.__get_height(new_root.right))
        return new_root

    def search(self, value):
        return self.__search(self.root, value)

    def __search(self, node, value):
        if node is None or node.value == value:
            return node

        if value < node.value:
            return self.__search(node.left, value)
        else:
            return self.__search(node.right, value)
