### Problem:

Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:  
Given n will always be valid.  
Try to do this in one pass.  

### Hints:
1. use two pointers, one in front one in after. Both pointed to head;  
2. first use the front one move to the nth node, and then let both of them move together;  
3. until the first one move to the end of the linked list, then the later one is pointed to the nth node from the end;  
4. need another pointer to point the previous node of the later one;  
5. let the prev one pointer to the next node of later one.


#### References:
 
#### Tags:
pointer, linked-list
