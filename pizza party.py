students=int(input("enter number of students:"))
slices=int(input("enter number of slices:"))
total=students*slices
pizzas=(total+7)//8
leftover =(pizzas*8)-total
print("total slices required=",total)
print("pizzas required=",pizzas)
print("leftover slices=",leftover)