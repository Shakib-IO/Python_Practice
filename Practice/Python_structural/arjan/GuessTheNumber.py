##### BEFORE #####
import random

class PlayerGuss:
    def __init__(self, name):
        self.name = name
    
    def welcome_meesage(self) -> str:
        print(f"Hello {self.name}!! Welcome to this Game!!")

    def guessTheNumber(self) -> int:
        print("Please guess a number between 1 to 10: ")
        number = int(input("Please enter your guess number: "))
        return number
 
class Track:
    def __init__(self, chance:int = 5):
        self.chance = chance

    def count_chance(self):
        return self.chance


class PlayGame:
    def __init__(self):
        self.playerdetails = PlayerGuss("Shakib")
        
        self.answer = random.randint(1, 10)
        self.numberOfChance = Track().count_chance()
        self.playerdetails.welcome_meesage()
        
    def run(self):
        print("Ready!!")
        print("Start")
        

        
        while self.numberOfChance > 0:
            self.playerNumber = self.playerdetails.guessTheNumber()
            
            if self.playerNumber == self.answer:
                print("You Win!!")
                return True
            elif self.playerNumber < self.answer:
                print("Too Low!")
            else:
                print("Too High!")
                
            self.numberOfChance -= 1
            print(f"Player has {self.numberOfChance} guesses left.")
            
            if self.numberOfChance <= 0:
                print("YOU LOST!!!! You have lost all the chances!!!")
                return False
            
def main() -> None:
    game = PlayGame()
    game.run()

if __name__ =="__main__":
    main()

##### AFTER ####
from dataclasses import dataclass
import random

@dataclass
class NumberGuessGame:
    guesses:int = 5
    answer: int =  random.randint(1, 10)

    @staticmethod
    def read_integer():
        return int(input("Enter a number between 1 and 10: "))
    
    def place_a_guess(self) -> bool:
        guess = NumberGuessGame.read_integer()
        if guess == self.answer:
            print("You win!")
        elif guess < self.answer:
            print("Too low!")
        else:
            print("Too high!")

        return guess == self.answer
    def play(self) -> None:
        print("I'm thinking of a number between 1 and 10.")
        print(f"You have {self.guesses} guesses.")
        print("Ready? Go!")

        while self.guesses > 0 and not self.place_a_guess():
            self.guesses -= 1
            print(f"Player has {self.guesses} guesses left.")
        if self.guesses <= 0:
            print(f"You lost! The number was {self.answer}.")


def main():
    game = NumberGuessGame()
    game.play()


if __name__ == "__main__":
    main()
