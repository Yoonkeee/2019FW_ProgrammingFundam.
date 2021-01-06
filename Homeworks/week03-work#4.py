def mult1(m,n):
    def loop(m, n, ans):

        if n > 0:
            return loop(m, n - 1, m + ans)
        else:
            return ans
    return loop(m, n, 0)
