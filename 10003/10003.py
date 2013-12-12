a, b = map(int, raw_input().split(' '))

if a == b:
  c = '=='
elif a > b:
  c = '>'
else:
  c = '<'

print 'a %s b' % c
