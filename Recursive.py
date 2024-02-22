def floyd (graph):
    "recursive algorithim to find shortest possible path"
    n = len(graph)
    def floyd_recursive (dist, a, b, c):
        if a == 0:
            return dist[b][c]
        else: 
            return min(floyd_recursive(dist, a-1, b, c), floyd_recursive(dist, a-1, b, a) + floyd_recursive(dist, k-1, a, c))

        