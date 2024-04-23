import sys
from heapq import heappop, heappush, heapify



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
  current = next(iter(graph))
  visited.add(current)

  queue = []
  for neighbor, weight in graph[current]:
    heappush(queue, (weight, neighbor))

  while queue:
    weight, neighbor = heappop(queue)
    if neighbor not in visited:
      visited.add(neighbor)
      tree[neighbor] = (current, weight)
      current = neighbor
      for n, w in graph[neighbor]:
        if n not in visited:
          heappush(queue, (w, n))
  return tree

main()
