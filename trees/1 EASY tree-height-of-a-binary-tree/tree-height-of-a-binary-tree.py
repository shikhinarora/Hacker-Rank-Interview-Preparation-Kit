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


def height(root):
    return calculate_depth(root)


def calculate_depth(root, depth=0, max_depth=0):
    root.level = depth

    left = root.left
    right = root.right

    max_depth_left = 0
    max_depth_right = 0

    if left is not None:
        max_depth_left = calculate_depth(left, depth + 1, max_depth)

    if right is not None:
        max_depth_right = calculate_depth(right, depth + 1, max_depth)

    return max(depth, max_depth_left, max_depth_right)


tree = BinarySearchTree()
t = int(raw_input())

arr = list(map(int, raw_input().split()))

for i in xrange(t):
    tree.create(arr[i])

print height(tree.root)
