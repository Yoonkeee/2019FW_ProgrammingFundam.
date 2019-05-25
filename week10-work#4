class negativeNumberError(Exception): pass


def calculate_comb_pascal(n, r):
    matrix = [[]] * (n - r + 1)
    matrix[0] = [1] * (r + 1)
    for i in range(1, n - r + 1):
        matrix[i] = [1]
    for i in range(1, n - r + 1):
        for j in range(1, r + 1):
            newvalue = matrix[i][j - 1] + matrix[i - 1][j]
            matrix[i].append(newvalue)
    return matrix[n - r][r]


def comb_pascal():
    while True:
        try:
            print('This program computes combination of two natural numbers, n and r.')
            print('Press Control-C to quit.')
            print('Press Enter when you are ready.')
            n = int(input('Enter n: '))
            if n < 0: raise negativeNumberError
            r = int(input('Enter r: '))
            if r < 0: raise negativeNumberError
            result = calculate_comb_pascal(n, r)
            print(n, 'C', r, ' = ', result, sep='')
        except ValueError:
            print('정수를 입력해야 합니다.')
        except IndexError:
            print('n이 r보다 커야 합니다.')
        except negativeNumberError:
            print('음수는 입력할 수 없습니다.')
        except KeyboardInterrupt:
            print('<cnrl>-C')
            break
        # end try
    # end while
    print('Goodbye!')


print(comb_pascal())
