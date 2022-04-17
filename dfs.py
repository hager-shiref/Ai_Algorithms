graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'E'],
    'E': ['B', 'D'],
    'F': ['C', 'H'],
    'G': ['C'],
    'H': ['F']
}

def DFS(graph,initial,goal):
    stack=list()
    visited=list()
    stack.append(initial)
    visited.append([initial])
    while stack:
        node=stack.pop()
        path=visited.pop()
        if node==goal:
            print(path)
        else:
            for child in graph[node]:
                if child not in path:
                    stack.append(child)
                    visited.append(path+[child])

DFS(graph,'A','F')
