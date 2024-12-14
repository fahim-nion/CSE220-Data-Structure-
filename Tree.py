class BTNOde:
    def __init__(self,element):
        self.elem = element
        self.left = None
        self.right = None
    
root = BTNOde("A")
root.left = BTNOde("B")
root.right = BTNOde("C")
root.left.left = BTNOde("D")
root.left.right = BTNOde("E")


#Tree Traversal
'''
1. Pre-Order (Each Node will be read on first-met-up)
2. In-Order (Each Node will be read on second-met-up)
3. Post Order (Each Node will be read on third-met-up))

'''

#PReOrder Traversal (Root -- Left -- Right)

def preorder(root):
    if root == None:
        return
print(root.elem, end=" ")
preorder(root.left)
preorder(root.right)


#INOrder Traversal (Left -- Root -- Right)

def inorder(root):
    if root == None:
        return
inorder(root.left)
print(root.elem, end=" ")
inorder(root.right)


##POSTOrder Traversal (Left -- Right -- Root)
def postorder(root):
    if root == None:
        return
postorder(root.left)
postorder(root.right)
print(root.elem, end=" ")



#creating a BTree from array

'''
Caution it has to be from idx 1 , 0 num idx will be None

'''

def treeFromArray(arr,i=1):
    if i>= len(arr) or arr[i] == None:
        return None
    node = BTNOde(arr[i])
    node.left = treeFromArray(arr,2*i)
    node.right = treeFromArray(arr, 2*i +1)
    return node
root = treeFromArray([None,"A","B","C","D","E"])

