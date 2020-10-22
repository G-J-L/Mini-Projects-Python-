# ERRORS TO COVER
# Invalid Input Given
# Spacing Required
import random
game = True
def game_on():
    choice = "WRONG"
    while choice.upper() not in ["Y", "N"]:
        choice = input("Would you like to keep rolling? (Y / N): ")
        if choice.upper() not in ["Y", "N"]:
            print("Sorry! That input is invalid. Please enter either (Y / N)")
        elif choice.upper() == "Y":
            return True
        elif choice.upper() == "N":
            return False

while game:
    print("        Welcome to Dungeons & Dice!")
    print("      Enter your roll like so \"2d20 + 4\"\nSpacing in between the operator is required!!!")
    try:
        roll = input("Take the chance! : ")
        dice_tn = roll.split()[0]
        rolls = []
        num_rolls = dice_tn[:dice_tn.index("d")]
        dice_type = dice_tn[1 + dice_tn.index("d"):]
        modif = ""
        if dice_tn == "8d6":
            print("\n                 FIREBALL!!!")
        if "+" in roll or "-" in roll:
            for val in roll.split()[1:]:
                modif += val
        else:
            modif += "0"
        if num_rolls == "" or num_rolls == " ":
            num_rolls = "1"
        for i in range(1, (1 + int(num_rolls))):
            dice = random.randint(1, int(dice_type))
            rolls.append(dice)
        print("                   Rolls:")
        print(">" + str(rolls) + " + (" + str(modif) + ")")
        print(">" + str(sum(rolls) + int(modif)))
    except:
        print("\n               Invalid Input")
    game = game_on()
    if game == False:
        break
    print("\n" * 5)
print(quit("\nTHANK YOU FOR USING DUNGEONS & DICE!!!"))
