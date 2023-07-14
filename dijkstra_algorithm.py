import math
from collections import defaultdict
import heapq


class Dijkstra:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, node1, node2, weight):
        self.graph[node1].append((node2, weight))
        self.graph[node2].append((node1, weight))

    def find_shortest_path(self, start, destination):
        if self.contains_negative_cycle():
            raise ValueError("Graph contains a negative cycle")

        num_nodes = len(self.graph)
        distance = [math.inf] * num_nodes
        distance[start] = 0
        previous = [None] * num_nodes
        heap = [(0, start)]

        while heap:
            current_dist, current_node = heapq.heappop(heap)

            if current_node == destination:
                break

            if current_dist > distance[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:
                distance_through_current = distance[current_node] + weight

                if distance_through_current < distance[neighbor]:
                    distance[neighbor] = distance_through_current
                    previous[neighbor] = current_node
                    heapq.heappush(heap, (distance_through_current, neighbor))

        # Extract the shortest path
        path = []
        node = destination

        while node != start:
            path.append(node)
            node = previous[node]

        path.append(start)
        path.reverse()

        return distance[destination], path

    def contains_negative_cycle(self):
        num_nodes = len(self.graph)
        distance = [[math.inf] * num_nodes for _ in range(num_nodes)]

        for node in self.graph:
            distance[node][node] = 0

        for node in self.graph:
            for neighbor, weight in self.graph[node]:
                distance[node][neighbor] = weight

        for k in range(num_nodes):
            for i in range(num_nodes):
                for j in range(num_nodes):
                    if distance[i][k] + distance[k][j] < distance[i][j]:
                        distance[i][j] = distance[i][k] + distance[k][j]

        for node in self.graph:
            if distance[node][node] < 0:
                return True

        return False

    def remove_edge(self, node1, node2):
        self.graph[node1] = [(node, weight)
                             for node, weight in self.graph[node1] if node != node2]
        self.graph[node2] = [(node, weight)
                             for node, weight in self.graph[node2] if node != node1]

    def prune_graph(self, irrelevant_nodes):
        for node in irrelevant_nodes:
            del self.graph[node]

        self.graph = {node: [(neighbor, weight)
                             for neighbor, weight in neighbors if neighbor not in irrelevant_nodes]
                      for node, neighbors in self.graph.items()
                      if node not in irrelevant_nodes}

    def is_valid_graph(self):
        num_nodes = len(self.graph)
        for node in self.graph:
            if not (0 <= node < num_nodes):
                return False
            for neighbor, weight in self.graph[node]:
                if not (0 <= neighbor < num_nodes):
                    return False
        return True

    def visualize_shortest_path(self, start, destination, path):
        path_nodes = set(path[:-1])
        for node in self.graph:
            if node == start:
                print(f"Start Node: {node} (Shortest Distance: 0)")
            elif node == destination:
                print(f"Destination Node: {node}")
            elif node in path_nodes:
                distance = self.get_distance(node, start)
                node_path = self.get_path(node, start, path)
                print(
                    f"Node {node} (Shortest Distance: {distance}), Path: {node_path}")
            else:
                distance = self.get_distance(node, start)
                print(f"Node {node} (Shortest Distance: {distance})")

    def get_distance(self, node, start):
        num_nodes = len(self.graph)
        distance = [math.inf] * num_nodes
        distance[start] = 0
        heap = [(0, start)]

        while heap:
            current_dist, current_node = heapq.heappop(heap)

            if current_node == node:
                return current_dist

            if current_dist > distance[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:
                distance_through_current = distance[current_node] + weight

                if distance_through_current < distance[neighbor]:
                    distance[neighbor] = distance_through_current
                    heapq.heappush(heap, (distance_through_current, neighbor))

        return math.inf

    def get_path(self, node, start, path):
        if node == start:
            return str(start)

        path_str = ""
        while True:
            for i, n in enumerate(path):
                if n == node:
                    path_str += f"{node} -> "
                    node = i
                    break
            else:
                break

        return path_str.rstrip(" -> ")
