#Write a basic program 


 #initiatlization
i=1 

while (i<=10):

    # The body of the loop
    print('The number is :' , i)  
    i+=1   # The increment

""" The basic program on while loop"""

prompt='\n Tell me something!, I will repeat it to you: '

prompt += '\n Enter "quit" to exit the game'

message=""
""" The while loops using flags"""

active=True
while active:

    message=input(prompt)

    if message == 'quit':
        active=False
    else:
        print(message)
print(message)

