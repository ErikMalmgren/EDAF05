import sys
from point2d import Point2D
import math

def main():
  people, points = parse()
  graham_scan(people, points)
  
def graham_scan(people, points):
  points.sort(key=lambda p: (p.y, p.x))
  t = Point2D(points[0])
  for point in points:
    point -= t
   
  points.sort(key=lambda p: (p.a - t.a) % (2 * math.pi))
  print(points)


def parse():
  inp = sys.stdin.read().strip().split('\n')
  people = int(inp.pop(0))
  points = []
  for line in inp:
    x, y = map(int, line.split())
    points.append(Point2D(x, y))
  return people, points

main()