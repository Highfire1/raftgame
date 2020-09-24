import random
import os

os.system("")

print('''\x1B[92;40m
incremental raft game
take over the world, all from a shipwreck
By buckler, devepcoder, electronicsboy & highfire1
--------------------------------------------------\x1B[0m \n \n''')

Health = 7
Hunger = 5

def display_status(health: int, hunger: int):
    i = 0
    y = 0
    for x in range(health):
        i+=1
    print("Health : \x1B[31;40m " + "♥"*i + "\x1B[0m")
    for x in range(hunger):
        y+=1
    print("Hunger : \x1B[33;40m " + "▪"*y + "\x1B[0m \n")

display_status(Health, Hunger)
print("you open your eyes")
print("you are on a lifeboat")
print("you can see nothing but water around you")

input("search the boat")

print("you find some rations and a fishing rod")
print("and a note that says good luck")

fishes = [
    "cod",
    "sardines",
    "tuna",
    "junk"
]

print("you cast your rod")
catch = random.choice(list(fishes))
print("You caught a " + catch + "\n")
if catch == fishes[0]:
    Hunger += 2
elif catch == fishes[1]:
    Hunger += 1
elif catch == fishes[2]:
    Hunger += 3
elif catch == fishes[3]:
    Hunger -= 1
display_status(Health, Hunger)
