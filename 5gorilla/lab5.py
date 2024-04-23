import sys

def main():
  matrix, queries = parse()
  gap_score = 4
  memo = {}
  for q in queries:
    needleman_wunsch(matrix, q[0], q[1], -4, memo)
  
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

def match_score(c1, c2, gap_score):
  if c1 == c2:
    return 1
  else:
    return gap_score

def print_matrix(mat):
    for i in range(0, len(mat)):
        print("[", end = "")
        for j in range(0, len(mat[i])):
            print(mat[i][j], end = "")
            if j != len(mat[i]) - 1:
                print("\t", end = "")
        print("]\n")


  
def create_score_matrix(matrix, string1, string2, gap_score):
  score_matrix = []
  for i in range(len(string2) +1):
    l = []
    for j in range(len(string1) +1):
      l.append(0)
    score_matrix.append(l)
    
  for i in range(len(string2) + 1):
    score_matrix[i][0] = gap_score * i
    
  for j in range(len(string1) + 1):
    score_matrix[0][j] = gap_score * j
    
  for i in range(1, len(string2) + 1):
    for j in range(1, len(string1) + 1):
      match = score_matrix[i - 1][j - 1] + match_score(string1[j - 1], string2[i - 1], gap_score)
      insert = score_matrix[i][j - 1] + gap_score
      delete = score_matrix[i - 1][j] + gap_score
      score_matrix[i][j] = max(match, insert, delete)
      
  return score_matrix

def needleman_wunsch(matrix, string1, string2, gap_score, memo):
  # if (string1, string2) in memo:
    # return memo[(string1, string2)]
  score = create_score_matrix(matrix, string1, string2, gap_score)
  res1 = ''
  res2 = ''
  i = len(string2)
  j = len(string1)  
  
  while i > 0 and j > 0:
    score_current = score[i][j]
    score_diagonal = score[i-1][j-1]
    score_up = score[i][j-1]       
    score_left = score[i-1][j]

  
main()