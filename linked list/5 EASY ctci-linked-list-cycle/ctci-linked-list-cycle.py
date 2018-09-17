"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    # A trick that works in this case as number of nodes will always be < 100
    # counter = 0
    
    # while head.next is not None:
    #     head = head.next
    #     counter += 1
        
    #     if counter > 100:
    #         return True
        
    # return False