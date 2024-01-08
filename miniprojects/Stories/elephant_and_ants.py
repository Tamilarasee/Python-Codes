def madlib():
    print("Elephant and Ants\n")


    adj1 = input("Adjective: ")
    adj2 = input("Adjective: ")
    emotion = input("Emotion: ")
    body_part = input("Elephant body part: ")
    action = input("Action verb: ")
    sound = input("Sound: ")
    apology = input("Words for feeling sorry: ")

    mad_lib = f"There was once a {adj1} elephant who constantly bullied {adj2} animals. \
He would go to the anthill near his home and spray water at the ants. The ants, with their size, \
could do nothing but {emotion}. The elephant just laughed and threatened the ants that he would crush them to death.\
One day, the ants had enough and decided to teach the elephant a lesson. They went straight into the \
elephant’s {body_part} and started {action} him. The elephant could only {sound} in pain. He realized his mistake and \
{apology} to the ants and all the animals he bullied."

    print(mad_lib)
