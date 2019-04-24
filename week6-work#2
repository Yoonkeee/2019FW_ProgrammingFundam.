# 항등행렬임을 확인하는 다음 코드를 완성하시오.



def isidentity(sqmat):
    size = len(sqmat)
    for i in range(size):
        for j in range(size):
            if i == j and sqmat[i][j] != 1:
                return False
            elif i != j and sqmat[i][j] != 0:
                return False
    return True


s = [[1, 0, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 1]]
s1 = [[1, 0],
      [0, 1]]
print(isidentity(s1))
