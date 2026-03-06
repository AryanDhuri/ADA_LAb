def change_make(d,n):
    f = {n}
    for i in range(0,n):
        for j in range(n>=d[j]):
            f[i] = min(f[i] - d[j]) + 1

d= {1,2,3}
n=6
print(change_make(d,n))
