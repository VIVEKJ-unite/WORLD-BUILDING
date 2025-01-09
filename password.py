import string
import random
len = int(input("Enter the length of the password:"))
for i in range(len):
    print(random.choice(
	string.ascii_letters+
        string.digits +
        string.punctuation),
        end="")
print()
