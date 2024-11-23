#initialization of a DoublyLinkedList

class DoublyNode:
    def __init__(self,elem,next,prev):
        self.elem = elem
        self.next = next
        self.prev = prev


#dll from array

def list_from_array(arr):
    dummy_head = DoublyNode(None,None,None)
    dummy_head.next = dummy_head
    dummy_head.prev = dummy_head
    tail = dummy_head
    for i in range(len(arr)):
        n = DoublyNode(arr[i],dummy_head,tail)
        tail.next = n
        tail = tail.next
        dummy_head.prev = tail
    return dummy_head


#iterations

def iterations(dummy_head):
    temp = dummy_head.next
    while temp!= dummy_head:
        print(temp.elem)
        temp = temp.next



#retrive_Node
def retrive_node(dummy_head,idx):
    temp = dummy_head.next
    c = 0
    while temp != dummy_head:
        if c == idx:
            return temp
        temp = temp.next
        c+=1
    return None

#insert
def insert(dummy_head,elem,idx):
    new_node = DoublyNode(elem,None,None)
    curr_Node = retrive_node(dummy_head,idx)
    prev_node = curr_Node.prev
    new_node.next = curr_Node
    new_node.prev = prev_node
    prev_node.next = new_node
    curr_Node.prev = new_node
    return dummy_head



#delete node
def delete(dummy_head,idx):
    curr_node = retrive_node(dummy_head,idx)
    prev_node = curr_node.prev
    next_node = curr_node.next
    prev_node.next = next_node
    next_node.prev = prev_node
    curr_node.next = None
    curr_node.prev = None
    return dummy_head