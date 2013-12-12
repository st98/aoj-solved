from itertools import combinations

while True:
  n, x = map(int, raw_input().split(' '))
  
  if n == x and n == 0:
    break
  
  print len(filter(
    lambda a: a == x,
    map(sum, combinations(range(1, n + 1), 3))
  ))
