# 栈（只需要两个指针实现局部翻转）
# 时间复杂度为 O(n),空间复杂度为 O(k)
# 栈每次有需要开辟 k 个空间。
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        self.stack = []
        #定义一个哨兵节点
        p = ListNode(-1)
        result = p
        # 状态标志
        flag = True
        temp_head = head
        while head:
            for i in range(k):
                if not head:
                    flag = False
                    break
                self.stack.append(head)
                head = head.next
            if not flag:
                break
            else:
                temp_head = head
            for i in range(k):
                cur = self.stack.pop()
                p.next = cur
                p = cur
            # 翻转后和后面的节点相连
            p.next = temp_head
        return result.next


# 利用三个指针实现局部翻转
# 时间复杂度为O(n),空间复杂度为O(1)
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 定义一个哨兵节点
        sentry = ListNode(0)
        pre = sentry
        start = head
        flag = True
        while head:
            for i in range(k):
                if not head:
                    # 剩余节点数量小于k，跳出
                    flag = False
                    break
                head = head.next
            if not flag:
                break
            # 上次翻转后的节点连接这次翻转后的节点
            pre.next = self.reverse(start,head)
            # 连接这次翻转以后的正常节点
            start.next = head
            # 更新位置
            pre = start
            # 更新位置
            start = head
        return sentry.next

    def reverse(self,start,end):
        pre, cur, nexts = None, start, start
        # 三个指针进行局部翻转
        while cur != end:
            nexts = nexts.next
            # 箭头反指
            cur.next = pre
            # 更新pre位置
            pre = cur 
            # 更新cur位置
            cur = nexts
        return pre


# 外网高票答案
# 9行递归
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        node, i = head, 0
        while node:
            if (i:=i+1) == k: break   #python3.8.0新特新，:=赋值表达式，pep-5072,最下面有解释
            node = node.next
        if i < k: return head
        prev, node = None, head
        for _ in range(k): node.next, node, prev = prev, node.next, node
        head.next = self.reverseKGroup(node, k)
        return prev

