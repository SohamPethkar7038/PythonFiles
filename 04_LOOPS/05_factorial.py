# find the factorial number using while loop

number=int(input("enter the number "));
factorial=1;

while number >0:
    factorial=factorial*number
    #factorial*=number;
    number=number-1;
    #number-=1
    
print(factorial);