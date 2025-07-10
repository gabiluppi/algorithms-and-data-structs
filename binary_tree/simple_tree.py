class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self) -> None:
        self.root = None
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)
            
    def _insert_recursive(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)
    
    def search(self, data):
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, node, data):
        if node is None:
            return False
        if node.data == data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)
        
    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.data)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
            
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)
    
    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.data)
        
        

tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(1)
tree.insert(10)
tree.insert(15)
tree.insert(7)

print(f'Search 3: {tree.search(3)}')
print(f'Search 5: {tree.search(5)}')
print(f'Search 1: {tree.search(1)}')
print(f'Search 10: {tree.search(10)}')
print(f'Search 15: {tree.search(15)}')
print(f'Search 7: {tree.search(7)}')
print(f'Search 0: {tree.search(0)}')
print(f'Search 8: {tree.search(8)}')

print(f'Pre traversal: {tree.preorder_traversal()}')
print(f'In traversal: {tree.inorder_traversal()}')
print(f'Post traversal: {tree.postorder_traversal()}')