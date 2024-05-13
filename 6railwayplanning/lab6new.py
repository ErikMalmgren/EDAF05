import sys
from collections import deque


def main():
  capacity, routes, routes_to_remove, min_capacity = parse()
  findX(capacity, routes, routes_to_remove, min_capacity)


def findX(capacity, routes, routes_to_remove, min_capacity):
  start = 0
  end = len(routes_to_remove)
  mid = (start + end) // 2
  remove_counter = 0
  while (start <= end or current_capacity < min_capacity):
    capacity_copy = [row[:] for row in capacity]
    mid = (start + end) // 2
    for i in range(mid):
      u, v = routes[routes_to_remove[i]]
      capacity_copy[u][v] = 0
      capacity_copy[v][u] = 0
    current_capacity = preflow_push(capacity_copy)
    if current_capacity >= min_capacity:
      start = mid + 1
    else:
      remove_counter = mid
      end = mid - 1
  res = str(remove_counter - 1) + ' ' + str(current_capacity)
  print(res)


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
    routes.append((u, v))
  routes_to_remove = []
  for i in range(nbr_of_edges, nbr_of_edges + nbr_of_routes):
    routes_to_remove.append(int(inp[i]))
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
    height[u] += 1

  def visit_neighbors(u):
    while ef[u] > 0:
      if capacity[u][seen[u]] - F[u][seen[u]] > 0 and height[u] > height[seen[u]]:
        push(u, seen[u])
      if seen[u] < n - 1:
        seen[u] += 1
      else:
        relabel(u)
        seen[u] = 0
        nodes.append(u)

  height[0] = n
  ef[0] = float('inf')
  for v in range(n):
    push(0, v)

  nodes = deque(range(1, n - 1))
  while nodes:
    u = nodes.popleft()
    old_height = height[u]
    visit_neighbors(u)
    if height[u] > old_height:
      nodes.appendleft(u)
  return sum(F[0])


main()
