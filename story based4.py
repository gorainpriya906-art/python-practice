#Calculate electricity bill using these rules:
#First 100 units → ₹5 per unit
#Next 100 units → ₹7 per unit
#Above 200 units → ₹10 per unit
units=int(input("enter electricity units:"))
if units<=100:
 bill = units*5
elif units<=200:
 bill=(100*5) +((units-100)*7)
else:
 bill=(100*5)+(100*7)+((units-200)*10)
print("electricity bill=",bill)