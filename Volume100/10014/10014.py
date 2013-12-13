import sys

while True:
  h, w = map(int, raw_input().split(' '))
  
  if h == w and h == 0:
    break
  
  for a in range(h):
    for b in range(w):
      sys.stdout.write('#.'[(a + b) % 2])
    print
  
  print
