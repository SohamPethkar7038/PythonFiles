# Password Strength Checker

password=str(input("enter the password\n"));

password_length=len(password)

if len(password)<6:
    strength="weak";
elif len(password)<=10:
    strength="Medium"
else:
    strength="strong";
    
print("password strength is",strength);     