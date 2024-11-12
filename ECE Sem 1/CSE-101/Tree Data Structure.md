Tree is a non-linear data structure and forms a recursive structure

| `Name`              | `Description`                                       |
| ------------------- | --------------------------------------------------- |
| **Root Node**       | Topmost Node (A)                                    |
| **Child Node**      | Immediate Successor of a Node                       |
| **Parent Node**     | Immediate Predecessor of a Node                     |
| **Leaf Node**       | Node with no Children                               |
| **Ancestor Nodes**  | Nodes in the path from child to root                |
| **Level of a Node** | Root is at level 0 and further children add 1 level |


![[Pasted image 20241111133531.png]]

| `Property`           | `Description`                                                                                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Number of edges**  | An edge can be defined as the connection between two nodes. If a tree has N nodes then it will have (N-1) edges. There is only one path from each node to any other node of the tree |
| **Depth of Node**    | Level of a Node                                                                                                                                                                      |
| **Height of Node**   | Length of longest path from the node to the leaf node of the tree                                                                                                                    |
| **Height of tree**   | Height of the root node                                                                                                                                                              |
| **Degree of a Node** | The total count of subtrees attached to a node is its degree. Leaf nodes have 0 degree and root nodes have the highest degree                                                        |
# Tree Traversal Methods

- **Depth First Search (DFS)**
	- *Inorder Traversal:* Left -> Root -> Right `O(n)`
	- *Preorder Traversal:* Root -> Left -> Right `O(n)`
	- *Postorder Traversal:* Left -> Right -> Root `O(n)`
- **Level Order Traversal**: Visits all nodes in the same level before moving to next level. `O(n)`

```java
static void inorderTraversal(Node node) {
    // Base case
    if (node == null)
        return;
    // Recur on the left subtree
    inorderTraversal(node.left);
    // Visit the current node
    System.out.print(node.data + " ");
    // Recur on the right subtree
    inorderTraversal(node.right);
}
static void preorderTraversal(Node node) {
    // Base case
    if (node == null)
        return;
    // Visit the current node
    System.out.print(node.data + " ");
    // Recur on the left subtree
    preorderTraversal(node.left);
    // Recur on the right subtree
    preorderTraversal(node.right);
}
static void postorderTraversal(Node node) {
    // Base case: 
    if (node == null)
        return;
    // Recur on the left subtree
    postorderTraversal(node.left);
    // Recur on the right subtree
    postorderTraversal(node.right);
    // Visit the current node
    System.out.print(node.data + " ");
}
static void levelOrderTraversal(Node root) {
    if (root == null) return;
        Queue<Node> q = new LinkedList<>();
        q.add(root);
    while (!q.isEmpty()) {
        Node curr = q.poll();
        System.out.print(curr.data + " ");
        if (curr.left != null) q.add(curr.left);
        if (curr.right != null) q.add(curr.right);
    }
}
```

# Binary Tree

Binary tree is a tree data structure(non-linear) in which each node can have at most two children which are referred to as the left child and the right child.

![[Pasted image 20241111152216.png|]]

## Inserting in an unsorted binary tree:
```java
static Node insert(Node root, int key) {
    if (root == null) return new Node(key);
    // Create a queue for level order traversal
    Queue<Node> q = new LinkedList<>();
    q.add(root);
    while (!q.isEmpty()) {
        Node temp = q.poll();
        // If left child is empty, insert the new node here
        if (temp.left == null) {
            temp.left = new Node(key);
            break;
        } else {
            q.add(temp.left);
        }
        // If right child is empty, insert the new node here
        if (temp.right == null) {
            temp.right = new Node(key);
            break;
        } else {
            q.add(temp.right);
        }
    }
    return root;
}
```

## Searching in Binary Tree

The most common methods are depth-first search (DFS)(LIFO) and breadth-first search (BFS)(FIFO).

![[Pasted image 20241111154508.png]]
```java
static boolean searchDFS(Node root, int value){
    // Base case: If the tree is empty or we've reached
    // a leaf node
    if (root == null) return false;
    // If the node's data is equal to the value we are
    // searching for
    if (root.data == value) return true;
    // Recursively search in the left and right subtrees
    boolean left_res = searchDFS(root.left, value);
    boolean right_res = searchDFS(root.right, value);
    return left_res || right_res;
}
```

## Time Complexities in Binary Tree
![[Pasted image 20241111155402.png]]

## Properties of Binary Tree:
1. The maximum number of nodes at level `l` of a binary tree is $2^l$
2. The maximum number of nodes in a binary tree of height `h` will be $2^h$
3. In a binary tree with `N` nodes, minimum height is $log_2(N+1)$
4. A binary tree with `L` leaves will have at least $log_2L+1$ levels
5. In a binary tree with `N` nodes, there are `N-1` edges
## Implementation as Array
We keep the root at index 0, if index of a parent is n, then:
- left child = 2n + 1
- right child = 2n + 2
