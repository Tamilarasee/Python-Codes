def madlib():
    print("Thirsty Crow\n")

    adj1 = input("Adjective: ")
    place = input("Location: ")
    food = input("Food/Drink: ")
    vessel = input("Container: ")
    size = input("Size(long/short: ")
    obj = input("Object: ")
    adj2 = input("Adjective: ")

    mad_lib = f"After flying a {adj1} distance, a thirsty crow wandered the {place} searching for {food}. \
Finally, he saw a {vessel} half-filled with {food}. He tried to drink from it, but his beak wasn’t \
{size} enough to reach the {food} inside. He then saw {obj} on the ground, and one by one, \
he put them in the {vessel} until the {food} rose to the brim. The crow then {adj2} drank from it and \
quenched his thirst."

    print(mad_lib)
