def count_score(cards):
    score = 0
    number_of_ace = 0
    for card in cards:
        if card["rank"] == "A":
            score += 11
            number_of_ace += 1
        elif type(card["rank"]) != int:
            score += 10
        else:
            score += card["rank"]
    while (score > 21) and (number_of_ace >= 1):
        score -= 10
        number_of_ace -= 1

    return score
