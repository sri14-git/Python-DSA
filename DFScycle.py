def detectcycle1(graph):
    visited = set()  # Initialize visited set

    def DFSforCycle(graph, node, visited, parent=None):
        visited.add(node)  # Mark the node as visited

        for neighbour in graph[node]:  # Explore neighbors
            if neighbour not in visited:  # If neighbor is unvisited
                if DFSforCycle(graph, neighbour, visited, node):  # Recur
                    return True
            elif parent != neighbour:  # If neighbor visited and not parent, cycle exists
                return True
        
        return False

    # Start DFS for all nodes in the graph
    for node in graph:
        if node not in visited:  # Start a DFS if the node is unvisited
            if DFSforCycle(graph, node, visited, None):
                return True
    
    return False  # No cycle found

# Example graph

#print(detectCycle(graph))  # Output: True (Cycle exists)





def detectcycle2(graph):
    visited=set()
    def dfscycle(graph,node,visited,parent=None):
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                if dfscycle(graph,neighbour,visited,node):
                    return True
            elif neighbour!=parent:
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfscycle(graph,node,visited):
                return True
    return False
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}
print(detectcycle2(graph))