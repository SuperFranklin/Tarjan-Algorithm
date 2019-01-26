import DFSRecursive
from audioop import reverse



def getLows(graph, path, number, lows):
    for vertex in reversed(path):
        p = getParent(vertex, graph, path, number)
        lows[vertex] = low(vertex, number, p, lows, path)
        parent = vertex
        number -= 1
        
        
def low(vertex, nr, parent, lows, path):
    values = []
    childs = graph[vertex]
    for child in childs:
        if child !=parent:
            values.append(path.index(child)+1)
    
    low = 999999
    for child in childs:
        if child in lows and lows[child] <low:
            low = lows[child]
    values.append(low)
    values.append(nr)
    
    return min(values)

def getParent(vertex, graph, path, nr):
    childs = graph[vertex]
    for v in reversed(path[:nr]):
        if v in childs:
            return v


def printBridges(graph, path, lows):
    for ver, low in lows.items():
        if ver == start:
            continue
        if low >= path.index(ver)+1:
            p = getParent(ver, graph, path, low)
            print ver,'<->', p
    

graph2 = {1: set([3]),
         2: set([3,4,5]),
         3: set([1,2,4,5]),
         4: set([2,3,8]),
         5: set([3,6,7]),
         6: set([5,7]),
         7: set([5,6]),
         8: set([4,9,11]),
         9: set([8,10,11]),
         10: set([11,9]),
         11: set([10,9])}

graph = { 'A': set(['B']),
          'B': set(['A','C','D','E']),
          'C': set(['D','B']),
          'D': set(['C','B','H']),
          'E': set(['B','G','F']),
          'F': set(['E','G']),
          'G': set(['E','F']),
          'H': set(['I','J','D']),
          'I': set(['K','J','H']),
          'J': set(['K','I','H']),
          'K': set(['J','I'])}

graph1 = {1:set([2,3]),
         2:set([1,3]),
         3:set([2,1,4]),
         4:set([3,5,7]),
         5:set([6,4]),
         6:set([5,7]),
         7:set([4,6])}


start = 'D'
path = DFSRecursive.rec_dfs(graph, [], start)
number = len(path)
lows = dict()
getLows(graph, path, number, lows)
printBridges(graph, path, lows)




