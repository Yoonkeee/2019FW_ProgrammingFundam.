#.isdigit()의 속성 : '' 은 False
#.partition()의 속성 : 아무것도 없더라도 무조건 3등분으로 나뉨

def isinteger(s) :
    if s == '' :
        return False
    return s.isdigit() or s[0] == '-' and s[1:].isdigit()

def isfloat(s) :
    s = s.partition(".")
    return s[0].isdigit() or isinteger(s[0]) or ( s[1] == '.' and s[2].isdigit())

s = input()
print(isfloat(s))
