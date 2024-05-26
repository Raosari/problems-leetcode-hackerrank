from collections import deque

def dfs(graph,node):
    visited = set()
    stack = deque()

    visited.add(node)
    stack.append(node)

    while stack:
        s = stack.pop()
        visited.add(s)

        print(s, end=' ')
        for n in reversed(graph[s]):
            if n not in visited:
                stack.append(n)

graph = {
    'A' : ['B','G'],
    'B' : ['C','D','E'],
    'C' : [],
    'D' : [],
    'E' : ['F'],
    'F' : [],
    'G' : ['H'],
    'H' : ['I'],
    'I' : [],
}

dfs(graph=graph,node = 'A')