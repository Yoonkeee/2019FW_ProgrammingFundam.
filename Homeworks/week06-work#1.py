def issymmetric(mat):
    count = 0
    size = len(mat)
    for i in range(1, size):  # size = 4
        for j in range(1, size):  # 0, 1, 2, 3
            if i == j: continue
            count += 1
            if mat[i][j] != mat[j][i]:
                return False
    print(count,"번 비교")
    return True

m0 = [[ 1, 9,  5, 11],
      [ 9, 4,  7,  3],
      [ 5, 7, -7,  8],
      [11, 3,  8,  6]]
      
      
print(issymmetric(m0))
