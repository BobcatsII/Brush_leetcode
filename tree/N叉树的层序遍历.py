##dfs
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        def dfs(root, depth):
            if not root: return 
            if len(res) <= depth:
                res.append([])
            res[depth].append(root.val)
            for ch in root.children:
                dfs(ch, depth+1)
        
        dfs(root, 0)
        return res


##BFS
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []        
        res = []
        queue = [root]                                  #初始化一个root
        while queue:
            cur = []
            res.append([])
            for node in queue:                          #因为是N叉树,所以需要遍历
                res[-1].append(node.val)
                cur.extend(node.children)
            queue = cur                                 ##重要!
        return res