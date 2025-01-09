#from math import factorial
#num = int(input("Enter the number:"))
#print(factorial(num))


num  = int(input("Enter the number: "))

fact = 1
for i in range (1, num+1):
    
    fact *= i
print(fact)
