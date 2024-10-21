'''
CP: https://courses.codepath.org/courses/tip101/unit/5#!session_two
Answers: https://github.com/codepath/compsci_guides/wiki/Unit-5-Session-2
'''

'''Problem 10: Double to Single
Below are the node classes for a singly linked list and a doubly linked list.
Write a function dll_to_sll() that takes in the head of a doubly linked list as a parameter
and recreates it as a singly linked list.

The function returns the head of the new singly linked list.

# DLL: Ice <-> Water <-> Steam
dll_head = Ice
sll_head = dll_to_sll(dll_head)
#SLL: Ice -> Water -> Steam'''

class SLLNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class DLLNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value 
        self.next = next
        self.prev = prev
    
def dll_to_sll(dll_head):
    current = dll_head
    while current:
        current.prev = None
        current = current.next 
    return 

steam = DLLNode('Steam')
water = DLLNode('Water', steam)
ice = DLLNode('Ice', water)
dll_head = ice
sll_head = dll_to_sll(dll_head)