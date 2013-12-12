while True:
  a = raw_input()
  
  if a == '0':
    break
  
  print sum(map(int, list(a)))
