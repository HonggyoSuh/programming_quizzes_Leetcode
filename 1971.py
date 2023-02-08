from collections import defaultdict, deque
from typing import Dict, List
import sys


class Solution:
    # def validPath(
    #     self, n: int, edges: List[List[int]], source: int, destination: int
    # ) -> bool:
    #     if source == destination:
    #         return True

    #     stack = [source]
    #     visited = set()

    #     while stack:
    #         vertex = stack.pop()
    #         if vertex not in visited:
    #             visited.add(vertex)

    #             if vertex == destination:
    #                 return True

    #             for edge in edges:
    #                 if edge[0] == vertex:
    #                     stack.append(edge[1])
    #                 elif edge[1] == vertex:
    #                     stack.append(edge[0])

    #     return False

    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        graph = defaultdict(set)

        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)

        queue, visited = deque(), set()
        queue.append(source)
        visited.add(source)

        while queue:
            node = queue.popleft()
            if node == destination:
                return True

            for adjacent_node in graph[node]:
                if adjacent_node not in visited:
                    queue.append(adjacent_node)
                    visited.add(adjacent_node)

        return False
