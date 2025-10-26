# Solve this Question:
# Use a stack to check whether a given string of HTML/XML tags is properly nested.

# Example:
# Input: "<html><body><h1>Hello</h1></body></html>"
# Output: True

# Input: "<html><body><h1></body></h1></html>"
# Output: False

# Concept Tested:
# Applying LIFO to validate opening and closing tag order.

# Every opening tag must be matched by its corresponding closing tag in reverse order of appearance.

import re

def is_html_nested_properly(s):
    # Find all tags like <html>, </html>, <body>, </body>
    tags = re.findall(r'<[^>]+>', s)
    stack = []
    
    for tag in tags:
        if not tag.startswith("</"):
            # Opening tag — remove < > and push to stack
            tag_name = tag[1:-1]
            stack.append(tag_name)
        else:
            # Closing tag — remove </ >
            tag_name = tag[2:-1]
            if not stack or stack[-1] != tag_name:
                return False
            stack.pop()
    
    # If stack is empty, tags were properly nested
    return len(stack) == 0

# Test cases
print(is_html_nested_properly("<html><body><h1>Hello</h1></body></html>"))  
print(is_html_nested_properly("<html><body><h1></body></h1></html>"))        
