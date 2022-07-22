n = int(input())
m = 0
c = 0
r = list(map(int, input().split(' ')))
for i in range(n):
    if m < res[i]:
        m = res[i]
for i in range(n):
    if m == res[i]:
        c = c+1
print(c)