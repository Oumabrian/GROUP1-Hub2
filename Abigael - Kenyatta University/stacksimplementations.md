SECTION 1
1.What happens if you try to pop from an empty deque?
An error will occur(indexerror to be specific in python).

2.Why is deque faster than using a Python list for stack operations?
Because deque allows for fast appends and pops from both ends unlike a python list,deque is preferred for performance critical operations.

3.Write a method to reverse a string using a deque stack.
from collections import deque

def reversed_string_stack(s):
    stack = deque()
    for ch in s:
        stack.append(ch)
    rev = []
    while stack:
      rev.append(stack.pop())
    return ''.join(rev)

print(reversed_string_stack("hello"))

4.How can you limit the stack size using deque(maxlen=N)?
from collections import deque

dq = deque(maxlen = 2)
dq.append(1)
dq.append(3)
print(dq)

dq.append(5)
print(dq)

5.Implement a function that checks for balanced parentheses using deque.
from collection import deque

def is_balanced(expr):
   stack = deque()

   for ch in expr:
       if ch == '(':
        stack.append(ch)
       elif ch == ")":
          if not stack:
            return False
          stack.pop()
   return not stack

print(is_balanced("((()))"))
print(is_balanced("((()"))  


SECTION 2

