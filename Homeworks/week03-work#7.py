def fastmult1(m, n):
    def loop(m, n, ans):
        if n > 0:
            return loop(m, n - 1, ans + m)

        else:
            return ans
    return loop(m, n, 0)

print(fastmult1(2, 100))
