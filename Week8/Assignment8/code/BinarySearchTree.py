


class BST:
    
    def __init__(self, value=None):
        if value is None:
            self.root = None
        else:
            self.root = self._Node(value)


    def search(self, key):
        '''Searches the BST for the key. If found a reference to that node
        is returned. Otherwise None is returned'''
        if self.root is None:
            return None

        current = self.root
        while(current is not None ):
            if key > current.value[0]:
                current = current.right
            elif key < current.value[0]:
                current = current.left
            else:
                return current
        
        return None


    def insert(self, value):
        '''Inserts the value into the correct possition of the tree.'''
        if self.root is None:
            self.root = self._Node(value)
            return
        
        parent = None
        current = self.root
        while(current is not None):
            parent = current
            if value > current.value:
                current = current.right
            else:
                current = current.left
        
        child = self._Node(value, parent=parent)
        if value > parent.value:
            parent.right = child
        else:
            parent.left = child


    def inorder(self):
        '''Prints the values of a tree in the Left-Sefl-Right pattern.'''
        if self.root is None:
            print('Empty Tree')
        else:
            self._inorder_helper(self.root)

    def _inorder_helper(self, node):
        '''Helper to inorder.'''
        if node is not None:
            self._inorder_helper(node.left)
            print(node.value)
            self._inorder_helper(node.right)
    

    class _Node: 
        '''Nods make up a BST. one node has a parent node, and left and right childern. 
        It also has a value being stored. '''
        def __init__(self, value, left=None, right=None, parent=None):
            self.value = value
            self.left = left
            self.right = right
            self.parent = parent


