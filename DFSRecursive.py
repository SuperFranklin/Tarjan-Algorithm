graph = {'A': set([ 'C','B']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def rec_dfs(graph, path, start):
    path.append(start)
    for neighbor in graph[start]:
        if neighbor not in path:
            path = rec_dfs(graph, path, neighbor)
            
    return path


