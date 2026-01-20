import random

def guess_age():
    print("Hey!  I'm going to try and guess your age.")
    name = input("What's your name?")
    correct_or_not = input(f"I'm going to guess your age is {random.randrange(15, 31)}!  Is that right? (y/n)")
    if correct_or_not == 'y':
        print(f"Yay! ! got it right!"
        return
    else:
        print("rats!")
    
