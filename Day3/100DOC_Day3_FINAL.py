print('''
*******************************************************************************
                 _____
              .-" .-. "-.
            _/ '=(0.0)=' \_
          /`   .='|m|'=.   `\
          \________________ /
      .--.__///`'-,__~\\\\~`
     / /6|__\// a (__)-\\\\
     \ \/--`((   ._\   ,)))
     /  \\  ))\  -==-  (O)(
    /    )\((((\   .  /)))))
   /  _.' /  __(`~~~~`)__
  //"\\,-'-"`   `~~~~\\~~`"-.
 //  /`"              `      `\
//
*******************************************************************************
''')

print("Welcome to Treasure Island! ")
print("Your mission is to find the treasure. ")

crossroad = input("You're at a cross-road. Where do you want to go? Type 'left' or 'right.' ")

if crossroad == "right":
    print("You've fallen off a cliff. Game Over ")
else:
    lake = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ")

    if lake == "swim":
        print("You were eaten by a shark. Game Over... ")
    else:
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One is red, the others are yellow and blue. Which color do you choose? ")

        if door != "yellow":
            print("It's a room full of fire. Game over :( ")
        else:
            print("Congrats - you found the treasure! ")
