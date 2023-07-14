# Dijkstra Algorithm

The Dijkstra Algorithm is an algorithm for finding the shortest path between nodes in a graph. This implementation of the Dijkstra Algorithm allows you to:

- Create a graph with nodes and edges
- Find the shortest path between two nodes
- Add and remove edges from the graph
- Check the validity of the graph

## Soleves Problem: 
 - Implement Dijkstra's algorithm to find the shortest path between two nodes in a weighted graph.
## How to Use:

1. Import the required modules:
    ```python
    import math
    from collections import defaultdict
    import heapq
    ```
2. Copy the `Dijkstra` class into your code or import it from the `dijkstra_algorithm` module:
    ```python
    from dijkstra_algorithm import Dijkstra
    ```
3. Create a `Dijkstra` object:
    ```python
    dijkstra = Dijkstra()
    ```
4. Add edges to the graph using the `add_edge` method. The method takes three parameters: node1, node2, and weight.
    ```python
    dijkstra.add_edge(node1, node2, weight)
    ```
5. Find the shortest path between two nodes using the `find_shortest_path` method:
    ```python
    distance, path = dijkstra.find_shortest_path(start, destination)
    ```
6. You can also visualize the shortest path using the `visualize_shortest_path` method. The method takes three parameters: `start`, `destination`, and `path`.
    ```python
    dijkstra.visualize_shortest_path(start, destination, path)
    ```
8. To remove an edge from the graph, use the `remove_edge` method:
    ```python
    dijkstra.remove_edge(node1, node2)
    ```
9. To check the validity of the graph, use the `is_valid_graph` method:
    ```python
    is_valid = dijkstra.is_valid_graph()
    ```
10. Run your Python script to see the output.

## Example:

Here's an example that demonstrates the usage of the Dijkstra Algorithm:

```python
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
print("Shortest Distance:", distance)
print("Shortest Path:", path)
```
**This Will Output**:
```mathematica
Shortest Distance: 12
Shortest Path: [0, 2, 1, 3, 4]
```

### For more detailed examples and method descriptions, please refer to the code comments. Also see `Dijkstra_test.py` for test cases.

