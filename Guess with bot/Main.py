import random

n = random.randint(1,100)
guess=0
a=-1
print("Guess the number b/w 1 to 100 in least guesses.")
print()
while(a!=n):
    a=int(input("Enter ur Guess : "))

    if(a>n):
        print("Lower number plz")
        guess+=1
    elif(a<n):
        print("Greater number plz")
        guess+=1

    print()    

print(f"You have gussed the number {n} correctly in {guess} attempts !")        
