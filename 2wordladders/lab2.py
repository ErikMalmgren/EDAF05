import sys

def main():
  nodes, queries = parse()
  graph = build_graph(nodes)
  print(graph)
  for i in range(0, len(queries), 2):
    starting_word = queries[i:i+1][0]
    ending_word = queries[i+1:i+2][0]
    print(bfs(graph, starting_word, ending_word))
  
  
def bfs(graph, starting_word, ending_word):
  if starting_word == ending_word:
    return 0
  queue = []
  queue.append(starting_word)
  visited = set()
  visited.add(starting_word)
  distance = 1
  while len(queue) != 0:
    v = queue.pop(0)
    for neighbor in graph[v]:
      print(neighbor)
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append(neighbor)
      if neighbor == ending_word:
        # print(neighbor, ending_word)
        return(distance)
    distance += 1
    print("--------------")

  return("Impossible")   
    
def parse():
  inp = sys.stdin.read().split()
  N = int(inp.pop(0))
  Q = int(inp.pop(0))
  nodes = inp[:N]
  queries = inp[N:]
  return nodes, queries

def build_graph(nodes):
  graph = {}
  for node1 in nodes:
    graph[node1] = []
    for node2 in nodes:
      if node1 == node2:
        continue
      if check_if_edge(node1, node2):
        graph[node1].append(node2)
  return graph
      

def check_if_edge(node1, node2):
  # edge om all of the last four letters in node1 are present in node2
  four_last = node1[-4:]
  for char in four_last:
    if node2.count(char) < four_last.count(char):
      return False
  return True
      

main()