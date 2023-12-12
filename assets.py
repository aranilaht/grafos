from typing import List, TypeVar, Generic
import heapq

from math import radians, sin, cos, sqrt, atan2

T = TypeVar('T', bound=str)
W = TypeVar('W', bound=int)

grafo = []
class EdgeNDForMap(Generic[T, W]):
    def __init__(self, point1: T, point2: T, weight: W, latPoint1: float, lonPoint1: float, latPoint2: float,
                 lonPoint2: float) -> None:
        # Initialize EdgeNDForMap with point1, point2, weight, and coordinates
        self.point1: T = point1
        self.point2: T = point2
        self.weight: W = weight
        self.latPoint1: float = latPoint1
        self.lonPoint1: float = lonPoint1
        self.latPoint2: float = latPoint2
        self.lonPoint2: float = lonPoint2

# Function to safely convert string to float or replace with zero
def safe_float(input_string):
    try:
        result = float(input_string.replace(",", "."))
        return result
    except ValueError:
        return 0
# Function to calculate distance between two points
calculate_distance = lambda point1, point2: math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

def haversine(lat1, lon1, lat2, lon2):
    # Calculate Haversine distance between two points on the Earth
    R = 6371.0  # Earth radius in kilometers

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


def dijkstra(graph: List[EdgeNDForMap[T, W]], start: T, latPoint1: float, lonPoint1: float) -> T:
    # Dijkstra's algorithm to find the shortest path in a graph
    distances = {vertex.point2: float('infinity') for vertex in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for edge in graph:
            if edge.point1 == current_vertex:
                neighbor = edge.point2
                new_distance = distances[current_vertex] + edge.weight

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))

    # Find the closest vertex to the new coordinates using Haversine distance
    min_distance = float('infinity')
    closest_vertex = None

    for vertex in distances:
        matching_edges = [edge for edge in graph if edge.point2 == vertex]
        if matching_edges:
            closest_edge = min(matching_edges,
                               key=lambda edge: haversine(latPoint1, lonPoint1, edge.latPoint2, edge.lonPoint2))
            distance_to_vertex = haversine(latPoint1, lonPoint1, closest_edge.latPoint2, closest_edge.lonPoint2)

            if distance_to_vertex < min_distance:
                min_distance = distance_to_vertex
                closest_vertex = vertex

    return closest_vertex, min_distance
