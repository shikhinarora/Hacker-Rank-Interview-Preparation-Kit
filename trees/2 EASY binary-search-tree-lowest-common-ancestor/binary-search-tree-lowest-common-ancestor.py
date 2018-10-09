class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''


def lca(root, v1, v2):
    # Enter your code here
    val = root.info

    if val == v1 or val == v2:
        return root
    elif v1 > val > v2 or v1 < val < v2:
        return root
    elif v1 < val and v2 < val:
        return lca(root.left, v1, v2)
    else:
        return lca(root.right, v1, v2)


tree = BinarySearchTree()
t = int(raw_input())

arr = list(map(int, raw_input().split()))

for i in xrange(t):
    tree.create(arr[i])

v = list(map(int, raw_input().split()))

ans = lca(tree.root, v[0], v[1])
print ans.info
