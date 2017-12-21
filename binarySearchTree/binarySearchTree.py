class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root
        self.size = 1 if root != None else 0

    # True: node did not exist in BST and was added
    # False: node already exists in BST
    def add(self, val):
        if self.root:
            return self._add(val, self.root)
        else:
            self.root = Node(val)
            self.size += 1
            return True

    def _add(self, val, curr):
        if val == curr.value:
            return False
        if val < curr.value:
            if curr.left == None:
                curr.left = Node(val)
                self.size += 1
                return True
            else:
                return self._add(val, curr.left)
        else:   # val > curr.value
            if curr.right == None:
                curr.right = Node(val)
                self.size += 1
                return True
            else:
                return self._add(val, curr.right)

    def find(self, val):
        if self.root:
            if val == self.root.value:
                return True
            else:
                return self._find(val, self.root)
        else:
            return False

    def _find(self, val, curr):
        if curr == None:
            return False
        elif val == curr.value:
            return True    # value already exists in the BST
        elif val < curr.value:
            return self._find(val, curr.left)
        else:   # val > curr.value
            return self._find(val, curr.right)

    # Print BST level-by-level
    def print(self):
        print("BST:")
        queue = [self.root]
        nodesInCurrLevel = 1
        nodesInNextLevel = 0
        while queue != []:
            curr = queue.pop(0)
            nodesInCurrLevel -= 1
            if curr:
                print(curr.value, end=" ")
                if curr.left:
                    queue.append(curr.left)
                    nodesInNextLevel += 1
                if curr.right:
                    queue.append(curr.right)
                    nodesInNextLevel += 1
            if nodesInCurrLevel == 0:
                print() # Start on a new line
                nodesInCurrLevel = nodesInNextLevel
                nodesInNextLevel = 0


if __name__ == "__main__":
    myBST = BinarySearchTree()
    myBST.add(7)
    myBST.add(3)
    myBST.add(10)
    myBST.add(5)
    myBST.add(14)
    myBST.add(1)
    myBST.print()
