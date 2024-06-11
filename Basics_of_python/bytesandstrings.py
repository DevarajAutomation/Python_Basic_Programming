"""The bytes are strings in python are different"""

b1=bytes([0x41,0x42,0x43,0x44])
#print(b1)
#Initialize the string
s1='This is python'
#print(b1+s1)    #This must throw an error

b=b1.decode('utf-8')

print(b)
print(b+s1) 