class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class linkedlist:
    def __init__(self):
        self.head=None
    
    def insert_at_start(self,data):
        # Insert at leftside of linkedlist(or begining)
        node= Node(data,self.head)
        self.head=node
    def insert_at_end(self,data):
        if self.head is None:
            self.head= Node(data,None)
            return
        # iterator
        iter=self.head
        while iter.next:
            iter= iter.next
        
        # when reached to end insert the node
        iter.next= Node(data,None)
    def llist_length(self):
        count=0
        iter= self.head
        while iter:
            count+=1
            iter=iter.next
        #In the end return the total_count/length of linkedlist 
        return count

    def print(self):
        if self.head is None:
            print("Linked_list is empty")
        iter= self.head
        # concate strings
        linkListStr=""
        while iter:
            linkListStr+= f"{iter.data} ==> "
            iter=iter.next
        print(linkListStr,"NextNone")

    # insert at given index
    def insert_at_index(self,index,data):
        if index<0 or index>=self.llist_length():
            raise Exception("Index Exceeded")
        # No need to iterate if index is 0 =>complexity O(1) always and in linked_list
        # we also don't need to copy and paste all below elements down like in list 
        if index==0:
            self.insert_at_start(data)
            return
        #count so that we can stay before the index node  
        count=0
        iter= self.head
        while iter:
            if count== index-1: #when we reach the one node before the indexed node
                node= Node(data,iter.next) # our node next pointer will points to the node that the previous node next pointer were pointing to 
                iter.next= node #now we have/can change previous node next pointer to our node 
                # node successfully added in between of a linked list
            
            iter= iter.next
            count+=1
        


#Initialize Object
ll= linkedlist()
ll.insert_at_end(2)
ll.insert_at_start(1)
ll.insert_at_end(3)

ll.insert_at_index(1,8)
ll.insert_at_index(2, 9)
print(f'Length: {ll.llist_length()}')
ll.print()