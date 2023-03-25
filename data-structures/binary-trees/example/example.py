import sys

sys.path.append("avl_tree")
sys.path.append("bs_tree")

from avl_tree import AVLTree
from bs_tree import BSTree
from os import system

values = [10, 8, 9, 4, 2, 17, 15, 25, 3, 6, 19, 34, 1, 30, 5]

bst = BSTree()
avlt = AVLTree()

# Add values to the trees
system("clear")
print("\nInterting these values into the trees:\n")
print(values)
input("\nPress enter to continue")

for value in values:
    bst.insert(value)
    avlt.insert(value)

# Print the trees' diagrams
system("clear")
print("\nBinary Search Tree diagram after insetion:\n")
bst.print_tree_diagram()

print("\n\nAVL Tree diagram after insetion:\n")
avlt.print_tree_diagram()
input("\n\nPress enter to continue")

# Print the trees' values in-order, pre-order and post-order
system("clear")
print("\nPrinting Binary Search Tree values:\n")
print("in-order:   ", bst.traverse_in_order())
print("pre-order:  ", bst.traverse_pre_order())
print("post-order: ", bst.traverse_post_order())

print("\n\nPrinting AVL Tree values:\n")
print("in-order:   ", avlt.traverse_in_order())
print("pre-order:  ", avlt.traverse_pre_order())
print("post-order: ", avlt.traverse_post_order())
input("\nPress enter to continue")

# delete values from the Binary Search Tree and show before and after
system("clear")
print("\nDeleting value 8, 25, 30 and 5 from BS Tree...")
print("\nBinary Search Tree diagram before delition:\n")
bst.print_tree_diagram()
print("\nBinary Search Tree diagram after delition:\n")
bst.delete(8)
bst.delete(25)
bst.delete(30)
bst.delete(5)
bst.print_tree_diagram()
input("\nPress enter to continue")

# delete values from the AVL Tree and show before and after
system("clear")
print("\nDeleting value 8, 25, 19 and 4 from AVL Tree...")
print("\nBinary Search Tree diagram before delition:\n")
avlt.print_tree_diagram()
print("\nBinary Search Tree diagram after delition:\n")
avlt.delete(8)
avlt.delete(25)
avlt.delete(19)
avlt.delete(4)
avlt.print_tree_diagram()
input("\nPress enter to exit")
