import timeit
from Recursive import floyd as recursive_floyd
from Iteration import floyd_iterative

graph_size = 10
large_graph = [[float('inf')] * graph_size for _ in range(graph_size)]
for i in range(graph_size):
    large_graph[i][i] = 0

iterations = 3

print("Recursive Algorithm:")
recursive_time = timeit.timeit(lambda: recursive_floyd(large_graph), number=iterations)
print("Average time:", recursive_time / iterations)

print("Iterative Algorithm:")
iterative_time = timeit.timeit(lambda: floyd_iterative(large_graph), number=iterations)
print("Average time:", iterative_time / iterations)