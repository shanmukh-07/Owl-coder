#User function Template for python3

#User function Template for python3

# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None


#Back-end complete function Template for Python 3
class Solution:
    
    def reorderList(self,head):
        l = []
        t = head
        while t:
            l.append(t.data)
            t = t.next
        n = len(l)
        fl = []
        i = 0
        j = n-1
        while i<=j:
            if i == j:
                fl.append(l[i])
            else:
                fl.append(l[i])
                fl.append(l[j])
            i += 1
            j -= 1
        t = head
        for i in fl:
            t.data = i
            t = t.next
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
            self.tail = self.head
        else:
            new_node = node(val)
            self.tail.next = new_node
            self.tail = new_node

    def createList(self, arr, n):
        for i in range(n):
            self.insert(arr[i])
        return self.head

    def printList(self,head):
        tmp = head
        while tmp is not None:
            print(tmp.data, end=" ")
            tmp=tmp.next
        print()

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        lis = Linked_List()
        head = lis.createList(arr, n)
        ob=Solution()
        ob.reorderList(head)

        lis.printList(head)

# } Driver Code Ends