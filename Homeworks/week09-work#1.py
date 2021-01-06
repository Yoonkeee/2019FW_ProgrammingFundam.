def login(members):
    username = input("Enter your name: (4 letters max) ")
    while len(username) > 4:
        username = input("Enter your name: (4 letters max) ")
    trypasswd = input("Enter your password: ")
    if username in members:
        if trypasswd == members[username][0]:
            print(members[username])
            tries = members[username][1]
            wins = members[username][2]
            chips = members[username][3]
            print('You played', tries,'games and won', wins,'of them.')
            # username의 게임시도 횟수와 이긴 횟수를 members에서 가져와 보여준다.
            # 예시: You played 101 games and won 54 of them.
            if tries > 0:
                rate = float(wins / tries) * 100
            else:
                rate = float(0)
            print('Your all-time winning percentage is {0:.1f}'.format(rate), '%')
            if chips > 0:
                print('You have', chips, 'chips.')
            else:
                print('You owe', chips, 'chips.')
            # 승률 계산하여 %로 보여줌 (분모가 0인 오류 방지해야 함)
            # 예시: Your all-time winning percentage is 53.5 %
            # 칩 보유개수를 보여줌
            # 예시 : 개수가 양수이면 You have 5 chips.
            # 예시 : 개수가 음수이면 You owe 5 chips.
            return username, tries, wins, chips, members
        else:
            return login(members)
    else:
        members[username] = (trypasswd, 0, 0, 0)
        # username을 members 사전에 추가한다.
        return username, 0, 0, 0, members
