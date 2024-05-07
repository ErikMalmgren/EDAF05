import sys
import math

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
 
def dist(p1, p2):
  return math.sqrt((p1.x - p2.x)*(p1.x - p2.x) + (p1.y - p2.y)*(p1.y - p2.y))
 

def main():
  n, points = parse()
  res = closest_points(n, points)
  print("%.6f" % res)
  
  
def parse():
  inp = sys.stdin.read().strip().split('\n')
  n = int(inp.pop(0))
  points = []
  for line in inp:
    x, y = map(int, line.split())
    points.append(Point(x, y))
  return n, points

def closest_points(n, points):  
  points.sort(key=lambda p: p.x)
  return closest(points, n)

def closest(points, n):
  if n <= 3:
    d = float('inf')
    for i in range(n):
      for j in range(i + 1, n):
        d = min(dist(points[i], points[j]), d)
    return d
  
  mid = n // 2
  left = points[:mid]
  right = points[mid:]
  d1 = closest(left, mid)
  d2 = closest(right, n - mid)
  d = min(d1, d2)

  sy = []
  for point in points:
    if abs(point.x - points[mid].x) <= d:
      if point not in sy:
        sy.append(point)

  sy.sort(key=lambda p: p.y)
  for i in range(len(sy)):
    for j in range(i + 1, min(len(sy), i + 3)): # i + 5 säkert alla fall
      d = min(dist(sy[j], sy[i]), d)
  return d
 
main()