while True:
  m, f, r = map(int, raw_input().split(' '))
  
  if m == f == r and m == -1:
    break
  
  if 30 > (m + f) or m == -1 or f == -1:
    print 'F'
  elif (m + f) >= 80:
    print 'A'
  elif 80 > (m + f) >= 65:
    print 'B'
  elif 65 > (m + f) >= 50 or r >= 50:
    print 'C'
  elif 50 > (m + f) >= 30:
    print 'D'
