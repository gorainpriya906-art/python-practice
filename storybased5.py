#A cinema charges ₹200 per ticket. Ask for the number of tickets and calculate the total cost. If more than 5 tickets are booked, give a 15% discount
tickets=int(input("enter a number of ticket:"))
total=tickets*200
if tickets>5:
    discount=total*15/100
    final_amount=total-discount
else:
    final_amount=total
print("total amount =",total) 
print("final_amount =",final_amount)


