import sys

class Edge():
  def  __init__(self, node1, node2, capacity, flow, activated) -> None:
    self.node1 = node1
    self.node2 = node2
    self.capacity = capacity
    self.flow = flow
    self.activated = activated


def main():
  graph, routes_to_remove = parse()
  preflow_push(graph, routes_to_remove)
  
def parse():
  inp = sys.stdin.read().strip().split('\n')
  first_line = inp.pop(0).split()
  nbr_of_nodes, nbr_of_edges, nbr_of_students, nbr_of_routes = map(int, first_line[:4])
  graph = {}
  for i in range(nbr_of_edges):
    u, v, c = map(int, inp[i].split())
    graph.setdefault(u, []).append((v, c))
    graph.setdefault(v, []).append((u, c))
  routes_to_remove = []
  for i in range(nbr_of_edges, nbr_of_edges + nbr_of_routes):
    routes_to_remove.append(int(inp[i]))
  return graph, routes_to_remove

def preflow_push(graph, routes_to_remove):
  pass

main()