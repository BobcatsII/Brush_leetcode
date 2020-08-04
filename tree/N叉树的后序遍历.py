# N叉树通用递归模板
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def helper(root):
            if not root:
                return
            for child in root.children:
                helper(child)
            res.append(root.val)    #后序
        helper(root)
        return res
