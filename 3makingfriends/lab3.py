import sys
import heapq

def main():
  graph = parse()
  prim(graph)

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
  queue = heapq.heapify(graph.keys())
  visited = set()
  root = queue.pop()
  
  
  
  
  
main()