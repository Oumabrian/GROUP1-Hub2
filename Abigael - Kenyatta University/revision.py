# # LOOPS
#   #see nested loops example output

# for i in range (3):
#     for j in range (2):
#         print(i,j)
#     print( )

# for i in :
#    if i < 2 and i >6:
#        for j in range(2):
#            print(input("Enter a number "))
#            print(i,j)
# print( )       

#summing rows in loops
# row_sum += value - adds the nested list(row)
# matrix = [
#     [1, 2, 3],   # row 0
#     [4, 5, 6],   # row 1
#     [7, 8, 9]    # row 2
# ]

# for row in matrix:
#     row_sum = 0
#     for value in row:
#         row_sum += value
#     print("Row sum:", row_sum)
#print( )

#Reversing a string using deque as a stack
# from collections import deque
# def reversed_string_stack(s):
#     stack = deque()
#     for ch in s:
#         stack.append(ch)
#     rev = []
#     while stack:
#       rev.append(stack.pop())
#     return ''.join(rev)

# print(reversed_string_stack("abby"))

#Using Maxlen
# from collections import deque
# dq = deque(maxlen = 2)
# dq.append(1)
# dq.append(3)
# print(dq)
# dq.append(5)
# print(dq)

#balancing expressions
# from collections import deque

# def is_balanced(expr):
#    stack = deque()

#    for ch in expr:
#        if ch == '(':
#         stack.append(ch)
#        elif ch == ")":
#           if not stack:
#             return False
#           stack.pop()
#    return not stack

# print(is_balanced("((()))"))
# print(is_balanced("((()"))    

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class StackLinkedList:
#     def __init__(self):
#         self.top = None

#     def push(self, data):
#         new_node = Node(data)
#         new_node.next = self.top
#         self.top = new_node

#     def pop(self):
#         if not self.top:
#             raise IndexError("Pop from empty stack")
#         data = self.top.data
#         self.top = self.top.next
#         return data

#     def __iter__(self):
#         current = self.top
#         while current:
#             yield current.data
#             current = current.next


# import threading
# import time
# from queue import LifoQueue

# stack = LifoQueue()

# def producer():
#     for i in range(5):
#         stack.put(i)
#         print(f"Produced: {i}")
#         time.sleep(0.1)

# def consumer():
#     while True:
#         item = stack.get()
#         print(f"Consumed: {item}")
#         stack.task_done()
#         if item == 4:
#             break

# t1 = threading.Thread(target=producer)
# t2 = threading.Thread(target=consumer)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("All done!")

# from queue import LifoQueue

# stack = LifoQueue(maxsize=3)
# stack.put(10, block=True, timeout=2)

# from queue import LifoQueue, Empty
# import time

# stack = LifoQueue()

# try:
#     item = stack.get(block=True, timeout=2)
#     print("Got item:", item)
# except Empty:
#     print("Timeout! No item available after 2 seconds.")