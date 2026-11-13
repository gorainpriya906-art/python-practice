total_classes=int(input("enter a total number of classes:"))
attended_classes=int(input("enter attended classes:"))
attendance=(attended_classes/total_classes)*100
print("Attendance=",attendance,"%")
if attendance>=75:
    print("status=eligible")
else:
    print("status=not eligible")   
