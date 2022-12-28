
#Get the loan details
money_owed = float(input('How much money do you owe, in dollers?\n')) # $50,000
apr = float(input('What is the annual percentage rate?\n')) # 3%
payment = float(input('What will your monthly payment be, in dollers?\n')) # $1,000
months = int(input('How many months do you want to see results for?\n')) # 24

#Devide apr by 100 to make is percent, then devide by 12 to make it monthly
monthly_rate = apr/100/12

for i in range(months):
    #Add in interest
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    if(money_owed - payment < 0):
        print("The last payment is", money_owed)
        print("You paid of the loan in", i+1, "months")
        break

    #Make payment
    money_owed = money_owed - payment

    #Print ths results after this month
    print('Paid payment', payment, 'of which', interest_paid, 'was interest', end=' ')  #default end is with \n, make it space
    print('Now I owe', money_owed)

#output

#How much money do you owe, in dollers?
#50000
#What is the annual percentage rate?
#3
#What will your monthly payment be, in dollers?
#1000
#How many months do you want to see results for?
#54
#Paid payment 1000.0 of which 125.0 was interest Now I owe 49125.0
#Paid payment 1000.0 of which 122.8125 was interest Now I owe 48247.8125
#.
#.
#Paid payment 1000.0 of which 3.6868092659850893 was interest Now I owe 478.4105156600208
#The last payment is 479.60654194917083
#You paid of the loan in 54 months