'''A bus service charges different fares based on age:
Age below 5 → Free
Age 5–17 → ₹20
Age 18–59 → ₹40
Age 60 or above → ₹25
Write a Python program that takes the passenger's age and displays the ticket fare'''
age=int(input("enter your age:"))
if age<5:
    fare=5
elif age<17:
    fare=20
elif age<59:
    fare=40
else:
    fare=25
print("ticket fare=",fare)   
