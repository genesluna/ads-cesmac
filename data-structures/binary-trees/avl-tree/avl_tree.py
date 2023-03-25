class AVLTree:
    """
    A self-balancing binary search tree called an AVL tree with the following public methods:
    - insert: to insert a value in the tree
    - delete: to delete a value from the tree
    - search: to search for a value in the tree
    - traverse_in_order: to traverse the tree in-order and return a list of values
    - traverse_pre_order: to traverse the tree pre-order and return a list of values
    - traverse_post_order: to traverse the tree post-order and return a list of values
    - print_tree_diagram: to print a diagram of the tree to the console
    """

    class Node:
        """
        A class representing a node in the AVL Tree, with a value, left and right child nodes and
        the height of the node.
        """

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            self.height = 1

    def __init__(self):
        """
        Create a new AVL Tree with null root.
        """
        self.root = None

    def insert(self, value):
        """
        Insert a new value into the AVL Tree.

        Args:
            value: The value to be inserted.
        """
        self.root = self.__insert(self.root, value)

    def __insert(self, node, value):
        """
        Recursive helper function for inserting a new value into the AVL Tree.

        Args:
            node: The root node of the AVL Tree (or a subtree).
            value: The value to be inserted.

        Returns:
            The new root node of the AVL Tree (or subtree) after the value has been inserted.
        """
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
        """
        Delete a value from the AVL Tree.

        Args:
            value: The value to be deleted.
        """
        self.root = self.__delete(self.root, value)

    def __delete(self, node, value):
        """
        Recursive helper function for deleting a value from the AVL Tree.

        Args:
            node: The root node of the AVL Tree (or a subtree).
            value: The value to be deleted.

        Returns:
            The new root node of the AVL Tree (or subtree) after the value has been deleted.
        """
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
        """
        Recursive helper function to get the node with the minimum value in an AVL Tree.

        Args:
            node: The root node of the AVL Tree (or a subtree).

        Returns:
            The node with the minimum value in the AVL Tree (or subtree).
        """
        current = node

        while current.left is not None:
            current = current.left

        return current

    def __get_height(self, node):
        """
        Recursively calculate the height of a node in the AVL tree.

        Args:
            node: The node to calculate the height of.

        Returns:
            int: The height of the node. If the node is None, 0 is returned.

        """
        if node is None:
            return 0
        else:
            return node.height

    def __get_balance_factor(self, node):
        """
        Returns the balance factor of the given node, which is defined as the difference in height between
        the left and right subtrees of the node. If the node is None, the balance factor is 0.

        Args:
            node: The node whose balance factor should be calculated.

        Returns:
            int: The balance factor of the node.
        """
        if node is None:
            return 0
        else:
            return self.__get_height(node.left) - self.__get_height(node.right)

    def __rotate_right(self, node):
        """
        Performs a right rotation on the given node and returns the new root of the subtree.

        Args:
            node: The node to rotate.

        Returns:
            Node: The new root of the subtree after the rotation.
        """
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        node.height = 1 + max(self.__get_height(node.left), self.__get_height(node.right))
        new_root.height = 1 + max(self.__get_height(new_root.left), self.__get_height(new_root.right))
        return new_root

    def __rotate_left(self, node):
        """
        Performs a left rotation on the given node and returns the new root of the subtree.

        Args:
            node: The node to rotate.

        Returns:
            Node: The new root of the subtree after the rotation.
        """
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        node.height = 1 + max(self.__get_height(node.left), self.__get_height(node.right))
        new_root.height = 1 + max(self.__get_height(new_root.left), self.__get_height(new_root.right))
        return new_root

    def search(self, value):
        """
        Search for a node with the given value in the AVL binary search tree.

        Args:
            value: The value to search for.

        Returns:
            The node containing the given value if it exists in the tree, None otherwise.
        """
        return self.__search(self.root, value)

    def __search(self, node, value):
        """
        Recursively search for a node with the given value in the AVL binary search tree.

        Args:
            node: The current node being examined.
            value: The value to search for.

        Returns:
            The node containing the given value if it exists in the tree, None otherwise.
        """
        if node is None or node.value == value:
            return node

        if value < node.value:
            return self.__search(node.left, value)
        else:
            return self.__search(node.right, value)

    def traverse_in_order(self):
        """
        Traverses the tree in-order (left, root, right).

        Returns:
        - A list of the tree nodes visited in-order (left, root, right).
        """
        nodes = []

        def __traverse_in_order(node):
            if node is not None:
                __traverse_in_order(node.left)
                nodes.append(node.value)
                __traverse_in_order(node.right)

        __traverse_in_order(self.root)

        return nodes

    def traverse_pre_order(self):
        """
        Traverses the tree in pre-order (root, left, right).

        Returns:
        - A list of the tree nodes visited pre-order (root, left, right).
        """
        nodes = []

        def __traverse_pre_order(node):
            if node is not None:
                nodes.append(node.value)
                __traverse_pre_order(node.left)
                __traverse_pre_order(node.right)

        __traverse_pre_order(self.root)

        return nodes

    def traverse_post_order(self):
        """
        Traverses the tree in post-order (left, right, root).

        Returns:
        - A list of the tree nodes visited post-order (left, right, root).
        """
        nodes = []

        def __traverse_post_order(node):
            if node is not None:
                __traverse_post_order(node.left)
                __traverse_post_order(node.right)
                nodes.append(node.value)

        __traverse_post_order(self.root)

        return nodes

    def print_tree_diagram(self):
        """
        Prints a graphical representation of the binary search tree.

        Returns:
            None.
        """

        def get_height(root):
            return 1 + max(get_height(root.left), get_height(root.right)) if root else -1

        num_levels = get_height(self.root)
        width = pow(2, num_levels + 1)

        queue = [(self.root, 0, width, "c")]
        levels = []

        while queue:
            node, level, position, alignment = queue.pop(0)
            if node:
                if len(levels) <= level:
                    levels.append([])

                levels[level].append([node, level, position, alignment])
                segment = width // (pow(2, level + 1))
                queue.append((node.left, level + 1, position - segment, "l"))
                queue.append((node.right, level + 1, position + segment, "r"))

        for i, nodes in enumerate(levels):
            previous_position = 0
            previous_line_position = 0
            line_str = ""
            value_str = ""
            segment = width // (pow(2, i + 1))
            for node_info in nodes:
                value = str(node_info[0].value)
                position = node_info[2]
                alignment = node_info[3]

                if alignment == "r":
                    line_str += (
                        " " * (position - previous_line_position - 1 - segment - segment // 2)
                        + "¯" * (segment + segment // 2)
                        + "\\"
                    )
                    previous_line_position = position
                elif alignment == "l":
                    line_str += " " * (position - previous_line_position - 1) + "/" + "¯" * (segment + segment // 2)
                    previous_line_position = position + segment + segment // 2

                value_str += " " * (position - previous_position - len(value)) + value
                previous_position = position

            print(line_str)
            print(value_str)
