def square(n):
    def loop(n):
        if n > 0:
            return (n + n - 1) + loop(n - 1)
        else:
            return 0
     # end loop
    return loop(abs(n))

def square(n):

    def loop(n, sum):
        if n > 0:
            sum += (n + n - 1)
            return loop(n - 1, sum)
        else:
            return sum
    # end loop
    return loop(abs(n), 0)

def square(n):
    n = abs(n)
    sum = 0
    while n > 0:
        sum += n + n - 1
        n -= 1
    return sum
    
    
print(square(0)) # => 0
print(square(1)) # => 1
print(square(-2)) # => 4
print(square(3)) # => 9
print(square(-4)) # => 16
print(square(5)) # => 25
