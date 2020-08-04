# N叉树通用递归模板
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def helper(root):
            if not root:
                return
            res.append(root.val)     #前序
            for child in root.children:
                helper(child)
        helper(root)
        return res