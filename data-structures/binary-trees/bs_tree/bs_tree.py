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

        # If the current node is None, the value becomes the new node
        if node is None:
            return self.Node(value)

        # If the value is less than the current node's value, go left
        if value < node.value:
            # Recursively insert the value into the left subtree
            node.left = self.__insert(node.left, value)
        else:
            # If the value is greater than or equal to the current node's value, go right
            # Recursively insert the value into the right subtree
            node.right = self.__insert(node.right, value)

        # Return the current node (or subtree)
        # This is needed to connect the newly created nodes to their parent nodes in the recursion
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

        # If the current node is None, return it to terminate recursion.
        if node is None:
            return node

        # If the value to be deleted is less than the current node's value, recursively search in the left subtree.
        if value < node.value:
            node.left = self.__delete(node.left, value)

        # If the value to be deleted is greater than the current node's value, recursively search in the right subtree.
        elif value > node.value:
            node.right = self.__delete(node.right, value)

        # If the value to be deleted matches the current node's value, we need to handle three cases.
        else:
            # If the current node has no left child, replace the current node with its right child.
            if node.left is None:
                return node.right

            # If the current node has no right child, replace the current node with its left child.
            elif node.right is None:
                return node.left

            # If the current node has both left and right children, replace the current node's value with the
            # smallest value in its right subtree and then delete that node.
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

        # Traverse the tree by going to the left child of each node until we reach the minimum value node.
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

        # If the current node is None or it contains the desired value, return it
        if node is None or node.value == value:
            return node

        # If the desired value is less than the current node's value, recursively search the left subtree
        if value < node.value:
            return self.__search(node.left, value)

        # Otherwise, recursively search the right subtree
        else:
            return self.__search(node.right, value)

    def traverse_in_order(self):
        """
        Traverses the tree in-order (left, root, right).

        Returns:
        - A list of the tree nodes visited in-order (left, root, right).
        """
        nodes = []

        # If the current node is not None, traverse the left subtree,
        # visit the current node, and then traverse the right subtree
        def __traverse_in_order(node):
            if node is not None:
                __traverse_in_order(node.left)
                nodes.append(node.value)
                __traverse_in_order(node.right)

        # Start the traversal at the root of the tree
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
            # If the current node is not None, visit the current node,
            # traverse the left subtree, and then traverse the right subtree
            if node is not None:
                nodes.append(node.value)
                __traverse_pre_order(node.left)
                __traverse_pre_order(node.right)

        # Start the traversal at the root of the tree
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
            # If the current node is not None, traverse the left subtree,
            # traverse the right subtree, and then visit the current node
            if node is not None:
                __traverse_post_order(node.left)
                __traverse_post_order(node.right)
                nodes.append(node.value)

        # Start the traversal at the root of the tree
        __traverse_post_order(self.root)

        return nodes

    def print_tree_diagram(self):
        """
        Prints a graphical representation of the binary search tree.

        Returns:
            None.
        """

        # Helper function to find the height of the binary tree
        def get_height(root):
            return 1 + max(get_height(root.left), get_height(root.right)) if root else -1

        # Calculate the total number of levels and width of the binary tree
        num_levels = get_height(self.root)
        width = pow(2, num_levels + 1)

        # Initialize the queue with the root node, level, position and alignment
        queue = [(self.root, 0, width, "c")]
        levels = []

        # Traverse the binary tree level by level and store the nodes in a list
        while queue:
            node, level, position, alignment = queue.pop(0)
            if node:
                if len(levels) <= level:
                    levels.append([])

                # Store the node, level, position, and alignment information in a list
                levels[level].append([node, level, position, alignment])
                segment = width // (pow(2, level + 1))
                queue.append((node.left, level + 1, position - segment, "l"))
                queue.append((node.right, level + 1, position + segment, "r"))

        # Print the binary tree
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

                # Add the lines that connect the nodes
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

                # Add the node value to the value string
                value_str += " " * (position - previous_position - len(value)) + value
                previous_position = position

            print(line_str)
            print(value_str)
