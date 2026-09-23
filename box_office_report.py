#Daniel Salazar
#CMP 131-86520
# week 4
# lab 1
# assignment 3
# 9/22/2026
movie_title=input("enter the movie title: ")
adult_tickets=int(input("Enter the number of adult tickets sold: "))
child_tickets=int(input("Enter the number of chilc tickets sold: "))
print("Movie:", movie_title)
print("Adult tickets:", adult_tickets)
print("Child tickets:", child_tickets)
adult_revenue= adult_tickets * 10.00
child_revenue= child_tickets * 6.00
gross_revenue= adult_revenue + child_revenue
theater_amount= gross_revenue * 0.20
distributor_amount= gross_revenue * 0.80
print("Adult Ticket Revenue: $", adult_revenue)
print("Child ticket Revenue: $", child_revenue)
print("Gross Box Office Revenue: $", gross_revenue)
print("Amount kept by Theater: $", theater_amount)
print("Amount Paid to Distributor: $", distributor_amount)