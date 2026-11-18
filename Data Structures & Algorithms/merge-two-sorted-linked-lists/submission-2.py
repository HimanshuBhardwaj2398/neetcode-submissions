# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        pointer_1=list1
        pointer_2=list2


        head=ListNode(val="")
        curr=head
        prev=None 
        while pointer_1 or pointer_2: 

            if not pointer_1:
                curr.val=pointer_2.val
                pointer_2=pointer_2.next

            elif not pointer_2:
                curr.val=pointer_1.val
                pointer_1=pointer_1.next
            elif pointer_1.val<=pointer_2.val:
                curr.val= pointer_1.val 
                pointer_1=pointer_1.next
            else:
                curr.val=pointer_2.val
                pointer_2=pointer_2.next

            if prev:
                prev.next=curr
            prev=curr
            curr=ListNode()

        return head 




        