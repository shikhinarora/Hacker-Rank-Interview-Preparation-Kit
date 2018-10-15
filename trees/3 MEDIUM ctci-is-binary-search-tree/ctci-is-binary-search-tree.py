""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    
    return check(root, -1, 10001)
    

def check(node, mini, maxi):
    if node is None:
        return True
    else:
        l = check(node.left, mini, node.data)
        r = check(node.right, node.data, maxi)
        
        if mini < node.data < maxi:
            current = True
        else:
            current = False
            
        return l and r and current