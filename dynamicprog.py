def coin_row(C):
    n = len(C)
    F = [0] * (n+1)
    F[0] = 0
    F[1] = C[0]

    for i in range(2,n+1):
        F[i] = max(C[i-1]+F[i-2],F[i-1])

    return F[n]

coins = [5,1,2,10,6]
result = coin_row(coins)
print("Maximum amount:",result)