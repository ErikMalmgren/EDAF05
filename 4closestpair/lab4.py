import sys
from point2d import Point2D
import math

def main():
  people, points = parse()
  graham_scan(people, points)
  
def graham_scan(n, points):
  points.sort(key=lambda p: (p.y, p.x)) ## TODO sortera inte här
  t = Point2D(points[0]) 
  for point in points:
    point -= t
   
  points.sort(key=lambda p: (p.a - t.a) % (2 * math.pi))
  # print(points)
  h = []
  h.push(points[0])
  h.push(points[1])
  h.push(points[2])

  for k in range(3, n):
    points[k]


def parse():
  inp = sys.stdin.read().strip().split('\n')
  people = int(inp.pop(0))
  points = []
  for line in inp:
    x, y = map(int, line.split())
    points.append(Point2D(x, y))
  return people, points

main()