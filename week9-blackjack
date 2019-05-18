import random
import os

def fresh_deck():
    suits = {'Spade', 'Heart', 'Diamond', 'Club'}
    ranks = {'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
    deck = []
    for i in suits:
        for j in ranks:
            deck.append({'suit': i, 'rank': j})
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
        elif type(card['rank']) != int:
            score += 10
        else:
            score += card['rank']
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
    answer = input(message)
    while not (answer == 'y' or answer == 'n'):
        answer = input(message)
    return True if answer == 'y' else False
# end more()


def end_round(gameResult):  # 승패에 따른 print와 chips 계산
    global chips  # 칩 갯수 전역변수 명시
    # 승부 결과에 따른 결과 print
    if gameResult == 'blackJackWin':  # blackjack 승리
        print('Blackjack! You won.')
        chips += 2
    elif gameResult == 'dealerBust':  # dealer bust 승리
        print('I bust! You won.')
        chips += 1
    elif gameResult == 'playerHigher':  # player 높은 숫자 승리
        print('You won.')
        chips += 1
    elif gameResult == 'playerBust':  # player bust 패배
        chips -= 1
        print('You Bust! I won.')
    elif gameResult == 'dealerHigher':  # dealer 높은 숫자 승리
        print('I won.')
        chips -= 1
    elif gameResult == 'draw':  # 무승부
        print('We draw.')

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


# ------------------- main -------------------
global chips
print('Welcome to SMaSH Casino!')
if is_there_file('members.txt') is False:  # members.txt 파일이 있는지 검사
    store_members({})  # members.txt 파일이 없으면 생성
username, passwd, tries, wins, chips, members = login(load_members())
beforePlayGame = [tries, wins]  # 오늘의 게임 승률 계산을 위해 시작값 저장
deck = fresh_deck()  # new deck 생성
dealerScore, playerScore = 0, 0
nextRoundBoolean = True
while nextRoundBoolean is True:  # 게임 시작
    tries += 1  # 한 판씩 할 때마다 tries 증가
    print('-----')
    dealerCards = []  # Dealer 손패 초기화
    playerCards = []  # Player 손패 초기화
    for i in range(2):  # 카드 2장을 각자 손에 추가
        newCard, deck = hit(deck)
        dealerCards.append(newCard)
        newCard, deck = hit(deck)
        playerCards.append(newCard)
    # end for  첫 카드 추가 종료
    show_cards(dealerCards, 'My cards are:')  # dealer 첫 패 공개
    show_cards(playerCards, 'Your cards are:')  # player 첫 패 공개
    dealerScore = count_score(dealerCards)  # 각자 점수 계산
    playerScore = count_score(playerCards)

    if playerScore == 21:  # 첫 2장 블랙잭일경우
        wins += 1
        if end_round('blackJackWin') is True:  # play more? y
            continue  # 블랙잭으로 이기고 게임을 더 할 경우 바로 while 반복
        else: break  # play more? n

    while playerScore <= 21:  # player 플레이부분
        if more('Hit? (y/n)') is True:  # Hit? y
            newCard, deck = hit(deck)
            playerCards.append(newCard)  # player 카드 추가
            playerScore = count_score(playerCards)  # player 점수 계산
            print(' ', newCard['suit'], newCard['rank'])  # 방금 나온 카드 표시
            if is_score_bust(playerScore) is True:  # player의 bust 감시
                break  # bust시 player 플레이부분 while 탈출
        else:  # Hit? n
            break  # player의 while break
    # end while  player 플레이부분
    if playerScore > 21:  # player bust이면 바로 패배
        if end_round('playerBust') is True:
            continue  # play more? y
        else:
            break  # play more? n

    while dealerScore < 22:  # dealer 플레이부분
        if dealerScore <= 16:  # 16 이하면 hit
            newCard, deck = hit(deck)
            dealerCards.append(newCard)
            dealerScore = count_score(dealerCards)
        else:  # 16 초과
            break
    # end while
    show_cards(dealerCards,'My cards are: ')  # dealer 카드 공개
    if dealerScore > 21:  # dealer bust일 경우
        nextRoundBoolean = end_round('dealerBust')  # dealer bust로 승리
        wins += 1
        if nextRoundBoolean is False:  # play more? n
            break
        else:
            continue  # play more? y

    if dealerScore > playerScore:  # dealer 점수 높음 패배
        nextRoundBoolean = end_round('dealerHigher')  # while 반복조건 nextRoundBoolean 값 결정
    elif playerScore > dealerScore:  # player 점수 높음 승리
        nextRoundBoolean = end_round('playerHigher')  # while 반복조건 nextRoundBoolean 값 결정
        wins += 1
    elif playerScore == dealerScore:  # 무승부
        nextRoundBoolean = end_round('draw')  # while 반복조건 nextRoundBoolean 값 결정

members[username] = (passwd, tries, wins, chips)  # members에 최신화
store_members(members)  # 알고리즘 #15
today_win_rate(beforePlayGame, tries, wins)  # 알고리즘 #16
show_top5(members)  # 알고리즘 #17
print('Bye!')  # program execute
