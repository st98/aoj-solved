a = {
  'S': [],
  'H': [],
  'C': [],
  'D': []
}

for _ in range(input()):
  b, c = raw_input().split(' ')
  a[b].append(int(c))

for d in 'SHCD':
  for e in range(1, 14):
    if e not in a[d]:
      print '%s %d' % (d, e)
