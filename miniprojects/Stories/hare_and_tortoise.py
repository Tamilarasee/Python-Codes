def madlib():
    print("Hare and Tortoise\n")

    relation = input("Relation: ")
    verb1 = input("Verb: ")
    speed = input("Speed(fast/slow): ")
    outcome = input("win/lose: ")
    verb2 = input("Verb: ")
    adj = input("Adjective: ")

    mad_lib = f"There was once a hare who was {relation} with a tortoise. One day, he {verb1} the tortoise \
to a race. Seeing how {speed} the tortoise was going, the hare thought he’d {outcome} this easily. So, he took a \
nap while the tortoise kept on going. When the hare {verb2}, he saw that the tortoise was already at the \
finish line. Much to his {adj}, the tortoise won the race while he was busy sleeping."

    print(mad_lib)