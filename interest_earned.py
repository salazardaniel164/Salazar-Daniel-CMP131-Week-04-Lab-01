#Daniel Salazar
#CMP 131-86520
# week 4
# lab 1
# assignment 3
# 9/22/2026
principal=float(input("Enter the principal amount originally deposited: ")) 
interest_rate=float(input("Enter the amountinterest rate as a percentage: "))
compounding_periods=int(input("Enter the number of times the interst is compounded per year: "))
interest_rate=interest_rate / 100
final_amount= principal * (1 + interest_rate / compounding_periods) ** compounding_periods
interest_earned = final_amount - principal
print("Principal Amount: $", principal)
print("Final amount Balance: ${:.2f}".format(final_amount))
print("Interest Earned: ${:.2f}".format(interest_earned))
#when entering numbers with commas, just type out the number no commas, decimals are okay
