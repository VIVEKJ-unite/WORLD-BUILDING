L = []
num= int(input("enter the total size of list: "))
for i in range (num):
    n= int(input("Enter the element:"))
    L.append(n)
print(f"original list :{L}")
L.sort()
print(f"Ascending order: {L}")
L.sort(reverse = True)
print(f"descending order : {L}")
