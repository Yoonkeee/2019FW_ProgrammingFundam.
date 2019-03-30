def rsmult1(m, n):
    def loop(m, n, a):
        if n > 1:
            if (n % 2) == 1:
                return loop(m * 2, int(n / 2), a + m)
            elif (n % 2) == 0:
                return loop(m * 2, int(n / 2), a)

        elif n == 1:
            return a + m
        # end loop()
    if n > 0:
        return loop(m, n, 0)
    else:
        return 0
        
print(rsmult1(57, 86))
