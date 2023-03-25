# Adelson-Velsky and Landis Tree

This class is an implementation of an AVL tree, a self-balancing binary search tree. It allows inserting, deleting, and searching for nodes in the tree, as well as traversing the tree in-order, pre-order, and post-order, and also printinting a diagram of the tree.

The AVLTree class has a nested Node class that represents the nodes of the tree. Each node has a value, left child, right child, and a height attribute that represents the height of the node in the tree.

The class has an insert method that takes a value and inserts a new node with that value into the tree. It does so by recursively calling a private **insert method that traverses the tree to find the appropriate position to insert the new node. After inserting the node, it updates the height of the node and checks if the tree needs to be rebalanced by calling a **rotate_right or \_\_rotate_left method, which perform the appropriate rotations to balance the tree.

The delete method takes a value and removes the node with that value from the tree. It does so by recursively calling a private \_\_delete method that finds the node to delete, replaces it with its successor, and updates the height of the affected nodes. It also checks if the tree needs to be rebalanced and performs the appropriate rotations to balance the tree.

The search method takes a value and searches for the node with that value in the tree. It does so by recursively calling a private \_\_search method that traverses the tree to find the node with the given value.

The traverse_in_order, traverse_pre_order, and traverse_post_order methods traverse the tree in the respective order and return a list of the node values.

The print_tree_diagram method generates a string representation of the tree in the form of a tree diagram. It calculates the height of the tree and uses a queue to traverse the tree level by level, keeping track of the position of each node in the diagram. It then prints out the diagram with appropriate spacing and characters to represent the branches and nodes of the tree.
