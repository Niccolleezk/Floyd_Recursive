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
floyd_iterative (graph)