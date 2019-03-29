def fastmult0(m,n):
    if n > 0:
        if n % 2 == 0:
            return fastmult0(m * 2, n / 2)
        else:
            return m + fastmult0(m, n-1)
    else:
        return 0

print(fastmult0(2,10))
