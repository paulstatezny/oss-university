totalPaid = 0

for i in range(12):
  payment = balance * monthlyPaymentRate
  balance -= payment
  interest = balance * (annualInterestRate / 12)
  balance += interest
  totalPaid += payment
  print 'Month: ' + str(i + 1)
  print 'Minimum monthly payment: ' + str(round(payment, 2))
  print 'Remaining balance: ' + str(round(balance, 2))
  
print 'Total paid: ' + str(round(totalPaid, 1))
print 'Remaining balance: ' + str(round(balance, 1))