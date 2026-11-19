# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        ll_map={}
        node=head
        i=0
        while node:
            if node in ll_map:
                print('node present at', ll_map[node])
                return True
            ll_map[node]=i
            node=node.next
            i+=1
            print(ll_map)
        return False



        