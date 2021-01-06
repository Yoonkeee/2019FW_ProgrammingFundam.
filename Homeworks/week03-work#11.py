def rsmult(m, n):
    sum = 0
    if n == 0:
        return 0
    else:
        while n > 1:
            if (n % 2) == 1:
                sum += m
                m = m * 2
                n = int(n / 2)
            elif (n % 2) == 0:
                m = m * 2
                n = int(n / 2)
    return m + sum


print(rsmult(57, 86))
