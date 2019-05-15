import random


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


# ------------------- main -------------------
global chips
print('Welcome to SMaSH Casino!')
deck = fresh_deck()  # new deck 생성
dealerScore, playerScore, chips = 0, 0, 0
nextRoundBoolean = True
while nextRoundBoolean is True:  # 게임 시작
    print('-----')
    dealerCards = []  # Dealer 손패 초기화
    playerCards = []  # Player 손패 초기화
    for i in range(2):  # 카드 2장을 각자 손에 추가
        newCard, deck = hit(deck)
        dealerCards.append(newCard)
        newCard, deck = hit(deck)
        playerCards.append(newCard)
    # end for
    show_cards(dealerCards, 'My cards are:')  # 첫 패 공개
    show_cards(playerCards, 'Your cards are:')
    dealerScore = count_score(dealerCards)  # 각자 점수 계산
    playerScore = count_score(playerCards)

    if playerScore == 21:  # 첫 2장 블랙잭일경우
        if end_round('blackJackWin') is True:  # play more? y
            continue
        else: break  # play more? n

    while playerScore <= 21:  # player 플레이부분
        if more('Hit? (y/n)') is True:  # Hit? y
            newCard, deck = hit(deck)
            playerCards.append(newCard)
            playerScore = count_score(playerCards)
            print(' ', newCard['suit'], newCard['rank'])
            if is_score_bust(playerScore) is True:
                break
        else:  # Hit? n
            break  # player의 while break
    # end while
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
        nextRoundBoolean = end_round('dealerBust')
        if nextRoundBoolean is False:  # play more? n
            break
        else:
            continue  # play more? y

    if dealerScore > playerScore:  # dealer 점수 높음
        nextRoundBoolean = end_round('dealerHigher')  # while 반복조건 nextRoundBoolean 값 결정
    elif playerScore > dealerScore:  # player 점수 높음
        nextRoundBoolean = end_round('playerHigher')  # while 반복조건 nextRoundBoolean 값 결정
    elif playerScore == dealerScore:  # 무승부
        nextRoundBoolean = end_round('draw')  # while 반복조건 nextRoundBoolean 값 결정

print('Bye!')  # program execute
