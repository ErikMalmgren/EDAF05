import sys

def main():
  students, companies = parse()
  print(students)
  print(companies)
  
def parse():
  students = []
  companies = []
  N = int(next(sys.stdin))
  for idx, line in enumerate(sys.stdin):
    tempLine = [int(x) for x in line.rstrip().split()]
    if idx < N:
        students.append(tempLine)
    else:
      companies.append(tempLine)
  return students, companies

main()