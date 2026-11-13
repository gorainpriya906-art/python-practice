#A website requires a password to contain at least 8 characters.
#If password has 8 or more characters → "Strong enough"
#Otherwise → "Password too short"
password=(input("enter password:"))
if len(password)>=8:
    print("password is strong")
else:  
    print("password is too short")

