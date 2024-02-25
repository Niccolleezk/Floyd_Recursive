import unittest
from Recursive import floyd

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

