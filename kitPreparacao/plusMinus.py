def plusMinus(arr):

    pos = neg = zero = 0
    size = len(arr)
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1
    print(pos / size)
    print(neg / size)
    print(zero / size)


ar = [-4, 3, -9, 0, 4, 1]
plusMinus(ar)


