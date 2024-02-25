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

