# 미완성 코드

def issudoku(mat):
    n = len(mat)
    oneDimentionArray = []
    compareArray = []

    for i in range(n):
        for j in range(n):
            index = (i * n) + j + 1
            oneDimentionArray.append(mat[i][j])
            compareArray.append(index)
    oneDimentionArray.sort()
    print(compareArray)

    return issame(compareArray, oneDimentionArray, n)

def issame(comA, oneA, n):
    for i in range(n):
        if comA[i] != oneA[i]:
            return False
    return True




s = [[5,3,4],[6,7,2],[1,9,8]]
s1 = []
print(issudoku(s))
