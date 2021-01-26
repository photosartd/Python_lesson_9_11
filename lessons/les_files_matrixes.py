n = int(input())
t = [[0]]
print(t)
for i in range(1, n):
    t.append([int(x) for x in input().split()])
    print(t)
    for j in range(i):
        t[j].append(t[i][j])
    t[i].append(0)
for row in t:
    print(' '.join(str(x) for x in row))