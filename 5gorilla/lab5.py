import sys

def main():
  matrix, queries = parse()
  gap_score = 4
  for q in queries:
    needleman_wunsch(matrix, q[0], q[1], -4)
  
def parse():
  inp = sys.stdin.read().strip().split('\n')
  alphabet = inp.pop(0).split()
  matrix = []
  for _ in inp[:len(alphabet)]:
    matrix.append(list(map(int, inp.pop(0).split())))
  num_queries = inp.pop(0)
  queries = []
  for q in inp:
    queries.append(q.split())
  return matrix, queries

def needleman_wunsch(matrix, string1, string2, gap_score):
  

  
main()