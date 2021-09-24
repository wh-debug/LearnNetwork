# 如何使用while保存字典

personsport = {}

Flag = True

while Flag:
    name = input("\nwhat's your name? ")
    sport = input("what are you favourite sport? ")

    personsport[name] = sport

    repeat = input("Would you like to let another person respond? (yes/nop) ")

    if repeat == 'no':
        Flag = False

print("\n--------Poll Results--------")
for name, sport in personsport.items():
    print(f"{name} would like to {sport}")