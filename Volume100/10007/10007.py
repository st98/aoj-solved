while True:
  a, b = sorted(map(int, raw_input().split(' ')), key=int)
  if a == b and a == 0:
    break
  print '%d %d' % (a, b)
