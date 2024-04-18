import sys
from point2d import Point2D
import math
from collections import deque
import numpy as np

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
  h = deque()
  h.append(points[0])
  h.append(points[1])
  h.append(points[2])

  for k in range(3, n):
    point_t = points[k]
    while direction(h[-2], h[-1], point_t): 
      h.pop()
    h.append(point_t)
  for point in points:
    point += t
  n = len(h)
  for point in h:
    print(point)
    

def direction(p1, p2, p3):
  return (((p2.x - p1.x) * (p3.y - p1.y)) - ((p2.y - p1.y) * (p3.x - p1.x))) < 0
  
def parse():
  inp = sys.stdin.read().strip().split('\n')
  people = int(inp.pop(0))
  points = []
  for line in inp:
    x, y = map(int, line.split())
    points.append(Point2D(x, y))
  return people, points

main()