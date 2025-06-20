class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()  # Dummy node to simplify edge cases
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach the remaining part of either list
        current.next = list1 if list1 else list2

        return dummy.next
