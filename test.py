""" count = 10

while count != 0:
    print("This is loop number", count)
    count = count - 1 """
   
""" for i in range(1,10):
    print(i) """

""" x = input("what's your favorite color? type stop to finish.")

while x != ["red","orange","yellow","green","blue","purple","stop"]:  
    item = input("what's your favorite color?")
    if x == "stop":
        print("okay") """
""" 
 
order = ""

while order != "done":
    order = input("What would you like to order? (type 'done' to finish): ")

print("Thanks for your order!")"""

""" color = ""

while color != "stop":
    color = input("what's your favorite color? (type stop to finish): ")

print("thank you for your compliance")  """

import random
RandomNumber = random.randint(1,10)
guess = False
answer = int(input("guess a number from 1 to 10"))

while guess == False:
    if answer == RandomNumber:
        guess = True
        print("congrats youre correct")
    else:
        answer = int(input("wrong; try again"))