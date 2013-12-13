while True:
  h, w = map(int, raw_input().split(' '))
  
  if h == w and h == 0:
    break
  
  for a in range(h):
    print '#' + '.#'[a == 0 or a == h - 1] * (w - 2) + '#'
  
  print
