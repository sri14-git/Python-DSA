def insertionsort(arr):
    for i in range(len(arr)):
        j=i
        while j>0 and arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
    return arr

def selectionsort(arr):
    n=len(arr)
    for i in range(n):
        min=i
        for j in range(i,n):
            if arr[j]<arr[min]:
                min=j
        arr[min],arr[i]=arr[i],arr[min]
    return arr
def bubblesort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
    return arr
def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    left=[]
    right=[]
    for i in arr[1:]:
        if i<pivot:
            left.append(i)
        else:
            right.append(i)
    return quicksort(left)+[pivot]+quicksort(right)
def quicks(arr,l,h):
    def findpivot(arr,l,h):
        low=l
        high=h
        pivot=l
        while low<high:
            while arr[low]<arr[pivot] and low<h:
                low+=1
            while arr[high]>arr[pivot] and high>l:
                high-=1
            if low<high:
                arr[high],arr[low]=arr[low],arr[high]
        arr[pivot],arr[high]=arr[high],arr[pivot]
        return high
    if l<h:
        pivot=findpivot(arr,l,h)
        quicks(arr,l,pivot-1)
        quicks(arr,pivot+1,h)
    return arr
# arr=[25,2,1,15,23,11]
# print(quicks(arr,0,len(arr)-1))


class LinkedList:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
        self.size=0
    def insertFirst(self,value):
        new_node=node(value)
        new_node.next=self.head
        self.head=new_node
        if self.tail is None:
            self.tail=new_node
        self.size+=1
    def PrintElements(self) -> None:
        temp=self.head
        while temp:
            print(temp.val,end="->")
            temp=temp.next
    def insertLast(self,value):
        new_node=node(value)
        if self.tail is None:
            return self.insertFirst(value)
        else:
            self.tail.next=new_node
            self.tail=new_node  
        self.size+=1
    def getelementsindex(self,value):
        temp=self.head
        for i in range(self.size):
            if temp.val==value:
                return i
            temp=temp.next
    def getelements(self,index):
        temp=self.head
        for i in range(index):
            temp=temp.next
        return temp
    def deleteIndex(self,index):
        prev=self.getelements(index-1)
        prev.next=prev.next.next
        curr=self.getelements(index)
        curr.next=None
            
class node:
    def __init__(self,value,next=None) -> None:
        self.val=value
        self.next=next

if __name__=='__main__':
    n= node(13)
    ll=LinkedList()
    ll.insertFirst(15)
    ll.insertFirst(16)
    ll.insertFirst(17)
    ll.insertFirst(18)
    ll.PrintElements()
    print(ll.getelementsindex(16))
    
    