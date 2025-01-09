a = int(input("total no. of element")) 
L = []
for i in range(a):
    ele= int(input("element to be entered:"))
    L.append(ele)

print(L)

avg = sum(L)/a

print(avg)
