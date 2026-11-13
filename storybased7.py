#A student returns a library book late. The library charges:
#1–5 late days → ₹2 per day
#6–10 late days → ₹3 per day
#More than 10 days → ₹5 per day
#Write a Python program to calculate the total fine
days=int(input("enter late days:"))
if days<=5:
 fine=days*2
elif days<=10:
 fine=days*3 
else:
 fine=days*5  
print("total fine =",fine)
