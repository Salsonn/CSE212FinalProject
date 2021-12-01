# Tree

Trees are green, and these data structures try to be as well, by keeping power consumption down. Similar to linked lists, as they both store data in nodes that are linked to other nodes, however a tree stands out by having more than a previous and next node. While there are several different types of trees, we will be addressing only three: binary trees, binary search trees (or BSTs), and balanced binary search trees.

## Tree Structure

Tree nodes have several different subcategories. Most trees have two different types of nodes, parent nodes, which they connect from, and child nodes, which they connect to. Trees will only have one parent node, and binary trees are called such because they contain only two child nodes. Other node types are the root node, which is at the top of the tree and as such has no parent node, and the leaf node, which is found at the bottom of a tree and has no child nodes.

## Binary Search Trees

Trees can have their data inserted at random but what's the point of that? In order to make a tree data structure more efficient, we use Binary Search Trees, which follow predefined rules for determining where to insert data.

In the case of numerical data, a BST can simply start at the root node, and compare the data being inserted to the value at the root node. If the incoming data is greater, look at the child node on the left, and if less than, look at the child node on the right. Then repeat the process until a leaf node is found, then insert the data on the respective side of the leaf node.

Searching a BST uses the same process, and is extremely efficient, as each recursive operation cuts the number of possible addresses to search for in half, indicating a performance of O(log n).

## Balancing a BST

Binary search trees do have a caveat, however. Searching with a speed of O(log n) requrires the tree to be 'balanced', which means that the tree is has the minimum possible height. If, for example, data was to be inserted into a BST structure from greatest to least value, the structure would have no nodes on its left side, and therefore be no more efficient to work with than a linked list.

To mitigate this problem, a BST must be balanced. There are many, many different algorithms used to detect imbalance in a BST, and these won't be covered in the scope of this article. While it should not be performed on large sets of data, smaller BSTs can be rebalanced by extracting their contents into an ordered list and reforming the BST from the center point of the ordered list and moving outward to the edges.

## Example

The following shows a simple BST class written in Python. Note that Nodes are a subclass of the BST class.

```python
class BST:

    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    def _insert(self, data, node):
        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        elif data > node.data:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)
```

## Problem to Solve

Using Python, generate an ordered list of random values, 500 items long, and insert them into a BST. Write and call a function that can determine the height of the BST. You may also wish to write a function that can search for a value within the BST.

### [<-- Back](../README.md)