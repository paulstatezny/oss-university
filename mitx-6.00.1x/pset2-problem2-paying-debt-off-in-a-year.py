balance = 5000
annualInterestRate = 0.18

payment = 0
lowestPaymentFound = False

while (not lowestPaymentFound):
    payment += 10
    testBalance = balance
    for i in range(12):
        testBalance -= payment
        interest = testBalance * (annualInterestRate / 12)
        testBalance += interest
    if testBalance <= 0:
        lowestPaymentFound = True

print 'Lowest Payment: ' + str(payment)