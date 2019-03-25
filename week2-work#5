#4의 배수이면 윤년인데, 그 중에서 400의 배수를 제외한 100의 배수는 평년이다
def isleapyear(year):
    if year >= 0:
        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
    else:
        return None

while True :
    print(isleapyear(int(input())))
