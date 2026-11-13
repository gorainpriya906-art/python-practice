#notebook for 80,pen for 30,bag for 750 calculate total bill and give discount if total is more than 500and also display the final amount
notebook=80
pen=30
bag=750
total=notebook+pen+bag
if total>500:
    discount=total*10/100
    final_amount=total-discount
else:
    final_amount=total
print("total bill=",total)
print("final_amount=",final_amount)


