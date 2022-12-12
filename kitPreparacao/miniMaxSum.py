def miniMaxSum(arr):

    soma = 0
    minnum = 999999999999999
    maxnum = 0
    for i in arr:
        soma += i
        minnum = min(minnum, i)
        maxnum = max(maxnum, i)
    print(soma - maxnum, soma - minnum)


ar = [1, 2, 3, 4, 5]
miniMaxSum(ar)










