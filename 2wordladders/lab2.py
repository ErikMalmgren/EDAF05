import sys

def main():
  parse()
  print(check_if_edge('lolem', 'hello'))
  
def parse():
  inp = sys.stdin.read().split()
  N = int(inp.pop(0))
  Q = int(inp.pop(0))
  nodes = inp[:N]
  queries = inp[N:]
  return N, Q, nodes, queries

def build_graph(nodes):
  for node1 in nodes:
    for node2 in nodes:
      if node1 == node2:
        continue
      

def check_if_edge(node1, node2):
  # edge om all of the last four letters in node1 are present in node2
  four_last = node1[1:5]
  for char in four_last:
    if char not in node2:
      return False
  return True
      

main()