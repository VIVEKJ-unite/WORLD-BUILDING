with open("demo.txt", "r") as file:
    content = file.read()
    print(content) 
    words = content.split()
    num = len(words)
    print(num) 

"""file = open("demo.txt", "r")
content = file.read()
count = 0
for i in content:
    if (i == '.'):
        count -= 1
    elif (i == ' '):
        count += 1
print(count + 1)
file.close()"""