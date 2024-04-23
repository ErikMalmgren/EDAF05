import sys

def main():
  matrix, queries = parse()
  gap_score = -4
  memo = {}
  for q in queries:
    res = needleman_wunsch(matrix, q[0], q[1], gap_score, memo)
    print(res[0] + " " + res[1])
  
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

def match_score(c1, c2, gap_score, cost):
  if c1 == c2:
    return cost
  elif c1 == '*' or c2 == '*':
    return gap_score
  else:
    return -1
  
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
    
  print(string1, string2)
    
  for i in range(1, len(string2) + 1):
    for j in range(1, len(string1) + 1):
      print("i: ", i, " j: ", j, '\n')
      match = score_matrix[i - 1][j - 1] + match_score(string1[j - 1], string2[i - 1], gap_score, matrix[i][j])
      print("match_score parametrar: ", string1[j - 1], string2[i - 1], matrix[j-2][i-2])
      print("match_score värde: ", match_score(string1[j - 1], string2[i - 1], gap_score, matrix[i][j]), '\n')
      
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
    
    if score_current == score_diagonal + match_score(string1[j-1], string2[i-1], gap_score, matrix[j - 2][i - 2]):
      res1 += string1[j-1]
      res2 += string2[i-1]
      i -= 1
      j -= 1
    elif score_current == score_up + gap_score:
      res1 += string1[j-1]
      res2 += '*'
      j -= 1
    elif score_current == score_left + gap_score:
      res1 += '*'
      res2 += string2[i-1]
      i -= 1

  # Finish tracing up to the top left cell
  while j > 0:
    res1 += string1[j-1]
    res2 += '*'
    j -= 1
  while i > 0:
    res1 += '*'
    res2 += string2[i-1]
    i -= 1
    
  res1 = res1[::-1]
  res2 = res2[::-1]
    
  return(res1, res2)

  
main()