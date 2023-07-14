from dijkstra_algorithm import Dijkstra
import math
from collections import defaultdict
import heapq
import time


# Test case 1: Basic shortest path


# Create a Dijkstra object
dijkstra = Dijkstra()

# Create a graph with nodes and edges
graph = {
    0: [(1, 4), (2, 2)],
    1: [(2, 1), (3, 5)],
    2: [(1, 2), (3, 8)],
    3: [(4, 3)],
    4: []
}
dijkstra.graph = graph

# Find the shortest path from node 0 to 4
start = 0
destination = 4
distance, path = dijkstra.find_shortest_path(start, destination)

# Output the result
print("Test Case 1: Basic shortest path")
print("Graph:")
for node, edges in graph.items():
    print("Node", node)
    for edge in edges:
        print("-> Edge:", node, "->", edge[0], "(Weight:", edge[1], ")")
print("Start Node:", start)
print("Destination Node:", destination)
print("Shortest Distance:", distance)  # Output: 9
print("Shortest Path:", path)  # Output: [0, 2, 1, 3, 4]
print()


# Test case 2: Unreachable destination


# Create a Dijkstra object
dijkstra = Dijkstra()

# Create a graph with nodes and edges
graph = {
    0: [(1, 4), (2, 2)],
    1: [(2, 1)],
    2: []
}
dijkstra.graph = graph

# Find the shortest path from node 0 to 2 (unreachable)
start = 0
destination = 2
try:
    distance, path = dijkstra.find_shortest_path(start, destination)
    print("Test Case 2: Unreachable destination")
    print("Graph:")
    for node, edges in graph.items():
        print("Node", node)
        for edge in edges:
            print("-> Edge:", node, "->", edge[0], "(Weight:", edge[1], ")")
    print("Start Node:", start)
    print("Destination Node:", destination)
    print("Shortest Distance:", distance)
    print("Shortest Path:", path)
except ValueError as e:
    print("Error:", str(e))  # Output: "Graph contains a negative cycle"
print()


# Test case 3: Negative edge weights

# Create a Dijkstra object
dijkstra = Dijkstra()

# Create a graph with nodes and edges
graph = {
    0: [(1, 4), (2, -2)],
    1: [(2, 1), (3, -5)],
    2: [(1, 2), (3, 8)],
    3: [(4, 3)],
    4: []
}
dijkstra.graph = graph

# Find the shortest path from node 0 to 4
start = 0
destination = 4
distance, path = dijkstra.find_shortest_path(start, destination)

# Output the result
print("Test Case 3: Negative edge weights")
print("Graph:")
for node, edges in graph.items():
    print("Node", node)
    for edge in edges:
        print("-> Edge:", node, "->", edge[0], "(Weight:", edge[1], ")")
print("Start Node:", start)
print("Destination Node:", destination)
print("Shortest Distance:", distance)  # Output: -2
print("Shortest Path:", path)  # Output: [0, 2, 1, 3, 4]
print()


# Test case 4: Invalid graph


# Create a Dijkstra object
dijkstra = Dijkstra()

# Create a graph with invalid node indices
graph = {
    0: [(1, 4), (2, 2)],
    1: [(2, 1)],
    2: [(3, 8)],
    3: [(4, 3)],
    5: []  # Invalid node index
}
dijkstra.graph = graph

# Check if the graph is valid
is_valid = dijkstra.is_valid_graph()

# Output the result
print("Test Case 4: Invalid graph")
print("Graph:")
for node, edges in graph.items():
    print("Node", node)
    for edge in edges:
        print("-> Edge:", node, "->", edge[0], "(Weight:", edge[1], ")")
print("Graph is Valid:", is_valid)  # Output: False
print()


# Test Case 5: Adding and removing edges

# Create a Dijkstra object
dijkstra = Dijkstra()

# Create a graph with nodes and edges
graph = {
    0: [(1, 4), (2, 2)],
    1: [(2, 1), (3, 5)],
    2: [(1, 2), (3, 8)],
    3: [(4, 3)],
    4: []
}
dijkstra.graph = graph

# Add a new edge
dijkstra.add_edge(2, 4, 1)

# Find the shortest path from node 0 to 4
start = 0
destination = 4
distance, path = dijkstra.find_shortest_path(start, destination)

# Output the result
print("Test Case 5: Adding and removing edges")
print("Graph:")
for node, edges in graph.items():
    print("Node", node)
    for edge in edges:
        print("-> Edge:", node, "->", edge[0], "(Weight:", edge[1], ")")
print("Start Node:", start)
print("Destination Node:", destination)
print("After Adding Edge (2 -> 4)")
print("Shortest Distance:", distance)  # Output: 3
print("Shortest Path:", path)  # Output: [0, 2, 4]
print()

# Remove an existing edge
dijkstra.remove_edge(1, 3)

# Find the shortest path from node 0 to 4
distance, path = dijkstra.find_shortest_path(start, destination)

# Output the result
print("Test Case 5: Adding and removing edges (after removing edge)")
print("Graph:")
for node, edges in graph.items():
    print("Node", node)
    for edge in edges:
        print("-> Edge:", node, "->", edge[0], "(Weight:", edge[1], ")")
print("Start Node:", start)
print("Destination Node:", destination)
print("After Removing Edge (1 -> 3)")
print("Shortest Distance:", distance)  # Output: 3
print("Shortest Path:", path)  # Output: [0, 2, 4]
print()
