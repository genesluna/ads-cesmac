class BSTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self.__insert(self.root, value)

    def __insert(self, node, value):
        if node is None:
            return self.Node(value)

        if value < node.value:
            node.left = self.__insert(node.left, value)
        else:
            node.right = self.__insert(node.right, value)

        return node

    def delete(self, value):
        self.root = self.__delete(self.root, value)

    def __delete(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self.__delete(node.left, value)
        elif value > node.value:
            node.right = self.__delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self.__get_min_value_node(node.right)
                node.value = temp.value
                node.right = self.__delete(node.right, temp.value)

        return node

    def __get_min_value_node(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current
