for _ in range(int(input())):
    l,n=list(map(int,input().split()))
    lap=[]
    class Node:
    
        # Function to initialize the node object
        def __init__(self, data):
            self.data = data  # Assign data
            self.next = None
            self.prev = None

    class LinkedList:
        # Function to initialize head
        def __init__(self):
            self.head = None
    
        def laps(self,u,dd,tempp):
            # temp = self.head
            prev=tempp
            while (u):
                # print(tempp.data)
                if dd== 'C':
                    if(tempp == self.head):
                        lap.append(1)
                    tempp = tempp.next
                else:
                    if(tempp == self.head and lap):
                        lap.remove(1)
                    else:
                        lap.append(1)
                    tempp = tempp.prev
                u = u-1
            return tempp

        def end(self):
            temp1=self.head
            while(temp1.next):
                temp1=temp1.next
            self.head.prev = temp1
            temp1.next=self.head

        def insert(self,val):
            new_node = Node(val)

            if self.head is None:
                self.head = new_node
                return

            temp = self.head
            while(temp.next):
                temp = temp.next
            new_node.prev=temp
            temp.next=new_node
    if __name__=='__main__':
        # Start with the empty list
        llist = LinkedList()

        for i in range(1,l+1):
            llist.insert(i)
            # print("d")

        llist.end()
        tempp = llist.head
        for i in range(n):
            u,dd=list(map(str,input().split()))
            tempp=llist.laps(int(u),dd,tempp)

    print(len(lap)-1)
