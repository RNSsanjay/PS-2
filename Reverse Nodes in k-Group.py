class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        last_end = dummy
        stack = []
        
        while head:
            first = head
            while len(stack) < k and head:
                stack.append(head)
                head = head.next
            if len(stack) < k:
                last_end.next = first
                break
            last_end.next = self._reverse_stack(stack)
            last_end = first
        
        return dummy.next

    def _reverse_stack(self, stack):
        node = stack.pop()
        if stack:
            node.next = self._reverse_stack(stack)
        return node
