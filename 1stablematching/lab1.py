import sys

def main():
  students, companies = parse()
  unmatched_students = list(students)

  while len(unmatched_students) != 0:
    current_student = unmatched_students.pop()
    most_prefered_company = students.get(current_student)[0]
    
  
def parse():
  students = dict()
  companies = dict()
  N = int(next(sys.stdin))
  for idx, line in enumerate(sys.stdin):
    line = line.rstrip().split(" ")
    temp_line = [int(x) for x in line[1:]]
    if idx < N:
      students[idx +1] = temp_line
    else:
      companies[idx + 1 - N] = temp_line
  return students, companies

main()