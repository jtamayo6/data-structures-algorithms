class Node:
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insertHead(self, newData):
        newNode = Node(newData, self.head)
        self.head = newNode

    def insertTail(self, newData):
        if self.head == None:
            insertHead(newData)
            return

        curr = self.head
        while curr.nextNode != None:
            curr = curr.nextNode

        newNode = Node(newData)
        curr.nextNode = newNode

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

    # True: data existed in LinkedList and was deleted
    # False: data did not exist in LinkedList
    def delete(self, data):
        curr = self.head
        prev = None
        while curr != None and curr.data != data:
            prev = curr
            curr = curr.nextNode

        if curr == None:
            return False
        
        if prev == None:
            self.head = curr.nextNode
        else:
            prev.nextNode = curr.nextNode

        return True # Python has built-in garbage collection


if __name__ == "__main__":
    myLL = LinkedList()

    myLL.insertHead(4)
    myLL.insertHead(3)
    myLL.insertHead(2)
    myLL.insertHead(1)
    
    myLL.insertTail(5)
    myLL.insertTail(6)

    # myLL.print()
    print("Is 1 in myLL?", myLL.exists(1))
    print("Is 7 in myLL?", myLL.exists(7))

    myLL.delete(4)
    myLL.delete(1)
    myLL.print()
