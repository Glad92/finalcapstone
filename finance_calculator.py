#this is a python program to allow a user to calculate their interest and bond
#investment is categorise into simple interest and compound
#use of if else statment
#interest rate is in percentage


import math
print("investment - to calculate the amount of interest you'll earn on your investment.")
print("bond - to calculate the amount you'll have to pay on a home loan.")
user=input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
print(user)

#calculate simple or compund interest
if (user == 'investment'):
   P = float(input('Enter the principle amount: '))
   t = float(input('Enter the years of planned investment: '))
   m = float(input('Enter interest rate: '))
   r = m/100
   new_user = str(input("Enter either 'simple' or 'compound': ")).lower()
   simple_interest = P* (1 + r * t)
   compound = P * math.pow((1 + r),t)
   if (new_user == 'simple'):
      print("Your simple interest rate is : ", simple_interest)

   if( new_user == 'compound'):
     print(" Your compund interest is :  ", compound)

#calculate amount to be paid monthly on a home loan
elif (user == 'bond'):
     P = float(input('Enter current value for the house: '))
     r = float(input('Enter the interest rate: '))
     i = (r/100)/12
     n = float(input(' Enter the number of months for repayment: '))
     repayment = ( i* P) /( 1- ( 1 + i) ** (-n))
     print(repayment)
    
else:
   print("incorrect choice")