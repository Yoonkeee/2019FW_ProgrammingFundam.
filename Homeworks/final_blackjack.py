import random
import os
import time
import Card_Display_

def fresh_deck():
    suits = {'Spade', 'Heart', 'Diamond', 'Club'}
    ranks = {"A", '2', '3', '4', '5', '6', '7', '8', '9', '10', "J", "Q", "K"}
    deck = []
    times = 0
    while times < 2:
        for i in suits:
            for j in ranks:
                deck.append({'suit': i, 'rank': j})
        times += 1
    random.shuffle(deck)
    return deck
# end fresh_deck()


def hit(deck):
    if deck == []:
        deck = fresh_deck()
    return deck[0], deck[1:]
# end hit()


def count_score(cards):
    score = 0
    numberOfAce = 0
    for card in cards:
        if card['rank'] == 'A':
            score += 11
            numberOfAce += 1
        else:
            try:
                score += int(card['rank'])
            except ValueError:
                score += 10
    while (score > 21) and (numberOfAce >= 1):
        score -= 10
        numberOfAce -= 1

    return score
# end count_score()


def show_cards(cards, message):
    print(message)
    if message == 'My cards are:':  # dealer의 첫 패 공개일 경우
        print('  **** **')
        print(' ',cards[1].get('suit'), cards[1].get('rank'))
        return  # 함수 종료
    for card in cards:
        print(' ',card['suit'], card['rank'])
# end show_cards()


def more(message):
    print(flush=True, end='')
    answer = input(message)
    while not (answer == 'y' or answer == 'n'):
        answer = input(message)
    return True if answer == 'y' else False
# end more()


def end_round(gameResult):  # 승패에 따른 print와 chips 계산                              ★ 칩 계산 변경
    global chips  # 칩 갯수 전역변수 명시
    global playersKeepGoing
    # 승부 결과에 따른 결과 print
    if gameResult == 'blackJackWin':  # blackjack 승리                                    ★ 건 칩 1.5배
        print('Blackjack! You won.')
        while playersKeepGoing is True:  # 나는 더이상 hit 하지 않는 상황에서 다른 player들은 끝까지 play
            time.sleep(1)
            players_hit()  # ★ 다른 player들 카드표시
            do_display_cards(False) #----------------------------------------수정(인자 추가됨)------------------------------------------------------
            print('Blackjack! You won.')
        chips += 2
    elif gameResult == 'dealerBust':  # dealer bust 승리
        print('Dealer bust! You won.')
        chips += 1
    elif gameResult == 'myHigher':  # my 높은 숫자 승리
        print('You won.')
        chips += 1
    elif gameResult == 'myBust':  # my bust 패배
        chips -= 1
        while playersKeepGoing is True:  # 나는 더이상 hit 하지 않는 상황에서 다른 player들은 끝까지 play
            print('You Bust! Dealer won.')
            time.sleep(1)
            players_hit()  # ★ 다른 player들 카드표시
            do_display_cards(False) #----------------------------------------수정(인자 추가됨)------------------------------------------------------
        print('You Bust! Dealer won.')
    elif gameResult == 'dealerHigher':  # dealer 높은 숫자 승리
        print('Dealer won.')
        chips -= 1
    elif gameResult == 'draw':  # 무승부
        print('Draw.')

    print('Chips =', chips)  # chips 갯수 표시
    return more('Play more? (y/n)')  # 다음 round 진행 여부 boolean값 return
# end endRound()


def is_score_bust(score):  # 점수가 21점 초과로 bust인지 판별
    if score > 21: return True  # bust이면 return True
    else: return False  # not Bust


def store_members(members):
    file = open('members.txt', 'w')
    names = members.keys()
    for name in names:
        passwd, tries, wins, chips = members[name]
        line = name + ',' + passwd + ',' + \
               str(tries) + ',' + str(wins) + ',' + str(chips) + '\n'
        file.write(line)
    file.close()


def load_members():
    file = open("members.txt", "r")
    members = {}
    for line in file:
        name, passwd, tries, wins, chips = line.strip('\n').split(',')
        members[name] = (passwd, int(tries), float(wins), int(chips))
    file.close()
    return members


def login(members):
    username = input("Enter your name: (4 letters max) ")
    while len(username) > 4:
        username = input("Enter your name: (4 letters max) ")
    trypasswd = input("Enter your password: ")
    if username in members:
        if trypasswd == members[username][0]:
            tries = members[username][1]
            wins = int(members[username][2])
            chips = members[username][3]
            print('You played', tries,'games and won', wins, 'of them.')
            if tries > 0:
                rate = float(wins / tries) * 100
            else:
                rate = float(0)
            print('Your all-time winning percentage is {0:.1f}'.format(rate), '%')
            if chips > 0:
                print('You have', chips, 'chips.')
            else:
                print('You owe', abs(chips), 'chips.')
            return username, trypasswd, tries, wins, chips, members
        else:
            return login(members)
    else:
        members[username] = (trypasswd, 0, 0, 0)
        return username, trypasswd, 0, 0, 0, members


