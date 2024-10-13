# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary_list = []
        while head:
            binary_list.append(head.val)
            head = head.next

        decimal_num = 0
        for i, num in enumerate(binary_list[::-1]):
            decimal_num += (2 ** i) * num
        return decimal_num