def findAllSentences(filename,key) :
    infile = open(filename,"r", encoding='utf-8')
    outfile = open("result.txt","w", encoding='utf-8')
    text = infile.read()
    count, total, senCount = 0, 0, 0

    while text != '':
        (sentence, sign, text) = textPartition(text)
        sentence = sentence.strip(' \n')
        i = sentence.find(key)
        count = 0
        while i != -1:
            count += 1
            i = sentence.find(key, i + 1)
        if count > 0:
            total += count
            outfile.write("'" + key + "' appears " + str(count) + " time.\n")
            outfile.write(sentence + sign + '\n\n' )
            senCount += 1
    outfile.write("'" + key + "' appears " + str(senCount) + " times in " + str(total) + " sentences.")
    outfile.close()
    infile.close()
    print("done")
def textPartition(text):
    dot = text.find('.')
    qst = text.find('?')
    if dot == qst == -1:
        return (text, '', '')
    elif dot == -1:
        return text.partition('?')
    elif qst == -1:
        return text.partition('.')
    elif qst < dot:
        return text.partition('?')
    else:
        return text.partition('.')


findAllSentences('article.txt', 'computer')
