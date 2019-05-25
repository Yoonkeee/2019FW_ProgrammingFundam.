class overAbsOne(Exception): pass


def input_float_one():
    while True:
        try:
            s = float(input('float 형식으로 입력하세요'))
            if abs(s) > 1:
                raise overAbsOne
        except ValueError as e:
            message = str(e)[35:]
            print(message, '는 float 형식이 아닙니다. 다시 입력하세요')
        except overAbsOne:
            print(s, '는 -1.0 ~ 1.0 범위가 아닙니다.')
        else:
            print(s, '는 -1.0 ~ 1.0 사이의 float 형식입니다.')
            break


input_float_one()
