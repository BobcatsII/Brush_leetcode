#哈希表---记录访问过的位置 O(n)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        dic = {}
        while head:
            if dic.get(head,0) != 0:   # dic.get(xxx, 0) 里 “xxx”不在字典里输出0，“xxx”在字典里输出value值(也就是不等于0)
                return True
            else:
                dic[head] = 1    # 将这个节点以head为key，以value=1加入字典{head: 1}
            head = head.next    # head前移
        return False

#快慢指针 O(1)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = low = head
        while fast and fast.next:
            low = low.next
            fast = fast.next.next
            if fast == low:
                return True
        return False

