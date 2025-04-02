class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def addElementFirst(self,value):
        node = Node(value)
        node.next = self.head
        self.head=node
        if self.tail is None:  # If the list was empty, set the tail to the new node
            self.tail = node
        self.size+=1
    def addElementLast(self, value):
        node = Node(value)  # Create a new node
        if self.tail:  # If the list is not empty
            self.tail.next = node  # Append the new node at the tail
        else:  # If the list is empty
            self.addElementFirst(value)  # Update head and tail to point to the new node
        self.tail = node
        self.size+=1
    def printelements(self):
        temp=self.head
        while temp:
            print(temp.val,end="->")
            temp=temp.next
        print("END")
    def deleteFirst(self):
        if self.head is not None:
            val=self.head.val
            self.head=self.head.next
            self.size-=1
        else:
            print("no elements")
            return
        return val
    def getelements(self,index):
        temp=self.head
        for i in range(index):
            temp=temp.next
        return temp

    def deleteLast(self):
        if self.head is not None:
            prevlast=self.getelements(self.size-2)
            prevlast.next=None
            self.tail=prevlast
            self.size-=1


class Node:
    def __init__(self,value,next=None):
        self.val=value
        self.next=next
    def __init__(self,value):
        self.val = value
        self.next = None
if __name__ == '__main__':
    ll=LinkedList()
    ll.addElementFirst(7)
    ll.addElementFirst(8)
    ll.addElementLast(100)
    ll.addElementFirst(99)
    ll.printelements()
    print(ll.size)
    ll.deleteFirst()
    ll.printelements()
    ll.deleteLast()
    ll.printelements()
    print(ll.size)


