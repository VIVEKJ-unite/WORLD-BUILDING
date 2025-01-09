L = []
n = int(input("enter the total number of list: "))
max = 0
num = 0
i = 0
a = int(input( "enter the value to be entered: " ))
while(i == n) :
    L.append(a)
    i+=1
for i  in L :
    if (L[i] > L[i+1]):
        max = L[i]
    else:
        max = L[i+1]
