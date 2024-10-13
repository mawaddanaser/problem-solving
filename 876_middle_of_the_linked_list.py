# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list_node = []
        while head:
            list_node.append(head)
            head = head.next

        middle_node_index = len(list_node) // 2
        return list_node[middle_node_index]


