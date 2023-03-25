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

        # If the current node is None, create a new node with the value and return it.
        if node is None:
            return self.Node(value)

        # If the value to be inserted is less than the current node's value, go to the left subtree.
        elif value < node.value:
            node.left = self.__insert(node.left, value)

        # If the value to be inserted is greater than or equal to the current node's value, go to the right subtree.
        else:
            node.right = self.__insert(node.right, value)

        # Update the height of the current node.
        node.height = 1 + max(self.__get_height(node.left), self.__get_height(node.right))

        # Check the balance factor of the current node to determine if it is balanced or unbalanced.
        balance_factor = self.__get_balance_factor(node)

        # If the current node is left-heavy and the value to be inserted is less than the value of its left child,
        # perform a right rotation to balance the tree.
        if balance_factor > 1 and value < node.left.value:
            return self.__rotate_right(node)

        # If the current node is right-heavy and the value to be inserted is greater than the value of its right child,
        # perform a left rotation to balance the tree.
        if balance_factor < -1 and value > node.right.value:
            return self.__rotate_left(node)

        # If the current node is left-heavy and the value to be inserted is greater than the value of its left child,
        # perform a left-right rotation to balance the tree.
        if balance_factor > 1 and value > node.left.value:
            node.left = self.__rotate_left(node.left)
            return self.__rotate_right(node)

        # If the current node is right-heavy and the value to be inserted is less than the value of its right child,
        # perform a right-left rotation to balance the tree.
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

        # If the node is None, return None
        if node is None:
            return node

        # If the value is less than the node's value, search in the left subtree
        elif value < node.value:
            node.left = self.__delete(node.left, value)

        # If the value is greater than the node's value, search in the right subtree
        elif value > node.value:
            node.right = self.__delete(node.right, value)

        # If the value matches the node's value
        else:
            # If the node has no left child, replace the node with its right child
            if node.left is None:
                temp = node.right
                node = None
                return temp

            # If the node has no right child, replace the node with its left child
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            # If the node has both left and right children
            else:
                # Find the minimum value in the right subtree
                temp = self.__get_min_value_node(node.right)
                # Replace the node's value with the minimum value
                node.value = temp.value
                # Delete the minimum value node from the right subtree
                node.right = self.__delete(node.right, temp.value)

        # Update the height of the current node.
        node.height = 1 + max(self.__get_height(node.left), self.__get_height(node.right))

        # Check the balance factor of the current node to determine if it is balanced or unbalanced.
        balance_factor = self.__get_balance_factor(node)

        # If the current node is left-heavy and the left subtree's balance factor is greater than or equal to 0,
        # perform a right rotation
        if balance_factor > 1 and self.__get_balance_factor(node.left) >= 0:
            return self.__rotate_right(node)

        # If the current node is right-heavy and the right subtree's balance factor is less than or equal to 0,
        # perform a left rotation
        if balance_factor < -1 and self.__get_balance_factor(node.right) <= 0:
            return self.__rotate_left(node)

        # If the current node is left-heavy and the left subtree's balance factor is less than 0,
        # perform a left-right rotation
        if balance_factor > 1 and self.__get_balance_factor(node.left) < 0:
            node.left = self.__rotate_left(node.left)
            return self.__rotate_right(node)

        # If the current node is right-heavy and the right subtree's balance factor is greater than 0,
        # perform a right-left rotation
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

        # Traverse the tree by going to the left child of each node until we reach the minimum value node.
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
            # if the node is None, its height is 0
            return 0
        else:
            # otherwise, returns the current node height
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
            # if the node is None, its balance factor is 0
            return 0
        else:
            # otherwise, the balance factor is the height of its left subtree minus the height of its right subtree
            return self.__get_height(node.left) - self.__get_height(node.right)

    def __rotate_right(self, node):
        """
        Performs a right rotation on the given node and returns the new root of the subtree.

        Args:
            node: The node to rotate.

        Returns:
            Node: The new root of the subtree after the rotation.
        """
        new_root = node.left  # Save the left child of the given node as the new root.
        node.left = new_root.right  # Make the right child of the new root the left child of the original node.
        new_root.right = node  # Make the original node the right child of the new root.

        # Recalculate the height of the original node and the new root based on their new children.
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
        new_root = node.right  # Save the right child of the given node as the new root.
        node.right = new_root.left  # Make the left child of the new root the right child of the original node.
        new_root.left = node  # Make the original node the left child of the new root.

        # Recalculate the height of the original node and the new root based on their new children.
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

        def __traverse_in_order(node):
            # If the current node is not None, traverse the left subtree,
            # visit the current node, and then traverse the right subtree
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
