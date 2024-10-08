class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_head = ListNode(0)  # A dummy head for the result linked list
        current = dummy_head  # Pointer to construct the new list
        carry = 0  # Initialize carry to 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # Get value from l1 or 0 if l1 is exhausted
            val2 = l2.val if l2 else 0  # Get value from l2 or 0 if l2 is exhausted
            
            total = val1 + val2 + carry  # Sum the values and the carry
            carry = total // 10  # Calculate new carry
            current.next = ListNode(total % 10)  # Create a new node with the digit
            current = current.next  # Move to the next node
            
            # Move to the next nodes in l1 and l2 if available
            if l1: 
                l1 = l1.next
            if l2: 
                l2 = l2.next
        
        return dummy_head.next  # Return the next of dummy head as the result