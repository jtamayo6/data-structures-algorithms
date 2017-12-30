class Node:
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getNext(self):
        return self.nextNode

    def setNext(self, nextNode):
        self.nextNode = nextNode


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        self.size = 1 if head != None else 0

    def insertHead(self, newData):
        newNode = Node(newData, self.head)
        self.head = newNode
        if self.tail == None:
            self.tail = newNode
        self.size += 1

    def insertTail(self, newData):
        newNode = Node(newData)
        if self.tail == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.nextNode = newNode
            self.tail = self.tail.nextNode
        self.size += 1

    def print(self):
        curr = self.head
        while curr != None:
            print(curr.data, end=' ')
            curr = curr.nextNode
        print()

    def exists(self, data):
        curr = self.head
        while curr != None and curr.data != data:
            curr = curr.nextNode

        return False if curr == None else True

    # True: data existed in list and was deleted
    # False: data did not exist in list
    def delete(self, data):
        curr = self.head
        prev = None
        while curr != None and curr.data != data:
            prev = curr
            curr = curr.nextNode

        if curr == None:
            return False
        
        if prev == None:    # Data is at head of list
            self.head = curr.nextNode
        else:
            prev.nextNode = curr.nextNode

        if curr.nextNode == None:   # Data is at tail of list
            self.tail = curr
        else:
            curr.nextNode = None    # Delete reference from current node

        self.size -= 1
        return True # Python has built-in garbage collection


if __name__ == "__main__":
    myLL = LinkedList()

    myLL.insertHead(4)
    myLL.insertHead(3)
    myLL.insertHead(2)
    myLL.insertHead(1)

    myLL.insertTail(5)
    myLL.insertTail(6)

    myLL.print()
    print("Size:", myLL.size)
    print("Is 1 in myLL?", myLL.exists(1))
    print("Is 7 in myLL?", myLL.exists(7))

    myLL.delete(4)
    myLL.delete(1)
    myLL.print()
    print("Size:", myLL.size)
