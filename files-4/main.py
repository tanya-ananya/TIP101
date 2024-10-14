'''
CP: https://courses.codepath.org/courses/tip101/unit/5#!session_one
Answers: https://github.com/codepath/compsci_guides/wiki/Unit-5-Session-2
'''

'''Problem 4: Linked List Length
Write a function ll_length() that takes in a head of a linked list as a parameter and returns
the length of the linked list.

# Linked List: num1 -> num2 -> num3
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
def ll_length(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count

num1 = Node('1')
num2 = Node('2')
num3 = Node('3')
head = num1
print(ll_length(head))
# Empty Linked List
head = None
print(ll_length(head))