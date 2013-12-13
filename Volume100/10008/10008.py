a, b = map(int, raw_input().split(' '))
print '%d %d %f' % (divmod(a, b) + (float(a) / b,))
