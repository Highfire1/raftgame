'''
incremental raft game
take over the world, all from a shipwreck
By buckler, devepcoder, electronicsboy & highfire1
'''

import random

print("you open your eyes")
print("you are on a lifeboat")
print("you can see nothing but water around you")

input("search the boat")

print("you find some rations and a fishing rod")
print("and a note that says good luck")

fishes = { 
    "cod": 33,
    "sardines":33,
    "tuna":33,
    "junk":1
}



def fish():
    print("you cast your rod")
    catch = random.choice(list(fishes.values))
    print("You caught a " + catch)
