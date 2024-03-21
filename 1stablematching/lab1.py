import sys
import time

def main():
  t1 = time.time()
  gs()
  print(time.time() - t1)


def gs():
  students, companies = parse()


  #print("Students", students)
  # print(companies)
  unmatched_students = list(students)
  matches = {}
  while unmatched_students:
    # print("unmatched students: ", unmatched_students)
    # print("matches: ", matches)
    current_student = unmatched_students.pop(0)
    # print("current student: ", current_student)
    student_companies = students.get(current_student)
    # print("student's companies: ", student_companies)

    for comp in student_companies:
      #print("Company list:", comp, " ", companies[comp])
      #print(comp not in matches)
      if comp not in matches:
        matches[comp] = current_student
        break

      #print("nuvarande match:" , companies[comp].index(matches[comp]))
      #print("potentiell match: ", companies[comp].index(current_student))
      if companies[comp].index(matches[comp]) > companies[comp].index(current_student):
        # print("comp ", matches[comp])
        unmatched_students.append(matches[comp])
        matches[comp] = current_student
        
        break
    
    if current_student not in matches.values():
      unmatched_students.append(current_student)
    #print("slut", matches)
    #print("----------------")

  printMatches(matches)   

def printMatches(matches):
  #print(matches)
  for i in range(len(matches)):
    print(matches[i +1])



def parse():
  students = dict()
  companies = dict()
  inp = sys.stdin.read()
  inp = [int(x) for x in inp.split()]
  N = inp[0]
  inp.pop(0)
  
  for i in range(0, len(inp), N + 1):
    row = inp[i:i+N+1]
    index = row[0]

    if index not in companies:
      companies[index] = row[1:]
    else:
      students[index] = row[1:]  
  return students, companies  

main()
