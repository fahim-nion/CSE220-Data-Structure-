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

#Linked List iteration

def iteration(head):
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


#insert node at one index