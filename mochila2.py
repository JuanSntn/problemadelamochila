def knapsack(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
    keep = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
                keep[i][w] = 0
            elif wt[i-1] <= w:
                if val[i-1] + K[i-1][w-wt[i-1]] > K[i-1][w]:
                    K[i][w] = val[i-1] + K[i-1][w-wt[i-1]]
                    keep[i][w] = 1
                else:
                    K[i][w] = K[i-1][w]
                    keep[i][w] = 0
            else:
                K[i][w] = K[i-1][w]
                keep[i][w] = 0
                
    i = n
    j = W
    items = [0]*n
    while i>0 and j>0:
        if keep[i][j] == 1:
            items[i-1] = 1
            j = j-wt[i-1]
            i = i-1
        else:
            i = i-1
    print("Objetos seleccionados:", items)
    return K[n][W]

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
result=knapsack(W, wt, val, n)
print("Valor máximo obtenido: ", result)


