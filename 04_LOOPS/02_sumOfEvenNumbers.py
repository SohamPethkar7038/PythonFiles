
#  count the sum of the evne numbers



# Define the value of n
n = 10

# Initialize the sum
sum_even = 0

# Loop through numbers from 1 to n
for i in range(1, n + 1):
    if i % 2 == 0:  # Check if the number is even
        sum_even += i

# Display the result
print("Sum of even numbers up to", n, "is:", sum_even)
