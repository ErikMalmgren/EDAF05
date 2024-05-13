import sys
import time

class Edge:
  def  __init__(self, node1, node2, capacity):
    self.node1 = node1
    self.node2 = node2
    self.capacity = capacity
    self.flow = 0
    self.activated = False
  
  def __repr__(self):
    return "Node1: {} Node2: {} capacity: {} flow: {} activated: {}".format(self.node1.label, self.node2.label, self.capacity, self.flow, self.activated)
    
class Node:
  def __init__(self, label):
    self.label = label
    self.height = 0
    self.edges = []

  def __repr__(self):
    return "Node: {}, Height: {}".format(self.label, self.height)

def main():
  edges, nodes, routes_to_remove = parse()
  print(preflow_push(edges, nodes, routes_to_remove))
  
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
    for i in range(len(nodes)):
      if nodes[i].label == u:
        node1 = nodes[i]
      if nodes[i].label == v:
        node2 = nodes[i]
        
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
  nodes.sort(key=lambda n: n.label)
  return edges, nodes, routes_to_remove

def preflow_push(edges, nodes, routes_to_remove):
  nodes[0].height = len(nodes)
  for node in nodes[1:]:
    node.height = 0

  for edge in nodes[0].edges:
    edge.flow = edge.capacity
  for edge in edges:
    if edge.node1.label != nodes[0].label and edge.node2.label != nodes[0].label:
      edge.flow = 0
  
  p = 0
  node_list = nodes[1:-1]
  while p < len(node_list):
    u = node_list[p]
    old_height = u.height
    discharge(u)
    if u.height > old_height:
      node_list.insert(0, node_list.pop(p))
      p = 0
    else:
      p += 1

  res = 0
  for edge in nodes[0].edges:
    res += edge.flow
  return sum([edge.flow for edge in nodes[0].edges])


def discharge(node):
  n = len(node.edges)
  i = 0
  print(node)
  while ef(node) > 0:
    time.sleep(1)
    print("i och n,", i, n)
    edge = node.edges[i]
    if edge.node1.label == node.label:
      v = edge.node2
    else:
      v = edge.node1
    if edge.capacity - edge.flow > 0 and node.height > v.height:
      push(node, v, edge)
    else:
      i += 1
    if i == n:
      relabel(node)
      i = 0
      
    

  

def push(v, w, edge):
  print("I push:", edge)
  if edge.node1.label == v.label:
    delta = min(ef(v), edge.capacity - edge.flow)
    edge.flow += delta
    if abs(edge.flow) > edge.capacity:
      edge.flow = edge.capacity
      print("edge.flow oka", edge.flow)
  else: 
    delta = min(ef(v), edge.flow)
    edge.flow -= delta
    if abs(edge.flow) > edge.capacity:
      edge.flow = -edge.capacity
      print("edge.flow minska", edge.flow)
  print("Kant efter push:", edge)
  print("ef for v", ef(v))
  print("--------------")

def relabel(v):
  v.height += 1
      
def ef(node):
  sum = 0
  for edge in node.edges:
    if node.label == edge.node1.label:
      sum -= edge.flow
    else:
      sum += edge.flow
  return sum
  

main()