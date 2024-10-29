from sense_hat import SenseHat
import random


def roll_dice():
    result = random.randint(1, 6)
    return result


s = SenseHat()
s.low_light = True

blue = (0, 0, 255)
white = (255,255,255)

def dice1():
    B = blue
    W = white
    logo = [
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    W, W, W, B, B, W, W, W,
    W, W, W, B, B, W, W, W,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
]
    return logo

def dice2():
    B = blue
    W = white
    logo = [
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, B, B, W,
    W, W, W, W, W, B, B, W,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    W, B, B, W, W, W, W, W,
    W, B, B, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
]
    return logo

def dice3():
    B = blue
    W = white
    logo = [
    W, W, W, W, W, W, B, B,
    W, W, W, W, W, W, B, B,
    W, W, W, W, W, W, W, W, 
    W, W, W, B, B, W, W, W, 
    W, W, W, B, B, W, W, W, 
    W, W, W, W, W, W, W, W, 
    B, B, W, W, W, W, W, W, 
    B, B, W, W, W, W, W, W,
]
    return logo

def dice4():
    B = blue
    W = white
    logo = [
    W, W, W, W, W, W, W, W,
    W, B, B, W, W, B, B, W,
    W, B, B, W, W, B, B, W,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    W, B, B, W, W, B, B, W,
    W, B, B, W, W, B, B, W,
    W, W, W, W, W, W, W, W,
]
    return logo

def dice5():
    B = blue
    W = white
    logo = [
    B, B, W, W, W, W, B, B, 
    B, B, W, W, W, W, B, B, 
    W, W, W, W, W, W, W, W, 
    W, W, W, B, B, W, W, W, 
    W, W, W, B, B, W, W, W, 
    W, W, W, W, W, W, W, W, 
    B, B, W, W, W, W, B, B, 
    B, B, W, W, W, W, B, B,
]
    return logo

def dice6():
    B = blue
    W = white
    logo = [
    B, B, W, W, W, W, B, B, 
    B, B, W, W, W, W, B, B, 
    W, W, W, W, W, W, W, W,
    B, B, W, W, W, W, B, B, 
    B, B, W, W, W, W, B, B, 
    W, W, W, W, W, W, W, W,
    B, B, W, W, W, W, B, B, 
    B, B, W, W, W, W, B, B,
]
    return logo






images = [dice1, dice2, dice3, dice4, dice5, dice6]
result = 6

user_input = input("Press enter to roll the dice" or "q to quit")

# while user_input != "q":
#     diceresult = roll_dice()
#     if diceresult == 1:
#         s.set_pixels(images[0])
        
#     elif diceresult == 2:
#         s.set_pixels(images[1])
#     elif diceresult == 3:
#         s.set_pixels(images[2])
#     elif diceresult == 4:
#         s.set_pixels(images[3])
#     elif diceresult == 5:
#         s.set_pixels(images[4])
#     elif diceresult == 6:
#         s.set_pixels(images[5])



#     user_input = input("Press enter to roll the dice" or "q to quit:" )
while user_input != "q":
    diceresult = roll_dice()
    s.set_pixels(images[diceresult - 1]())  # Correct way to call the function

    user_input = input("Press enter to roll the dice or 'q' to quit: ")

print("Thanks for playing!")