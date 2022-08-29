class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        # Insert at leftside of linkedlist(or begining)
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        # iterator
        iter = self.head
        while iter.next:
            iter = iter.next

        # when reached to end insert the node
        iter.next = Node(data, None)

    def llist_length(self):
        count = 0
        iter = self.head
        while iter:
            count += 1
            iter = iter.next
        # In the end return the total_count/length of linkedlist
        return count

    def print(self):
        if self.head is None:
            print("Linked_list is empty")
        iter = self.head
        # concate strings
        linkListStr = ""
        while iter:
            linkListStr += f"{iter.data} ==> "
            iter = iter.next
        print(linkListStr, "NextNone")

    # insert at given index
    def insert_at_index(self, index, data):
        if index < 0 or index >= self.llist_length():
            raise Exception("Index Exceeded/Invalid")
        # No need to iterate if index is 0 =>complexity O(1) always and in linked_list
        # we also don't need to copy and paste all below elements down like in list
        if index == 0:
            self.insert_at_start(data)
            return
        # count so that we can stay before the index node
        count = 0
        iter = self.head
        while iter:
            if count == index-1:  # when we reach the one node before the indexed node
                # our node next pointer will points to the node that the previous node next pointer were pointing to
                node = Node(data, iter.next)
                iter.next = node  # now we have/can change previous node next pointer to our node
                # node successfully added in between of a linked list

            iter = iter.next
            count += 1

    def middleLinked(self):
        import math
        middle = self.llist_length()/2
        if middle % 2 !=0: #return middle if length is odd
            middle= math.floor(middle)

        #else return second middle element     
        iter = self.head
        count = 0
        while iter:
            if count == middle:
                print(f"The middle element of linked list is: {iter.data}")
            count += 1
            iter = iter.next
    def removeAt(self,index):
        if index < 0 or index >= self.llist_length():
            raise Exception("Index Exceeded/Invalid")
        if index==0:
            print(f"Removed {index}th element from the linkedlist")
            self.head=self.head.next
            return

        iter= self.head
        count=0
        while iter:
            if count==index-1:
                print(f"Removed indexed {count+1} element from the linkedlist")
                iter.next=iter.next.next
                break
            count+=1
            iter=iter.next
    def insertMultiple(self,list):
        for data in list:
            self.insert_at_end(data)

    def reverseLinked(self):
        prev=None
        iter= self.head
        while iter:
            next = iter.next  #save next pointer of current node
            iter.next= prev    #Now we can update the next pointer of current node and point it towards none (becomes last node)
            prev= iter   #Save the current node in previous so that when we will move to the next node we point next node next pointer to this node by using prev  
            iter= next  # The reason why we save the next pointer (Now we can move forward)

        # In the end the last node become head as the prev will be last node so we make it head
        self.head=prev



# Initialize Object
ll = linkedlist()
ll.insert_at_end(2)
ll.insert_at_start(1)
ll.insert_at_end(3)
ll.insert_at_start(6)
ll.insert_at_start(7)
ll.insert_at_start(10)

ll.insert_at_index(1, 8)
ll.insert_at_index(2, 9)
ll.print()
ll.removeAt(0)
ll.print()
ll.removeAt(4)
ll.print()
print(f'Length: {ll.llist_length()}')
ll.middleLinked()
ll.insertMultiple([11,12,13])
ll.print()
ll.reverseLinked()
print("Reversed linked list")
ll.print()
