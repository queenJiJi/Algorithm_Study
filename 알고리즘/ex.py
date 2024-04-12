v = [[1, 4], [3, 4], [3, 10]]
v1 = [[1, 1], [2, 2], [1, 2]]

x = []
y = []

for i in v:
    if i[0] in x:
        x.remove(i[0])
    else:
        x.append(i[0])
    if i[1] in y:
        y.remove(i[1])
    else:
        y.append(i[1])
print([*x, *y])
