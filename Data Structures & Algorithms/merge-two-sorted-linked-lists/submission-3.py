# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()          # sentinel: no "is this the first node?" check needed

        while list1 and list2:
            if list1.val <= list2.val:      # <= keeps the merge stable
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 or list2          # attach whatever is left in one step
        return dummy.next                   # None when both inputs are empty