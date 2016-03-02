balance = 5000
annualInterestRate = 0.18

lowerBound = balance / 12
upperBound = (balance * (1 + (annualInterestRate/12)**12)) / 12
lowestPaymentFound = False
payment = lowerBound

while (not lowestPaymentFound):
    testBalance = balance
    for i in range(12):
        testBalance -= payment
        interest = testBalance * (annualInterestRate / 12)
        testBalance += interest
    if abs(testBalance) < 0.01:
        lowestPaymentFound = True
    else:
        payment += (testBalance / 12)
    print 'testBalance = ' + str(round(testBalance, 2))
    print 'payment = ' + str(round(payment, 2))
    print ''

print 'Lowest Payment: ' + str(round(payment, 2))