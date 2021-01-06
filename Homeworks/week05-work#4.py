def oneSentencePerLine(filename):
    infile = open(filename, "r")
    outfile = open('result.txt', "w")
    text = infile.read()
    count = 0
    newText = str  # text를 편집할 때마다 newText에 붙여주어 최신화한 뒤 '?' 판별 때 사용
    newText2 = str
    temp = str

    while True:
        text = text.partition('.')
        if text[2] == '':
            newText = str(newText) + str(text[0]) + str(text[1]) + '\n\n'  # partition한 앞문장과 '.'을 저장
            count += 1
            break

        temp = text[2]  # 문장의 첫 시작 판별을 위해 partition 후 남은 뒤의 문장들을 temp에 넣음
        if temp[0] == '\n':  # 단락의 끝이라 이미 줄바꿈이 있는 경우를 구분하여 줄바꿈 생략
            newText = str(newText) + str(text[0]) + str(text[1])
            count += 1
        else:
            newText = str(newText) + str(text[0]) + str(text[1]) + '\n\n'
            count += 1
        text = temp
        if temp[0] == ' ':  # 문장의 첫 시작이 띄어쓰기일 경우 띄어쓰기 없애기
            text = temp[1:]  # 첫글자인 띄어쓰기를 제외
        else:
            text = temp
    # end while
    text = newText  # 이미 조각조각난 text를 newText로 최신화

    while True:
        text = text.partition("?")
        if text[2] == '':  # 더이상 ?가 없을 때
            newText2 = str(newText2) + str(text[0]) + str(text[1])
            break
        temp = text[2]
        if temp[0] == '\n':
            newText2 = str(newText2) + str(text[0]) + str(text[1])
            count += 1
        else:
            newText2 = str(newText2) + str(text[0]) + str(text[1]) + '\n\n'
            count += 1
        text = text[2]
    # end while

    outfile.write(newText2[26:])
    outfile.write("There are " + str(count) + " sentences in total.\n")
    outfile.close()
    infile.close()
    print("Done")



oneSentencePerLine('article.txt')
