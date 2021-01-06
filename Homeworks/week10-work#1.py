def input_float():
    while True:
        try:
            s = float(input('float 형식으로 입력하세요'))
        except ValueError as e:
            message = str(e)[35:]
            print(message, '는 float 형식이 아닙니다. 다시 입력하세요')
        else:
            print(s, '는 float 형식입니다.')
            break


input_float()
