#Write a basic program 

i=1  #initiatlization

while (i<=10):
    print('The number is :' , i)  # The body of the loop
    i+=1   # The increment

""" The basic program on while loop"""

prompt='\n Tell me something!, I will repeat it to you: '

prompt += '\n Enter "quit" to exit the game'

message=""

while (message != 'quit'):

    message=input(prompt)

    if message != 'quit':
        print(message)
