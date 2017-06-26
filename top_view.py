"""
You are given a pointer to the root of a binary tree. Print the top view of the
binary tree. Top view means when you look the tree from the top the nodes you
will see will be called the top view of the tree. See the example below.
You only have to complete the function.

For example :
   1
    \
     2
      \
       5
      /  \
     3    6
      \
       4

Top View : 1 -> 2 -> 5 -> 6

"""


def topView(root, order=0):
    # use order to keep track of which side you're on
    if root:
        # negative means on the left side, so keep printing the left
        if order <= 0:
            topView(root.left, -1)
        # print the current node's data
        print root.data,
        #if positive means on the right side, so keep printing the right
        if order >= 0:
            topView(root.right, 1)
