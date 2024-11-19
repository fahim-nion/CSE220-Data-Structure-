# Linked List Declaration

#Node Class Design

class Node:
    def __init__(self,elem,next):
        self.elem = elem
        self.next = next

import numpy as np

#Linked List from an Array
def list_from_array(arr):
    head = Node(arr[0],None)
    tail = head

    for i in range(1,len(arr)):
        n = Node([i],None)
        tail.next = n
        tail = tail.next
    return head

#Linked List count

def count(head):
    temp = head
    count = 0
    while temp!= None:
        count += 1
        temp = temp.next
    return count


#Retrive Element Using index

def retrive_elem(head,idx):
    count = 0
    temp = head
    result = None
    while temp!= None:
        if count == idx:
            result = temp.elem
            break
        temp = temp.next
        count+=1
    if result == None:
        return "invalid index"
    else:
        return result


#Retrive node using idx

def retrive_node(head,idx):
    temp = head
    count = 0
    result = None
    while temp!= None:
        if count == idx:
            result = temp
            return temp
        count += 1
        temp = temp.next
    return None


#Updating Element

def updateElem(head,idx,elem):
    temp = head
    count = 0
    while temp != None:
        if count == idx:
            temp.elem = elem
            break
        temp = temp.next
        count += 1


#Search index of an element

def search_index(head,elem):
    temp = head
    count = 0
    while temp!= None:
        if temp.elem == elem:
            return count
        temp = temp.next
        count += 1
    return -1


##INSERTION

#  insert at the beginning
def (head,idx,elem):
    total_nodes = count(head)
    if idx == 0:
        n = Node(elem,head)
        head = n
    # return head

#insertion at middle
    elif idx > 1 and idx < (total_nodes-1):
        n = Node(elem,None) # N namer notun node create korlam
        prev_node = retrive_node(head,idx-1) #je index e dhukabo er ager idx er node ta collect krlam
        current_node = prev_node.next # n er next node ta
        n.next = current_node        #notun node er shamner ta ekhon
        prev_node.next = n  #[link kore fellam pichoner tar shathe notun er]
    #return head

#insertion at the end
    else:
        new = Node(elem,None)
        current_node = retrive_node(head,total_nodes-1)
        current_node.next = new

    #return None


#Node Deletation

#removing first node

def delete(head,idx):
    total_nodes = count(head)
    if idx == 0:
        # current_node = retrive_node(head,idx)
        # new_head = current_node.next
        # current_node.next = None
        new_head = head.next
        head.next = None
        #return new_head
#deleting at the middle:
    elif idx>1 and idx<(total_nodes-1):
        prev_node = retrive_node(head,idx-1):
        current_node = prev_node.next
        prev_node.next = current_node.next
        current_node.next = None
    # return head