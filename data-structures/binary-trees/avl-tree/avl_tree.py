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

    def traverse_in_order(self):
        nodes = []

        def __traverse_in_order(node):
            if node is not None:
                __traverse_in_order(node.left)
                nodes.append(node.value)
                __traverse_in_order(node.right)

        __traverse_in_order(self.root)

        return nodes

    def traverse_pre_order(self):
        nodes = []

        def __traverse_pre_order(node):
            if node is not None:
                nodes.append(node.value)
                __traverse_pre_order(node.left)
                __traverse_pre_order(node.right)

        __traverse_pre_order(self.root)

        return nodes

    def traverse_post_order(self):
        nodes = []

        def __traverse_post_order(node):
            if node is not None:
                __traverse_post_order(node.left)
                __traverse_post_order(node.right)
                nodes.append(node.value)

        __traverse_post_order(self.root)

        return nodes

    def print_tree_diagram(self):
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
