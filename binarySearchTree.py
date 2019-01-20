class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def makeEmpty(self):
        if self.data is not None:
            self.recursiveMakeEmpty(self)
            self.data = None
            print("Deleted every node ...Now the tree is empty")
            return None
        else:
            print("Tree is already emtpy ...")
            return None

    def recursiveMakeEmpty(self, node):
        if node.left is not None:
            node.left = self.recursiveMakeEmpty(node.left)
        if node.right is not None:
            node.right = self.recursiveMakeEmpty(node.right)
        del node
        return None

    def find(self, key):
        if self is None:
            return "Nothing to find... Tree is empty."
        else:
            if self.data > key and self.left is not None:
                return self.left.find(key)
            elif self.data < key and self.right is not None:
                return self.right.find(key)
            elif self.data is key:
                print("Node "+str(key)+" : Found.")
                return None
            else:
                print("Node " + str(key) + " : Not found.")
                return None

    def findMin(self):
        if self is None:
            return "Nothing to find... Tree is empty."
        else:
            if self.left is not None:
                return self.left.findMin()
            else:
                return self.data

    def findMax(self):
        if self is None:
            return "Nothing to find... Tree is empty."
        else:
            if self.right is not None:
                return self.right.findMax()
            else:
                return self.data

    def insertANode(self, key):
        if self.data:
            if self.data > key:
                if self.left is None:
                    self.left = BinarySearchTree(key)
                else:
                    return self.left.insertANode(key)
            elif self.data < key:
                if self.right is None:
                    self.right = BinarySearchTree(key)
                else:
                    return self.right.insertANode(key)
            else:
                print("Couldn't insert the node, cuz the node already exist.")
        else:
            self.data = key

    def deleteANode(self, key):
        if self is None:
            print("Nothing to delete... Tree is empty.")
        else:
            if self.data > key and self.left is not None:
                self.left = self.left.deleteANode(key)
            elif self.data < key and self.right is not None:
                self.right = self.right.deleteANode(key)
            elif self.data == key:
                if self.left is None:
                    newNode = self.right
                    del self
                    return newNode
                elif self.right is None:
                    newNode = self.left
                    del self
                    return newNode
                minimumNode = self.right.findMin()
                self.data = minimumNode
                self.right = self.right.deleteANode(minimumNode)
            else:
                return self
            return self

    def printTree(self):
        if self.data is None:
            print("Nothing to print... Tree is empty")
        else:
            if self.left is not None:
                self.left.printTree()
            print(self.data)
            if self.right is not None:
                self.right.printTree()

    def printRoot(self):
        if self:
            print("Root = "+str(self.data))
        else:
            print("Tree is Empty.")

if __name__ == "__main__":
    r = BinarySearchTree(20)
    r.insertANode(12)
    r.insertANode(34)
    r.insertANode(21)
    r.insertANode(56)
    r.insertANode(23)
    r.insertANode(16)
    r.insertANode(14)
    r.insertANode(19)
    r.insertANode(24)
    r.printTree()
    print("Element : "+str(r.find(78)))
    print("Minimum value in tree is : "+str(r.findMin()))
    print("Maximum value in tree is : " + str(r.findMax()))
    r.find(21)
    r.find(201)
    r.deleteANode(243)
    r.deleteANode(20)
    r.printTree()
    r.printRoot()
    r.makeEmpty()
    r.printTree()
    print("Insertion after making tree empty")
    r.insertANode(16)
    r.printTree()
    r.insertANode(14)
    r.insertANode(19)
    r.printTree()