class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum = 0
        prefix_map = {0: dummy}
        
        while head:
            prefix_sum += head.val
            if prefix_sum in prefix_map:
                prev = prefix_map[prefix_sum]
                prev.next = head.next
            else:
                prefix_map[prefix_sum] = head
            head = head.next
        
        return dummy.next
