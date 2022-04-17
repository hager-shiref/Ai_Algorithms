graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':['H','I'],
    'E':['J','K'],
    'F':['L','M'],
    'G':['N','O'],
    'H':[],
    'I':[],
    'J':[],
    'K':[],
    'L':[],
    'M':[],
    'N':[],
    'O':[]
}

def DLS(start,goal,path,level,maxD):
  path.append(start)
  if start == goal:
    print("Goal found successful")
    return path
  if level==maxD:
    return False
  for child in graph[start]:
    if DLS(child,goal,path,level+1,maxD):
      return path
    path.pop()
  return False
  
  
  
start = 'A'
goal = input('Enter the goal node:-')
maxD = int(input("Enter the maximum depth limit:-"))
path = list()
if(DLS(start,goal,path,0,maxD)):
    print("Path to goal node available")
    print("Path",path)
else:
    print("No path available for the goal node in given depth limit")