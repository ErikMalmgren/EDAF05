import sys

def main():
  gs()
  

def gs():
  students, companies = parse2()
  unmatched_students = list(students)
  matches = {}

  while unmatched_students:
    current_student = unmatched_students.pop()
    student_companies = students.get(current_student)
    print("student: ", current_student)
    print("stud comps: ", student_companies)

    for comp in student_companies:
      if current_student not in matches.values():
        matches[comp] = current_student
        break

      elif companies[comp].index(matches[comp]) < companies[comp].index(current_student):
        unmatched_students.append(matches[comp])
        matches[comp] = current_student
    
    if current_student not in matches: 
      unmatched_students.append(current_student)
    print("matches ", matches) 

  printMatches(matches)   

def printMatches(matches):
  print(matches)
  for i in range(len(matches)):
    print(matches[i +1])


    
  
def parse():
  students = dict()
  companies = dict()
  inp = sys.stdin
  print(inp)
  N = int(next(sys.stdin))
  for idx, line in enumerate(sys.stdin):
    line = line.rstrip().split(" ")
    temp_line = [int(x) for x in line[1:]]
    if idx < N:
      students[idx +1] = temp_line
    else:
      companies[idx + 1 - N] = temp_line
  print(students)
  print(companies)
  return students, companies

  
def parse2():
  students = dict()
  companies = dict()
  inp = sys.stdin.read()
  N = int(inp[0])
  char_idx = 0
  for char in inp[1:]:
    if char.isdigit():
      if char_idx == 0:
        preferences = []
        stu_comp = int(char)
      else:
        preferences.append(int(char))
      char_idx += 1
      if char_idx == N +1:
        if stu_comp not in students:
          students[stu_comp] = preferences
        else:
          companies[stu_comp] = preferences
        char_idx = 0

  return students, companies

main()
