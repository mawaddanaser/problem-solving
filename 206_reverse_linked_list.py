# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list_node = []

        while head:
            list_node.append(head.val)
            head = head.next

        # return list_node[::-1]
        ans = ListNode()
        current = ans
        for node in list_node[::-1]:
            current.next = ListNode(node)
            current = current.next
        return ans.next


