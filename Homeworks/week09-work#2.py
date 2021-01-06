def show_top5(members):
    print("-----")
    sorted_members = {}  # 칩의 개수 역순으로 정렬
    print("All-time Top 5 based on the number of chips earned")
    sorted_members = sorted(members.items(), key=lambda x: x[1][3], reverse=True)
    rank = 1
    for ranker in sorted_members[:5]:
        if ranker[1][3] <= 0: break
        print(str(rank) + '. ' + ranker[0] + ' : ' + str(ranker[1][3]))
        rank += 1
