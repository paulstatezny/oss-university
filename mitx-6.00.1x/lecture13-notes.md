# Trees

A root node with child nodes that have child nodes.
Nodes have a value.
Nodes with 0 children are called "leaves".

## Binary Trees

Every node has between 0 and 2 child nodes.
The left child node is always a lesser value, the right greater.

## Searching a Tree

Depth first search vs Breadth first search.

### Depth First Search

Uses a stack.
As you look at nodes, if the value does not match, push its children onto the stack.
Always just search for the next node on top of the stack.

### Breadth First Search

Uses a queue.
As you look at nodes, if the value does not match, push its children onto the end of the queue.
Always just search for the next node at the beginning of the queue.

## Ordered Binary Trees

Trees which for any node, all the nodes to the "left" are less than that node's value and all nodes to the "right" are greater than that node's value.

## Binary Decision Trees

Leaves are a "Power Set" -- set of all possible subsets of the initial set

# Graphs

A tree where there can be loops. (Child nodes that are parents of nodes closer to the root.)
If you search a graph