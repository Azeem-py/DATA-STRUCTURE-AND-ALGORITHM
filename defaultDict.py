from collections import defaultdict

# defaultdict is used to map multiple values to one key.

d = defaultdict(list)
c = defaultdict(set)

d['a'].append(1)
d['a'].append(2)
d['b'].append('my love')
d['b'].append('your love')
d['b'].append('our love')


c['a'].add('1')
c['a'].add('2')
c['a'].add('3')
c['a'].add('2')
print(d)
print(c)