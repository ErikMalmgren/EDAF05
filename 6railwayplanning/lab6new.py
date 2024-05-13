import sys

def main():
  capacity, routes, routes_to_remove, min_capacity = parse()
  removed_routs = 0
  while preflow_push(capacity) > min_capacity:
    
  

def parse():
  inp = sys.stdin.read().strip().split('\n')
  first_line = inp.pop(0).split()
  nbr_of_nodes, nbr_of_edges, nbr_of_students, nbr_of_routes = map(int, first_line[:4])
  capacity = [[0 for _ in range(nbr_of_nodes)] for _ in range(nbr_of_nodes)]
  routes = []
  for i in range(nbr_of_edges):
    u, v, c = map(int, inp[i].split())
    capacity[u][v] = c
    capacity[v][u] = c
    routes.append[(u, v)]
  routes_to_remove = []
  for i in range(nbr_of_edges, nbr_of_edges + nbr_of_routes):
    routes_to_remove.append(int(inp[i]))
  print(routes_to_remove)
  return capacity, routes, routes_to_remove, nbr_of_students

def preflow_push(capacity):
  n = len(capacity)
  height = [0] * n
  ef = [0] * n
  seen = [0] * n
  
  F = [[0] * n for _ in range(n)]
  
  def push(u, v):
    delta = min(ef[u], capacity[u][v] - F[u][v])
    F[u][v] += delta
    F[v][u] -= delta
    ef[u] -= delta
    ef[v] += delta
    
  def relabel(u):
    min_height = float('inf')
    for v in range(n):
      if capacity[u][v] - F[u][v] > 0:
        min_height = min(min_height, height[v])
        height[u] = min_height + 1
        
  def visit_neighbors(u):
    while ef[u] > 0:
      if seen[u] < n:
        v = seen[u]
        if capacity[u][v] - F[u][v] > 0 and height[u] > height[v]:
          push(u, v)
        else:
          seen[u] += 1
      else:
        relabel(u)
        seen[u] = 0
  
  height[0] = n
  ef[0] = float('inf')
  for v in range(n):
    push(0, v)
    
  p = 0
  nodes = [i for i in range(1, n - 1)]
  
  p = 0
  while p < len(nodes):
    u = nodes[p]
    old_height = height[u]
    visit_neighbors(u)
    if height[u] > old_height:
      nodes.insert(0, nodes.pop(p))
      p = 0
    else:
      p += 1
      
  return sum(F[0])
        



main()