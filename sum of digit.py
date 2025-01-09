
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))
numbers = [123, 456, 789, 101]
result = [sum_of_digits(number) for number in numbers]

# Output the result
print("Original list:", numbers)
print("Sum of digits at each index:", result)
