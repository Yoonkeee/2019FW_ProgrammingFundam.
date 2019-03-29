def rsmult0(m, n):
    def loop(m, n):
        if n > 1:
            if n % 2 == 0:
                return loop(m * 2, int(n / 2))
            else:
                return m + loop(m * 2, int(n / 2))

        else:
            return m

    if n > 0:
        return loop(m, n)
    else:
        return 0

print(rsmult0(57, 86))
