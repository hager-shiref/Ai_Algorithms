#depth=4
graph = {
    'A': ['B', 'C'],
    'B': ['D','E'],
    "C": ['G'],
    'D': [],
    'E': ['F'],
    'G': [],
    'F':[]
}

path = list()

def DFS(currentNode,goal,graph,maxDepth,curList):
    print("Checking for destination",currentNode)
    curList.append(currentNode)
    if currentNode==goal:
        return True
    if maxDepth<=0:
        return False
    for node in graph[currentNode]:
        if DFS(node,goal,graph,maxDepth-1,curList):
            path.append(curList)
            return True
        else:
            curList.pop()
    return False

def iterativeDDFS(currentNode,destination,graph,maxDepth):
    for i in range(maxDepth):
        curList = list()
        if DFS(currentNode,destination,graph,i,curList):
            return True
    return False

if not iterativeDDFS('A','F',graph,4):
    print("Path is not available")
else:
    print("A path exists")
    print(path.pop())