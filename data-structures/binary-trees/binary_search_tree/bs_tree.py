class BSTree:
    """
    Binary Search Tree (BST) class with the following public methods:
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
        A class representing a node in the BST, with a value, left and right child nodes.
        """

        def __init__(self, value):
            """
            Create a new Node object with the given value and null left and right children.

            Args:
                value: The value of the node.
            """
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        """
        Create a new BST with null root.
        """
        self.root = None

    def insert(self, value):
        """
        Insert a new value into the BST.

        Args:
            value: The value to be inserted.
        """
        self.root = self.__insert(self.root, value)

    def __insert(self, node, value):
        """
        Recursive helper function for inserting a new value into the BST.

        Args:
            node: The root node of the BST (or a subtree).
            value: The value to be inserted.

        Returns:
            The new root node of the BST (or subtree) after the value has been inserted.
        """
        if node is None:
            return self.Node(value)

        if value < node.value:
            node.left = self.__insert(node.left, value)
        else:
            node.right = self.__insert(node.right, value)

        return node

    def delete(self, value):
        """
        Delete a value from the BST.

        Args:
            value: The value to be deleted.
        """
        self.root = self.__delete(self.root, value)

    def __delete(self, node, value):
        """
        Recursive helper function for deleting a value from the BST.

        Args:
            node: The root node of the BST (or a subtree).
            value: The value to be deleted.

        Returns:
            The new root node of the BST (or subtree) after the value has been deleted.
        """
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
        """
        Recursive helper function to get the node with the minimum value in a BST.

        Args:
            node: The root node of the BST (or a subtree).

        Returns:
            The node with the minimum value in the BST (or subtree).
        """
        current = node

        while current.left is not None:
            current = current.left

        return current

    def search(self, value):
        """
        Search for a node with the given value in the binary search tree.

        Args:
            value: The value to search for.

        Returns:
            The node containing the given value if it exists in the tree, None otherwise.
        """
        return self.__search(self.root, value)

    def __search(self, node, value):
        """
        Recursively search for a node with the given value in the binary search tree.

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
