# to check whether given number is prime number

number =30

isPrime=True;

if number>1:
    for i in range(2,number):
        if(number%2)==0:
            isPrime=False;
            break;

print(isPrime)