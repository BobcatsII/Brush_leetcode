## 标准的BFS模板
def BFS(graph, start, end):
    queue = []
    queue.append([start])
    
    visited = set()  #很重要，绝对绝对不能忘
    
    while queue:
        node = queue.pop()
        visited.add(node)
        
        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)