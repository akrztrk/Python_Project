
print("Welcome to Treasure Island.")
print("Your mission isto find the treasure")

choice1 = input("Please choose 'Right' or 'Left'\n").lower()
if choice1 == "right":
    print("Game Over")
elif choice1 == "left":
    print("Congratulations, you've made it to the next level")
    choice2 = input("Do you want to swim or wait? Please write 'Swim' or 'Wait'\n").lower()
    if choice2 == "swim":
        print("Game Over")
    elif choice2 == "wait":
        print("Congratulations, you've made it to the next level")
        choice3 = input("Please choose door color? 'Red', 'Blue' or 'Yellow'\n").lower()
        if choice3 == "red":
            print("Game Over")
        elif choice3 == "blue":
            print("Game Over")
        elif choice3 == "yellow":
            print('''  You win
                .-=-.)
                /_ _  )
                \@ @  /
                (_> _)
                  `)(_
                  /((_`)_,
                  \__(/-"
                 __|||__
                ((__|__))
            ''')
        else:
            print("wrong login")
    else:
        print("wrong login")
else:
    print("wrong login")