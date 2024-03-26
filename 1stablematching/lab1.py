import sys

def main():
  gs()


def gs():
  students, companies = parse()
  unmatched_students = list(students)
  matches = {}
  while unmatched_students:
    current_student = unmatched_students.pop(0)
    student_companies = students.get(current_student)

    for comp in student_companies:
      if comp not in matches:
        matches[comp] = current_student
        break
      
      if companies[comp][matches[comp]] > companies[comp][current_student]:
        unmatched_students.append(matches[comp])
        matches[comp] = current_student
        break 


  printMatches(matches)   

def printMatches(matches):
  for i in range(len(matches)):
    print(matches[i +1])


def parse():
  students = dict()
  companies = dict()
  inp = sys.stdin.read()
  inp = [int(x) for x in inp.split()]
  N =  inp.pop(0)
  
  for i in range(0, len(inp), N + 1):
    row = inp[i:i+N+1]
    index = row[0]

    if index not in companies:
      pref_list = [-1] * (N + 1) # tom lista med n + 1 platser
      idx = 0
      for s in row[1:]:
        pref_list[s] = idx
        idx += 1
      companies[index] = pref_list
    else:
      students[index] = row[1:]
  
  return students, companies  

main()