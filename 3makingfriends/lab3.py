import sys
from heapq import heappop, heappush

def main():
  graph = parse()
  mst = prim(graph)
  res = sum([v for k, v in mst.values()])
  print(res)

def parse():
  inp = sys.stdin.read().split('\n')
  num_people, num_pairs = inp.pop(0).split(" ")
  inp.pop(-1)
  graph = {}
  for line in inp:
    u, v, w = map(int, line.split()) # u, v are indices of the persons of the edge and w is the weight of the edge
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