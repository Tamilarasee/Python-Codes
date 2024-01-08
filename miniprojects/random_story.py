from Stories import elephant_and_ants,hare_and_tortoise,music,thirsty_crow
import random

# story_list = []
#
# from pathlib import Path
#
# path_loc = r"C:\Users\User\PycharmProjects\TamilPracticeCodes\mini_projects\Stories"
# path = Path(path_loc)
# for file in path.glob('*'):
#     story_list.append(file.name.rstrip(".py"))
# print(story_list)


if __name__ == "__main__":
    chosen_story = random.choice([elephant_and_ants,hare_and_tortoise,music,thirsty_crow])
    print(chosen_story)
    chosen_story.madlib()