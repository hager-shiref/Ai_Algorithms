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
 
def bfs(graph,start,goal):
    queue=list()
    visited=list()
    queue.append(start)
    print('visited',start)
    result=['not reached',list()]
    while queue:
        node=queue.pop(0)
        visited.append(node)
        if node==goal:
            print('goal node found',node)
            result[0]='reachable'
            break
        print(node,'goal node not found')
        for child in graph[node]:
            if child not in visited:
                queue.append(child)
    result[1]=visited
    return result

result=bfs(graph,'A','B')
print(result[0])
print('path used ',result[1])
