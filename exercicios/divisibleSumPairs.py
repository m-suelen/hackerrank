def divisibleSumPairs(n, k, ar):

    pares = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                pares += 1
    return pares


c = 6
d = 3
arr = [1, 3, 2, 6, 1, 2]
res = divisibleSumPairs(c, d, arr)
print(res)

