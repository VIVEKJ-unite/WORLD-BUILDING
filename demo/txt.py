'''file = open("demo.txt","r")
consent =file.read()
print(consent)
file.close()
'''
'''
file =open("demo.txt","rb")
content= file.read()
print(content)
file.close()
'''
"""file=open("demo.txt","w")
file.write("parul is in vadodara,gujarat")
file=open("demo.txt","r")
content=file.read()
print(content)
file.close()"""

file=open("demo.txt","a")
file.write("\r this line is appended. ")
file=open("demo.txt","r")
content=file.read()
print(content)
file.close()

