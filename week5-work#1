# 파일이름 filename과 찾을 문자열 key을 받아서 파일에서 문자열이
# 마지막으로 나타나는 위치번호를 "result.txt" 파일에 쓰는
# 프로시저 findLast를 만들어보자.
# 즉, 텍스트 파일이름이 "article.txt"이고 찾으려는 문자열이 "computer"이면,
# findLast("article.txt","computer")를 호출하고, "article.txt"에서 "computer" 가
# 마지막으로 나타나는 위치번호를 "result.txt" 파일에 쓰고, 없으면 not found를 쓴다.
# 코딩 가이드 : find 메소드를 사용하여 끝까지 key를 찾는 작업을 반복한다.
# 최근 찾은 위치 하나는 항상 기억하고 있다가 끝나면 기억해 둔 위치를 쓴다.
# (rfind 메소드 사용은 금한다.)
# 프로시저를 완성하고 다음 호출을 실행하여 확인해보자.


def findLast(filename, key):
    infile = open(filename, "r")
    outfile = open("result.txt", "w")
    text = infile.read()
    position = text.find(key)

    if position == -1:
        outfile.write(key + " is not found.\n")
    while position != -1:
        if text.find(key, position + 1) == -1:
            outfile.write(key + " is at " + str(position) + " the last time.\n")
            break
        position = text.find(key, position + 1)
    # end while
    infile.close()
    outfile.close()
# end findLast()

findLast("article.txt", "computer") # computer is at 10926 the last time.
findLast('article.txt','Whole Earth') # Whole Earth is at 11231 the last time.
findLast('article.txt','Apple') # Apple is at 6557 the last time.
findLast('article.txt','apple') # apple is not found.