def show_top5(members):  # members를 받아 chips 내림차순 정렬 후 5위까지 표시
    print("-----")
    sorted_members = {}
    print("All-time Top 5 based on the number of chips earned")
    sorted_members = sorted(members.items(), key=lambda x: x[1][3], reverse=True)
    rank = 1  # 등수
    for ranker in sorted_members[:5]:
        if ranker[1][3] <= 0: break  # 칩이 0보다 작으면 더이상 print하지 않음
        print(str(rank) + '. ' + ranker[0] + ' : ' + str(ranker[1][3]))
        rank += 1
# end show_top5()  알고리즘 #17


def is_there_file(fileName):  # 파일이 있는지 검사
    return os.path.isfile(fileName)


def today_win_rate(today, tries, wins):  # 시작전 tries, wins와 게임 종료때 tries, wins를 받아옴
    beforeTries, beforeWins = today
    todayTries = tries - beforeTries  # 오늘 play한 try 수
    todayWins = wins - beforeWins  # 오늘 win 수
    if todayTries > 0:
        todayRate = float(todayWins / todayTries) * 100  # 오늘의 승률
    else:
        todayRate = float(0)
    print('You played', todayTries, 'games and won', todayWins, 'of them.')
    print('Your winning percentage today is {0:.1f}'.format(todayRate), '%')
# end today_win_rate()  알고리즘 #16


def players_hit():
    global p0score, p1score, p2score, p0cards, p1cards, p2cards, deck, playersKeepGoing
    keepGoing = [True, True, True]

    if p0score <= 15:  # 15 이하면 hit
        newCard, deck = hit(deck)
        p0cards.append(newCard)
        p0score = count_score(p0cards)
    else:
        keepGoing[0] = False  # 더이상 hit 하지 않음

    if p1score <= 17:  # 17 이하면 hit
        newCard, deck = hit(deck)
        p1cards.append(newCard)
        p1score = count_score(p1cards)
    else:
        keepGoing[1] = False  # 더이상 hit 하지 않음

    if p2score <= 18:  # 18 이하면 hit
        newCard, deck = hit(deck)
        p2cards.append(newCard)
        p2score = count_score(p2cards)
    else:
        keepGoing[2] = False  # 더이상 hit 하지 않음

    playersKeepGoing = keepGoing[0] or keepGoing[1] or keepGoing[2]


def do_display_cards(turn):#----------------------------------------수정(인자 turn 추가됨)------------------------------------------------------
    global p0cards, p1cards, p2cards, dealerCards, myCards
    playerScores, allCards = [], []
    allCards += dealerCards, p0cards, p1cards, p2cards, myCards
    os.system('cls')
    playerScores.append(count_score(dealerCards))
    playerScores.append(count_score(p0cards))
    playerScores.append(count_score(p1cards))
    playerScores.append(count_score(p2cards))
    Card_Display_.CardDisplay(allCards, turn, playerScores)




