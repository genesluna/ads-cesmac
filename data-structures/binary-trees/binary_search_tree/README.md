# Binary Search Tree

This is a Binary Search Tree class implementation that provides the basic functionality of inserting, deleting, searching, and traversing nodes in the tree, as well as a method to print a diagram of the tree. The class uses a nested Node class to define the structure of each node in the tree, which has a value attribute and left and right child nodes.

The insert method recursively inserts a new node into the tree at the appropriate location based on the node's value. The delete method also recursively searches the tree for the node to delete and performs the deletion based on whether the node has zero, one, or two children. The search method recursively searches the tree for a node with the specified value, and the traverse_in_order, traverse_pre_order, and traverse_post_order methods perform depth-first traversals of the tree in different orders.

The print_tree_diagram method generates a string representation of the tree in the form of a tree diagram. It calculates the height of the tree and uses a queue to traverse the tree level by level, keeping track of the position of each node in the diagram. It then prints out the diagram with appropriate spacing and characters to represent the branches and nodes of the tree.
