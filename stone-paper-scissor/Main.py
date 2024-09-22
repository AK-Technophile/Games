import random

"""

1 = rock
0 = paper
-1 = Scissors 

"""

while(1==1):

    computer=random.choice([-1,0,1])

    yourdict = {"r":1,"p":0,"s":-1}

    print("""
    press :
          p for paper
          r for rock
          s for scissor
        """)
    
    youin=input("Enter ur choice : ")
    revdict={1:"Rock",0:"paper",-1:"scissor"}

    compin=yourdict[youin]

    print(" ")
    print("========================")
    print(f"\nComputer : {revdict[computer]}\nYOU : {revdict[compin]}\n")
    print("========================")
    print(" ")

    if(computer==compin):
        print("OH no its a DRAW T_T")

    else:    
        if(computer==1 and compin==0):
            print("--> RESULT == You won! :)")
        elif(computer==0 and compin==-1):    
            print("--> RESULT == You won! :)")
        elif(computer==-1 and compin==1):    
            print("--> RESULT == You won! :)")
        elif(computer==0 and compin==1):    
            print("--> RESULT == You lost! >_<")
        elif(computer==-1 and compin==0):    
            print("--> RESULT == You lost! >_<")
        elif(computer==1 and compin==-1):    
            print("--> RESULT == You lost! >_<")
        else:
            print("Something went WRONG :(")   

    print(" ")
    stop=int(input("Press 1 to replay and 0 to stop : "))
    if(stop==0):
        break

print(" ")
print("Thanks for playig !")
