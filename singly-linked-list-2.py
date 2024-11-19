class Node:
    def __init__(self,elem,next):
        self.elem = elem
        self.next = next

#reversing a node [[Out Of Place]]

def reverse_out_of_place(head):
    new_head = Node(head.elem,None)
    temp = head.next
    while temp!= None:
        n = Node(temp.elem,new_head)
        new_head = n
        temp = temp.next
    return new_head


#reversing in place
def reverse_in_place(head):
    new_head = None
    temp = head
    while temp!= None:
        n = temp.next
        temp.next = new_head
        new_head = temp
        temp = n
    return new_head


#neetcode reversing

#finally this thing got into my brain, and it works perfectly
def reverse (head):
    prev = None
    curr = head
    next = None
    while curr!= None:
        next = curr.next #head er shamner value ta store kore rakhlam
        curr.next = prev #node er dik change krlam None er dike [None <-- 1-->2-->3-->4]
        prev = curr #ekhon previous node banabo bortoman take
        curr = next # aar current node ta hobe ager bortoman er shamner ta
    return prev
