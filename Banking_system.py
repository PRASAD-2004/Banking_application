from Banking_Operation import *


prasad=Bank('prasad',1000)
sairam=Bank("sairam",2000)
prasad.checkbalance()
sairam.checkbalance()

prasad.withdraw(500)
sairam.withdraw(1000)

prasad.deposit(1000)

prasad.transfer(500,sairam)