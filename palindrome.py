import string
st = input("Enter the string")
rev = st[::-1]
if(st == rev):
    print("it is palindrome")
else:
    print("it is not palindrome")

------------------------------------------------------------------------------------------------------------------
s = input("enter the string: ")
def palindrome(s):
    for  i in range (0,len(s)/2):
        if (s[i] != s[len(s) -i -1 ]:
            return  0
        else:
            return 1

r = palindrome(s)
if (r):
    print("string is palindrome:")
else:
    print("string is not palindrome")
