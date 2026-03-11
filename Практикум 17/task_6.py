import heapq
from collections import defaultdict
import ru_local as ru


def count_distance(graph: dict, start: str, end: str) -> int:
    """
    Counts minimum distance from start point to end. Uses Dijkstra's algorithm.
    :param graph: dict with all connections and distances
    :param start: start point
    :param end: end point
    :return: distance if path from start to end exists, else -1
    """
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    pq = [(0, start)]
    visited = set()

    while pq:
        current_dist, current = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)

        if current == end:
            return current_dist

        for neighbor, weight in graph[current]:
            distance = current_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return -1


def main() -> None:
    n = int(input(ru.CITIES_AMOUNT))
    m = int(input(ru.ROADS_AMOUNT))

    graph = defaultdict(list)

    for road in range(m):
        city1, city2, dist = input().split()
        dist = int(dist)

        graph[city1].append((city2, dist))
        graph[city2].append((city1, dist))

    if len(graph) > n:
        print(ru.CITIES_ERROR)
        return None

    start, end = input().split()
    print(count_distance(graph, start, end))


if __name__ == '__main__':
    main()





