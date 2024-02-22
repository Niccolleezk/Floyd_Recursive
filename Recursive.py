def floyd (graph):
    "recursive algorithim to find shortest possible path"
    n = len(graph)
    def floyd_recursive (dist, a, b, c):
        if a == 0:
            return dist[b][c]
        else: 
            return min(floyd_recursive(dist, a-1, b, c), floyd_recursive(dist, a-1, b, a) + floyd_recursive(dist, a-1, a, c))
    for a in range (n):
        for b in range (n):
            for c in range (n):
                graph [b][c]= floyd_recursive (graph, a, b, c)
    return graph 

import unittest

class TestingFloyd (unittest.TestCase):
    def testing_floyd (self):
        graph = [
            [0, 5, float('inf'), 10],
            [float('inf'), 0, 3, float('inf')],
            [float('inf'), float('inf'), 0, 1],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
        result = floyd(graph)
        expected = [
            [0, 5, 8, 9],
            [float('inf'), 0, 3, 4],
            [float('inf'), float('inf'), 0, 1],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()


"Below is the imperative version of Floyd's Algorithim which is provided" 

import sys
import itertools
graph = [
            [0, 5, float('inf'), 10],
            [float('inf'), 0, 3, float('inf')],
            [float('inf'), float('inf'), 0, 1],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
MAX_LENGTH = len(graph[0])

def floyd_iterative(distance):
    for intermediate, start_node,end_node\
    in itertools.product\
    (range(MAX_LENGTH),range(MAX_LENGTH), range(MAX_LENGTH)):
        if start_node == end_node:
            distance[start_node][end_node] = 0
        continue
    distance[start_node][end_node] = min(distance[start_node][end_node], distance[start_node][intermediate] + distance[intermediate][end_node] )
    print (distance)
floyd (graph)

