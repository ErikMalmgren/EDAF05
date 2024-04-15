import sys
from heapq import heappop, heappush


def main():
  print(sum([v for k, v in prim(parse()).values()]))

def parse():
  inp = sys.stdin.read().strip().split('\n')
  graph = {}
  for line in inp[1:]:
    u, v, w = map(int, line.split())
    graph.setdefault(u, []).append((v, w))
    graph.setdefault(v, []).append((u, w))
  return graph


def prim(graph):
  tree = {}
  visited = set()
  root = next(iter(graph))
  visited.add(root)
  queue = [(neighbor, weight) for weight, neighbor in graph[root]]
  queue.sort()
  heappush(queue, (float('inf'), None))

  while queue:
    weight, neighbor = heappop(queue)
    if neighbor and neighbor not in visited:
      visited.add(neighbor)
      tree[neighbor] = (root, weight)
      root = neighbor
      for n, w in graph[neighbor]:
        if n not in visited:
          heappush(queue, (w, n))
  return tree

main()
