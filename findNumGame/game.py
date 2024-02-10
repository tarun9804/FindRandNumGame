import yaml
import random


class FindNumGame:
    def __init__(self):
        with open("game_config.yaml", "r") as f:
            config_game = yaml.safe_load(f)
        self.max_limit = config_game['maxLimit']
        self.max_chance = config_game['maxChance']

    def play_game(self):
        correct_num = random.randint(1, self.max_limit)
        count = 0
        while count < self.max_chance:
            guessed_num = int(input("guess the number: "))
            if guessed_num < correct_num:
                print("too low")
            elif guessed_num > correct_num:
                print("too high")
            else:
                print("Hooray, guessed it correctly")
                break
            count = count + 1;
        print("Exceeded your limit of chance, Try again!!")


if __name__ == "__main__":
    x = FindNumGame()
    x.play_game()
