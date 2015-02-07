### Problem:
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

### Hints:
Stack to push in and pop out to match brackets.
1. define dict of brackets, one trick to define them like {")":"("}  
2. like a compiler push into stack if not in keys  
3. pop out when it is a key, and match them together  
4. check the size of stack at the end of processing.  

#### References:

#### Tags:
Stack String
