

class DoubleLinkedList:
    

    def __init__(self) -> None:
        self.head=None
        self.tail=None
        self.size=0
    def addElementFirst(self,value):
        new_node=Node(value)
        new_node.next=self.head
        if self.head is not None:
            self.head.prev=new_node
        self.head=new_node
        if self.tail is None:
            self.tail=new_node
        self.size+=1
            
    def addElementLast(self,value):
        
        if self.tail is None:
            self.addElementFirst(value)
        else:
            new_node=Node(value)
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.size+=1
    def getelements(self,index):
        temp=self.head
        for i in range(index):
            temp=temp.next
        return temp.next

    def printelements(self,index=None):
        temp=self.head
        if index is not None:
            for i in range(index):
                temp=temp.next
            print(temp.value)
        else:
            print("START  ",end="")
            while temp:
                print(temp.value,end=" <-> ")
                temp=temp.next
            print(" END")
    def printReverse(self):
        temp=self.tail
        if self.tail is not None:
            print("END ",end="")
            while temp:
                print(temp.value,end=" <-> ")
                temp=temp.prev
            print("START ")

class Node: 
        def __init__(self,value,prev=None,next=None) -> None:
            self.value = value
            self.prev=prev
            self.next=next


if __name__=="__main__":
    dl=DoubleLinkedList()
    dl.addElementFirst(5)
    dl.addElementFirst(6)
    dl.addElementLast(7)
    dl.printelements()
    dl.printReverse()

