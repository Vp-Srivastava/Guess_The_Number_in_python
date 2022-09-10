import random
Com_Number=random.randrange(1,100)
User_input=int(input("Enter your Number---"))

#Check the condition
if(Com_Number>User_input):
    print("Computer Number ",Com_Number )
    print("Your Guess Number is too Low")

elif(User_input>Com_Number):
    print("Computer Number ", Com_Number)
    print("Your Guess Number is too high")


else:
    print("Computer Number ",Com_Number)
    print("Your Guess Number is exactly Same")