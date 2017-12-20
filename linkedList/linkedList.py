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


    def printList(self):
        curr = self.head
        while curr != None:
            print(curr.data)
            curr = curr.nextNode



if __name__ == "__main__":
    myLinkedList = LinkedList()
    myLinkedList.insertHead(4)
    myLinkedList.insertHead(3)
    myLinkedList.insertHead(2)
    myLinkedList.insertHead(1)

    myLinkedList.insertTail(5)
    myLinkedList.insertTail(6)

    myLinkedList.printList()
