# This is a tree-traversal algorithm for Smart City Route Optimization for Emergency Services.
# This algorithm focuses on BFS and DFS

from collections import deque

# Function to perform BFS on the city road network
def bfs_shortest_path(city_graph, start_node, target_node):
    # Queue to store the path to explore
    queue = deque([(start_node, [start_node])])  # each element is (current_node, path_to_current_node)
    visited = set()  # to keep track of visited intersections

    # BFS traversal
    while queue:
        current_node, path = queue.popleft()  # Dequeue the current node and its path
        
        # Check if we reached the target node
        if current_node == target_node:
            return path  # Return the path to the destination
        
        # Mark the current node as visited
        visited.add(current_node)
        
        # Traverse all connected intersections (neighbors)
        for neighbor in city_graph[current_node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))  # Enqueue neighbor with updated path

    # If we exhaust the queue without finding the target, return None (no path found)
    return None

# Example usage of the BFS algorithm
# Define a sample city road network as a graph
city_graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E", "G"],
    "G": ["F"]
}

# Define the start and target intersections
start_node = "A"  # Start location of the emergency vehicle
target_node = "G"  # Location of the emergency

# Run the BFS algorithm to find the shortest path
shortest_path = bfs_shortest_path(city_graph, start_node, target_node)
print("Shortest path from start to target:", shortest_path)


# Function to perform DFS on the city road network

# Define the city as a weighted graph where nodes are locations and edges are roads with weights

# City graph represented as an adjacency list with weighted edges
# Format: { location1: [(neighbor1, weight1), (neighbor2, weight2)], ... }

city_graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('D', 4), ('E', 5)],
    'C': [('F', 1)],
    'D': [('G', 2)],
    'E': [('H', 3)],
    'F': [('I', 4)],
    'G': [],
    'H': [],
    'I': []
}

def dfs_optimized_route(city_graph, start, target):
    visited = set()  # Set to keep track of visited nodes
    min_path = []    # To store the minimum path found
    min_distance = float('inf')  # Set initial minimum distance to infinity

    def dfs(node, current_path, current_distance):
        nonlocal min_distance, min_path
        
        # Mark the current node as visited and add it to the current path
        visited.add(node)
        current_path.append(node)
        
        # If the target node is reached, check if this path is shorter
        if node == target:
            if current_distance < min_distance:
                min_distance = current_distance
                min_path = current_path.copy()  # Store the path with the minimum distance

        # Traverse neighbors
        for neighbor, distance in city_graph.get(node, []):
            if neighbor not in visited:
                # Recurse with updated path and distance
                dfs(neighbor, current_path, current_distance + distance)

        # Backtrack: remove the current node from path and mark it as unvisited
        visited.remove(node)
        current_path.pop()

    # Start DFS from the starting point
    dfs(start, [], 0)

    return min_path, min_distance

# Example Usage
start = 'A'    # Starting point (emergency dispatch center)
target = 'H'   # Target location (emergency location)

# Get the optimized route and distance
optimized_path, shortest_distance = dfs_optimized_route(city_graph, start, target)

print("Optimized Path:", optimized_path)
print("Shortest Distance:", shortest_distance)
