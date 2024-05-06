import sys

class Edge:
  def  __init__(self, node1, node2, capacity):
    self.node1 = node1
    self.node2 = node2
    self.capacity = capacity
    self.flow = 0
    self.activated = False
  
  def __str__(self):
    return "Node1: {} Node2: {} capacity: {} flow: {} activated: {}".format(self.node1.label, self.node2.label, self.capacity, self.flow, self.activated)
    
class Node:
  def __init__(self, label):
    self.label = label
    self.height = 0
    self.edges = []

  def __str__(self):
    return "Node: {}, Height: {}".format(self.label, self.height)

def main():
  edges, nodes, routes_to_remove = parse()
  preflow_push(edges, nodes, routes_to_remove)
  
def parse():
  inp = sys.stdin.read().strip().split('\n')
  first_line = inp.pop(0).split()
  nbr_of_nodes, nbr_of_edges, nbr_of_students, nbr_of_routes = map(int, first_line[:4])
  edges = []
  nodes = []
  for i in range(nbr_of_edges):
    u, v, c = map(int, inp[i].split())
    node1 = Node(u)
    node2 = Node(v)
    edge = Edge(node1, node2, c)
    node1.edges.append(edge)
    node2.edges.append(edge)
    edges.append(edge)
    if node1.label not in [node.label for node in nodes]:
      nodes.append(node1)
    if node2.label not in [node.label for node in nodes]:
      nodes.append(node2)
  routes_to_remove = []
  for i in range(nbr_of_edges, nbr_of_edges + nbr_of_routes):
    routes_to_remove.append(int(inp[i]))
  return edges, nodes, routes_to_remove

def preflow_push(edges, nodes, routes_to_remove):
  edges[0].flow = edges[0].capacity

  nodes[0].height = len(nodes)
  for node in nodes[:1]:
    node.height = 0

  for edge in nodes[0].edges:
    edge.flow = edge.capacity

  for edge in edges:
    if edge.node1.label != nodes[0].label and edge.node2.label != nodes[0].label:
      edge.flow = 0

  nodes_with_positive_ef = [node for node in nodes[:-1] if ef(node) > 0]

  while nodes_with_positive_ef:
    v = nodes_with_positive_ef.pop(0)
    for edge in nodes.edges:
      w = edge.node2
      if v.height > w.height:
        push(edge)
      else:
        relabel()
    
    nodes_with_positive_ef = [node for node in nodes[:-1] if ef(node) > 0]
  
  return 0
  

def push(edge):
  
  

def relabel(h, f, v):
  
      
def ef(node):
  sum = 0
  for edge in node.edges:
    if edge.node1 == node:
      sum -= edge.flow
    else:
      sum += edge.flow
  return sum

  
  

main()