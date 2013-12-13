from operator import *

op = {
  '+': add,
  '-': sub,
  '*': mul,
  '/': floordiv
}

while True:
  a, b, c = raw_input().split(' ')
  a, c = map(int, (a, c))
  
  if b == '?':
    break
  
  print op[b](a, c)
