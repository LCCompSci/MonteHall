import random

# List of Doors
doors = ["a","b","c"]

stickingwins=0
stickinglosses=0
switchingwins=0
switchinglosses=0

trials = int(input("How many trials?"))

# Sticking Trials
for sticking in range(0,trials):
        
    winning_door = doors[random.randint(0,2)]
    pick = doors[random.randint(0,2)]
    
    # We're sticking to our pick so if it's a winner we count it
    if(pick==winning_door):
        stickingwins += 1
    # If we didn't pick the winner we count it as a lost
    else:
        stickinglosses += 1
        

# Switching Trials
for switching in range(0,trials):
           
    winning_door = doors[random.randint(0,2)]
    pick = doors[random.randint(0,2)]
    
    # We're switching so if we have picked the winner, it counts as a loss
    if(pick==winning_door):
        switchinglosses += 1
    
    # If we didn't pick the winner, we switch to it now so it's a win
    else:
        switchingwins += 1



print("Sticking win",round((stickingwins/(stickingwins+stickinglosses)*100),0),"%")
print("Sticking loss",round((stickinglosses/(stickingwins+stickinglosses)*100),0),"%")

print("Switching win",round((switchingwins/(switchingwins+switchinglosses)*100),1),"%")
print("Switching loss",round((switchinglosses/(switchingwins+switchinglosses)*100),1),"%")


