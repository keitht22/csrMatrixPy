f = open('3elt_dual.txt', 'r')

for line in f:
    a = []
    for c in line:
        a.append(c)
    x = a[0:8]
    y = a[9:17]
    print('(' + (''.join(map(str, x))) + ')', '(' + (''.join(map(str, y))) + ')')