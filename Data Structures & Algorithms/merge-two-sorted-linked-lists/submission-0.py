# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val<list2.val:
            new = list1
            list1 = list1.next
        else:
            new = list2
            list2 = list2.next   

        res = new     

        while(list1 is not None and list2 is not None):

            if list1.val<list2.val:
                new.next = list1
                new = list1
                list1 = list1.next
                
            elif list1.val>=list2.val:
                new.next = list2
                new = list2
                list2 = list2.next


        if list1 is not None:
            new.next = list1
        if list2 is not None:
            new.next = list2
            
        return res

