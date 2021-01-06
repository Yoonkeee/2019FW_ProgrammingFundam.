# 파일이름 filename과 찾을 문자열 key를 받아서 파일에서
# 문자열이 나타나는 위치번호를 모두 "result.txt" 파일에
# 쓰는 프로시저 findAll을 만들어보자.


def findAll(filename, key):
    infile = open(filename, "r")
    outfile = open("result.txt", "w")
    text = infile.read()
    position = text.find(key)

    if position == -1:
        outfile.write(key + " is not found.\n")
    while position != -1:
        outfile.write(key + " is at " + str(position) + ".\n")
        position = text.find(key, position + 1)
    # end while
    outfile.close()
    infile.close()
# end findAll()

# findAll("article.txt", "computer")
findAll('article.txt','Whole Earth')
# findAll('article.txt','Apple')
# findAll('article.txt','apple')
