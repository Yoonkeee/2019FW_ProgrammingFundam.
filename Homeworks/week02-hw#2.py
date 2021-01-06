#주민등록번호(Resident Registration Number)는 총 13자리의 숫자로 다음과 같은 형태로 표기한다.

#dddddd-ddddddd

#주민등록번호 검증 규칙은 다음과 같다.

#앞 부분 6자리는 생년월일을 나타낸다. 
#예를 들어, 1999년 9월 15일에 태어난 사람은 990915로, 
#2002년 1월 1일에 태어난 사람은 020101로 표기한다.
#첫 2자리의 20이상은 1900년대라고 가정하고, 20미만은 2000년대라고 가정한다.
#앞 부분 6자리는 존재하는 날짜여야 한다. (윤년 포함)
#즉, 19991315, 20020932는 틀린 번호이다.
#뒤 부분 7자리 중 첫째 자리는 성별을 나타내며 0부터 9까지 모두 쓰인다.
#뒤 부분 7자리 중 둘째 자리부터 다섯째 자리까지 4개 숫자는 출생등록지 고유번호로 지역별로 번호가 할당되어 있다. (이 문제에서는 모든 수가 고유번호로 할당되어 있다고 가정한다.)
#뒤 부분 7자리 중 여섯째 숫자는 일련번호로 신고일에 출생신고한 순서이다. 
#대부분 앞자리 수가 매겨지지만 제한은 없다.
#각 자리 숫자를 abcdef-ghijklm과 같이 표시하면, 
#마지막 숫자 m은 주민등록번호에 오류가 없는지 확인하는 검증번호로 아래 공식으로 결정한다. 
#m = 11 - ((2*a+3*b+4*c+5*d+6*e+7*f+8*g+9*h+2*i+3*j+4*k+5*l) % 11) 
#단, m 값이 10이면 0으로, 11이면 1로 표기한다.
#아래 isRRN 함수는 주민등록번호 문자열을 "dddddd-ddddddd" 형식의 인수로 받아서 
#검증하여 True 또는 False를 내주는 함수이다.
#front_ok 함수와 back_ok 함수를 작성하여 isRRN 함수를 완성하시오.

#def isRRN(s):
#    (front, mid, back) = s.partition("-")
#    return front_ok(front) and mid == "-" and back_ok(s)
############################################################################

def isleapyear(year):
    if year >= 0:
        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
    else:
        return None

def date31(date) :
    if(date == 1, 3, 5, 7, 8, 10, 12) :
        return True
    else :
        return False

def front_ok(num) :
    month = int(num[2:4])
    day = int(num[4:])
    year = int(num[:1])
    if(year >= 20) :
        year = 1900 + year
    else :
        year = 2000 + year

    if(month < 1 or month > 12 or day < 1 or day > 31) :
        return False
    if(month == 2) :
        return day <= 28 or (day == 29 and isleapyear(year))
    if(day == 31) :
        return date31(month)
def back_ok(s) :
    i = 0
    sum = 0
    s = s.partition('-')
    full = s[0] + s[2]
    while(i < 12) :
        if(i >= 8) :
            sum += (i + 4)%10 * int(full[i])
        else :
            sum += (i+2) * int(full[i])
        i += 1

    m = 11 - (sum%11)
    if(m == 10) : m = 0
    if(m == 11) : m = 1
    return m == int(full[12])

def isRRN(s):
    (front, mid, back) = s.partition("-")
    return front_ok(front) and mid == "-" and back_ok(s)

print(isRRN(input()))
