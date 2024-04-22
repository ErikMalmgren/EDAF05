import sys
from point2d import Point2D
import math
from collections import deque
import numpy as np
import matplotlib.pyplot as plt

def main():
  n, points = parse()
  # plot(points)
  res = closest_points(n, points)
  print("%.6f" % res)
  
  
def parse():
  inp = sys.stdin.read().strip().split('\n')
  n = int(inp.pop(0))
  points = []
  for line in inp:
    x, y = map(int, line.split())
    points.append(Point2D(x, y))
  return n, points

def closest_points(n, points):  
  points.sort(key=lambda p: p.x)
  return closest(points, n)
  

def closest(points, n):
  if n <= 3:
    d = float('inf')
    for i in range(n):
      for j in range(i + 1, n):
        d = min((points[i] - points[j]).r, d)
    return d
  
  mid = n // 2
  left = points[:mid]
  right = points[mid:]
  d1 = closest(left, mid)
  d2 = closest(right, n - mid)
  d = min(d1, d2)

  middle_x = points[mid].x
  sy = []
  for point in points:
    if abs(point.x - middle_x) <= d:
      if point not in sy:
        sy.append(point)

  for i in range(len(sy)):
    for j in range(i + 1, len(sy)):
      d = min((sy[j]-sy[i]).r, d)
  return d

def plot(points):
  
  x = []
  y = []
  for point in points:
    x.append(point.x)
    y.append(point.y)
  plt.plot(x, y, 'bo')
  plt.show()
 
main()