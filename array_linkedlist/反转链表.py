class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None

        while head :
            tmp = head.next      # 备份原来head节点的next地址
            head.next = new_head
            new_head = head
            head = tmp

        return new_head


#高赞例子 4行
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        while head:
            head.next, head, pre = pre, head.next, head
        return pre
