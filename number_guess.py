import random
x=True
number=random.randint(1,100)
while x:
    try:
        guess=int(input("Enter a Number Between 1 to 100 : "))
        if guess>number:
            # print("greater")
            print("number")
        elif guess < number :
            print("lower")    
            print("number")
        else:
            print("you guessed it correctly!")   
            break
    except ValueError:
        print("ivalid choice!")    