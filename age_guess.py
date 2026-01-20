import random

def guess_age():
    print("Hey!  I'm going to try and guess your age.")
    name = input("What's your name?")
    
    while True:
        age = random.randint(15, 30)
        answer = input(f"Is your age {age}? (y/n): :")

        if answer == 'y':
            print(f"Yes! {name} is {age} years old.")
            break
        else:
            print("Rats...")
   
def main():
    guess_age()

if __name__ == "__main__":
    main()
