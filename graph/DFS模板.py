visited = set()

def dfs(node, visited):
    if node in visited:  #terminator
        # already visited
        return
    visited.add(node)   # 很重要，这个点要拿出来访问的话就加到visited里面去
    
    # process current node here.
    ...
    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node, visited) 