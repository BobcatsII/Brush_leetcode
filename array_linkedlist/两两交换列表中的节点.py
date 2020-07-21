# python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 递归方法
# 思路：
# 从链表的头节点 head 开始递归。
# 每次递归都负责交换一对节点。由 firstNode 和 secondNode 表示要交换的两个节点。
# 下一次递归则是传递的是下一对需要交换的节点。若链表中还有节点，则继续递归。
# 交换了两个节点以后，返回 secondNode，因为它是交换后的新头。
# 在所有节点交换完成以后，我们返回交换后的头，实际上是原始链表的第二个节点。

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 链表没有节点或只有一个节点
        if head == None or head.next == None: return head
        #交换的节点
        fst_node = head
        sec_node = head.next

        #交换
        fst_node.next = self.swapPairs(sec_node)
        sec_node.next = fst_node

        # sec_node 是交换后的头
        return sec_node

# 时间复杂度 O(n)，n是值链表的节点数量
# 空间复杂度 O(n)，递归过程使用的堆栈空间



# 其他方法
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        thead = ListNode(-1)
        thead.next = head
        c = thead
        while c.next and c.next.next:
            a, b=c.next, c.next.next
            c.next, a.next = b, b.next
            b.next = a
            c = c.next.next
        return thead.next   
