#!/bin/python

import math
import os
import random
import re
import sys
from __future__ import print_function

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    counter = 0
    node = head
    
    if position == 0:
        n = SinglyLinkedListNode(data)
        n.next = head
        head = n
        
        return head
    
    while counter < position-1:
        node = node.next
        counter += 1
        
    n = SinglyLinkedListNode(data)
    
    tbs = node.next
    
    node.next = n
    n.next = tbs
    
    return head

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(raw_input())

    llist = SinglyLinkedList()

    for _ in xrange(llist_count):
        llist_item = int(raw_input())
        llist.insert_node(llist_item)

    data = int(raw_input())

    position = int(raw_input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head, ' ', fptr)
    fptr.write('\n')

    fptr.close()
