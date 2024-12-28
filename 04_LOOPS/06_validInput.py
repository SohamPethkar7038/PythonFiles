# keep asking the user for input until they enter a number between 1 and 100

while True:
    number=int(input("enter the number "));
    if 1<=number<=100:
        print("Thankyou for the number");
        break;
    else:
        print("invalid number ,try again");