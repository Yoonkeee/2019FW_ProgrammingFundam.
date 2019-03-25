def monthlypaymentplan(principal, interest, year):
    interest = float(interest / 100)
    monthlyRate = interest / 12
    month = year * 12
    return int(( ((1+monthlyRate) ** month) * principal * monthlyRate ) / ( ((1 + monthlyRate) ** month) -1 ))
    

print(monthlypaymentplan(10000000, 2.8, 4))
# should print 220460
