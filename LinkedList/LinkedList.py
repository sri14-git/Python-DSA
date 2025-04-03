from calendar import c
from tempfile import tempdir


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
    def printelements(self,index=None):
        temp=self.head
        if index is not None:
            for i in range(index):
                temp=temp.next
            print(temp.val)
        else:
            while temp:
                print(temp.val,end="->")
                temp=temp.next
            print("END")
    def deleteFirst(self): 
        if self.head is not None: # to make sure there is elements
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
        if self.head is not None: # to make sure there is elements
            prevlast=self.getelements(self.size-2)
            prevlast.next=None
            self.tail=prevlast
            self.size-=1
        else:
            print("no elements")
        if self.head == self.tail : # if only one element is present
            self.head=None
            self.tail=None
            self.size-=1
            return
    def findvalue(self,value):
        temp=self.head
        for i in range(self.size-1):
            if temp.val==value:
                return i
            temp=temp.next
        return None
    # def ReverseList(self):
    #     c=self.head
    #     p=None
    #     while c:
    #         temp=c.next # to make sure we are not loosing the list
    #         c.next=p
    #         p=c #this contiunes and p becomes the head of the list
    #         c=temp 
    #     while p:
    #             print(p.val,end="->")
    #             p=p.next
    #     print("END")




    def deleteIndex(self,index):
        prevcurr=self.getelements(index-1)
        prevcurr.next=prevcurr.next.next
        curr=self.getelements(index)
        curr.next=None
    def insertAtIndex(self,value,index):
        if index==0:
            self.addElementFirst(value)
        else:
            new_node=Node(value)
            prevcurr=self.getelements(index-1)
            new_node.next=prevcurr.next # first new nodes next is updated to make sure nothing after prevcurr is left behind
            prevcurr.next=new_node

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
    ll.addElementFirst(11)
    ll.printelements()

    ll.printelements()

