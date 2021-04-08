#MUHAMMAD AMIRUL  HAFIZ BIN SYOFIAN
#20DDT19F1104

for x in range(11):
    number=x*x
    print ("The square of",x,"=",number)

#b)
maximum =10
total = 0

for number in range(2, maximum + 1, 2):
    total = total + number

print("The Sum of Even Numbers from 1 to {0} = {1}".format(number, total))


#2
import re
Username=input("Please enter your username :")
password=input("Please enter your password :")
x = True
while x:  
    if len(password)<5:
        break
    elif not re.search("[a-z]",password):
        break
    elif not re.search("[0-9]",password):
        break
    elif not re.search("[A-Z]",password):
        break
    else:
        print("Valid Password")
        x=False
        break
if x:
    print("Your password need to contain atleast 5 characters")

#3)
carPrice=103300
downpayment=carPrice*0.1
downpaymentPay=float(input("Please enter your downpayment :"))
if downpayment<downpaymentPay:
    print("you not eligible for the bank loan")
else:
    print("eligible for bank loan")
    loanPeriod=float(input("Please enter your loan period in years :"))
    loanAmount=carPrice-downpaymentPay
    totalInterest=0.027*loanAmount*loanPeriod
    loanPeriodMonth=loanPeriod*12
    monthlyinstallment=round(((loanAmount+totalInterest)/loanPeriodMonth),2)
    
    print('You need to pay Rm',monthlyinstallment,'as your montly installment')