# ------------------- main -------------------
def main_game():
    global chips                                                                                  # ★  chips
    global p0score, p1score, p2score, p0cards, p1cards, p2cards, players, playersKeepGoing, dealerCards, myCards, deck
    playersKeepGoing = True
    print('Welcome to SMaSH Casino!')
    if is_there_file('members.txt') is False:  # members.txt 파일이 있는지 검사
        store_members({})  # members.txt 파일이 없으면 생성
    username, passwd, tries, wins, chips, members = login(load_members())  # 알고리즘 #2
    beforePlayGame = [tries, wins]  # 오늘의 게임 승률 계산을 위해 시작값 저장
    deck = fresh_deck()  # new deck 생성
    dealerScore, myScore = 0, 0
    nextRoundBoolean = True

    while nextRoundBoolean is True:  # 게임 시작
        tries += 1  # 한 판씩 할 때마다 tries 증가
        playersKeepGoing = True
        print('-----')
        dealerCards = []  # Dealer 손패 초기화
        myCards = []  # my 손패 초기화
        p0cards, p1cards, p2cards = [], [], []
        players, allCards = [], []
        players += p0cards, p1cards, p2cards  # player 0, 1, 2 덱을 players에 이중 리스트로 구조화

        for i in range(2):  # 카드 2장을 각자 손에 추가
            newCard, deck = hit(deck)
            dealerCards.append(newCard)
            newCard, deck = hit(deck)
            myCards.append(newCard)
            for p in players:
                newCard, deck = hit(deck)
                p.append(newCard)
        # end for  첫 카드 추가 종료
        # show_cards(dealerCards, 'My cards are:')  # dealer 첫 패 공개                             ★
        # show_cards(myCards, 'Your cards are:')  # my 첫 패 공개                                   ★
        dealerScore = count_score(dealerCards)  # 각자 점수 계산
        myScore = count_score(myCards)
        p0score = count_score(p0cards)
        p1score = count_score(p1cards)
        p2score = count_score(p2cards)
        do_display_cards(True) #----------------------------------------수정(인자 추가됨)------------------------------------------------------


        if myScore == 21:  # 첫 2장 블랙잭일경우
            wins += 1
            if end_round('blackJackWin') is True:  # play more? y
                continue  # 블랙잭으로 이기고 게임을 더 할 경우 바로 while 반복
            else: break  # play more? n

        while myScore <= 21:  # my 플레이부분
            if more('Hit? (y/n)') is True:  # Hit? y
                newCard, deck = hit(deck)
                myCards.append(newCard)  # my 카드 추가
                myScore = count_score(myCards)  # my 점수 계산                                      ★
                players_hit()
                do_display_cards(True) #----------------------------------------수정(인자 추가됨)------------------------------------------------------
                # print(' ', newCard['suit'], newCard['rank'])  # 방금 나온 카드 표시               ★
                if is_score_bust(myScore) is True:  # my의 bust 감시
                    break  # bust시 my 플레이부분 while 탈출
            else:  # Hit? n
                while playersKeepGoing is True:  # 나는 더이상 hit 하지 않는 상황에서 다른 player들은 끝까지 play
                    time.sleep(1)
                    players_hit()                                                                 # ★ 다른 player들 카드표시
                    do_display_cards(False) #----------------------------------------수정(인자 추가돰)------------------------------------------------------
                break  # my의 while break
        # end while  my 플레이부분
        if myScore > 21:  # my bust이면 바로 패배
            if end_round('myBust') is True:
                continue  # play more? y
            else:
                break  # play more? n

        while dealerScore < 22:  # dealer 플레이부분
            if dealerScore <= 16:  # 16 이하면 hit
                time.sleep(1)
                newCard, deck = hit(deck)
                dealerCards.append(newCard)
                dealerScore = count_score(dealerCards)
                do_display_cards(False) #----------------------------------------수정(인자 추가됨)------------------------------------------------------
            else:  # 16 초과
                break
        # end while
        # show_cards(dealerCards,'My cards are: ')  # dealer 카드 공개                              ★
        if dealerScore > 21:  # dealer bust일 경우
            do_display_cards(False)#----------------------------------------수정(인자 추가됨)------------------------------------------------------
            nextRoundBoolean = end_round('dealerBust')  # dealer bust로 승리
            wins += 1
            if nextRoundBoolean is False:  # play more? n
                break
            else:
                continue  # play more? y

        if dealerScore > myScore:  # dealer 점수 높음 패배
            nextRoundBoolean = end_round('dealerHigher')  # while 반복조건 nextRoundBoolean 값 결정
        elif myScore > dealerScore:  # my 점수 높음 승리
            nextRoundBoolean = end_round('myHigher')  # while 반복조건 nextRoundBoolean 값 결정
            wins += 1
        elif myScore == dealerScore:  # 무승부
            nextRoundBoolean = end_round('draw')  # while 반복조건 nextRoundBoolean 값 결정

    members[username] = (passwd, tries, wins, chips)  # members에 최신화
    store_members(members)  # 알고리즘 #15
    today_win_rate(beforePlayGame, tries, wins)  # 알고리즘 #16
    show_top5(members)  # 알고리즘 #17
    print('Bye!')  # program execute

main_game()

# 다른플레이어 구현 완료
# 덱 2개로 추가, player 구분 위해 기존 player -> my 로 대치

'''
현재 문제점
0. player2 ( Card_Display 상으론 player3, 제일 오른쪽 ) player 카드추가 안됨. out of index 에러
1. my ( Card_Display 상으론 player ) 카드 추가 제대로 안됨
1-1. my card hit하면 새로 받은 카드가 2번째로 오게 됨
'''

'''
고친점, 고쳐야할점
0. CardDisplay 함수에 myTurn 인자가 추가됨
0-1. do_display_cards 함수에도 turn 인자를 추가해야함
1. 딜러의 패를 공개하는 상황에서 myTurn의 값을 False로 변경해주어야함
'''

# A. 칩 디스플레이     난이도 중간
# B. 현재 점수(플레이어) 표시    난이도 쉬움
# C. 각 hit마다 칩 걸기   난이도 중간  time.sleap(secs) , os.system('cls') 활용해서 줄거나 늘어날 때 애니메이션 효과 추가
# D. 떠블다운    난이도 쉬움
# E. 칩 계산 변경   난이도 쉬움


# 시연동영상, 알고리즘 순서도 ( 흐름 차트 )   = 발표 준비
