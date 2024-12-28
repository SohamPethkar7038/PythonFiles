# counting the positive number

numbers=[1,2,3,4,5,-1,-2,10,-10];

positive_number_count=0;
for num in numbers:
    if num>0:
        positive_number_count+=1;
print("final count of positive number is : ",positive_number_count);        