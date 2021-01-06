# 정렬된 정수 리스트를 인수로 받아서 이웃한 수의 차이가 가장 큰 두 수를 찾아서
# 그 차이와 위치를 튜플로 내주는 함수 searchWidestGap을 작성하자.
# 예를 들어, 정렬된 리스트 [3,5,8,20,22]에서 차이가 가장 큰 이웃 수 8과 20이다.
# 이 경우 차이는 12이며 위치는 첫 자리의 위치번호인 2이다.
# [3,5,8,20,22,34,37,40]와 같이 동률이 있는 경우는 앞에 있는 위치번호를 선택한다.
# 리스트는 항상 정렬되어 있다고 가정한다. 실행 사례는 다음과 같다.
#
# 함수 호출	리턴
# searchWidestGap([])	(0,-1)
# searchWidestGap([3])	(0,0)
# searchWidestGap([3,5,8,20,22])	(12,2)
# searchWidestGap([3,5,8,20,22,34,37,40])	(12,2)
# 완성이 되면, 다음 테스트 함수를 호출하여 잘 작동하는지 확인해보자.



import random
def searchWidestGap(db):
    db.sort()
    i, result, j= 0, 0, 1
    
    if len(db) == 0:
        return(0,-1)
    elif len(db) == 1:
        maximum,i = 0,0
    else:
        maximum = abs(db[0] - db[1])
    for i in range(0, len(db) - 1):
        if (abs(db[i] - db[j]) > maximum):
            maximum = abs(db[i] - db[j])
            result = i
        j += 1
    return (maximum, result)
def testSearchWidestGap():
    db = random.sample(range(500),100)
    print("Searching the widest gap...")
    db.sort()
    print(db)
    index, gap = searchWidestGap(db)
    print("The widest gap is:", gap)
    print("between", db[index], "and", db[index+1])
    print("at", index)
