# a = input("PLayer 1 Turn: Snake(s) Water(w) or Gun(g)?")
#this will create cheating

#rules of games
#1.if you chose g and comp chose s ->you win
#else : comp wins
#2 if you chose w and comp chose g->you wins
#else :comp wins
#3 if you choose s and comp choose w -> you wins
#else:comp wins
#if both choose same value -> Tie

#Now you play-->

#we will use random function
import random



def gameWin(comp,You):
    if comp == You:
        return None #Tie 
    elif comp == 's':
        if You == 'w':
            return False #player lose the match
        elif You == 'g':
            return True #player win the match
    elif comp == 'w':
        if You == 'g':
            return False #player lose the match
        elif You == 's':
            return True #player win the match
    elif comp == 'g':
        if You == 's':
            return False #player lose the match
        elif You == 'w':
            return True #player win the match


print("Lets Play Water,Snake and Gun Game**\n")

print("Comp Turn: Snake(s) Water(w) or Gun(g)?") 
randNo = random.randint(1,3)

if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'



You = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
a = gameWin(comp,You)

print(f"Computer chose {comp}")
print(f"You chose {You}")

if a == None:
    print("The game is tie!")
elif a:
      print("You Win!")
else:
    print("You lose !")