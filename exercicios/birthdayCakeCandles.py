def birthdayCakeCandles(candles):

    n = len(candles)
    maior = 0
    soma = 0
    for i in range(n):
        if candles[i] > maior:
            maior = candles[i]
            soma = 1
        elif candles[i] == maior:
            soma += 1
    return soma


arr = [3, 2, 1, 3]
res = birthdayCakeCandles(arr)
print(res)
