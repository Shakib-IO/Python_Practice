import random


class Die:

    def __init__(self):
        self._value = None
    @property
    def value(self):
        return self._value
    
    def roll(self):
        new_value = random.randint(1,6)
        self._value =  new_value
        return new_value


class Player:

    def __init__(self, die, is_computer = False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 10
    
    @property
    def die(self):
        return self._die
    
    @property
    def is_computer(self):
        return self._is_computer
    
    @property
    def counter(self):
        return self._counter
    
    def increment_counter(self):
        self._counter += 1
    
    def decrement_counter(self):
        self._counter -= 1

    def roll_die(self):
        return self._die.roll()


class DiceGame:

    def __init__(self, player, computer):
        self._player =  player
        self._computer =  computer

    def play(self):
        print("===============================")
        print("Welcome to Dice Game 🎲🎲🎲🎲")
        print("===============================")

        while True:
            self.play_round()
            game_over = self.check_game_over()
            if game_over:
                break

    def play_round(self):
        print("\n------ New Round ------")
        input("🎲🎲🎲 Press any key to roll the dice 🎲🎲🎲\n")

        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die()

        print(f"Your Die: {player_value}")
        print(f"Computer Die: {computer_value}")

        if player_value > computer_value:
            print("🏆🏆🏆 You win this round 🏆🏆🏆")
            self._player.decrement_counter()
            self._computer.increment_counter()
        elif player_value < computer_value:
            print("🏆🏆🏆 Computer Win this round 🏆🏆🏆")
            self._computer.decrement_counter()
            self._player.increment_counter()
        else:
            print("Draw!!!")
        
        print(f"Your wins Counter: {self._player.counter}")
        print(f"Computer wins Counter: {self._computer.counter}")

    def check_game_over(self):
        if self._player.counter == 0:
            self.show_game_over(self._player)
            return True

        elif self._computer.counter == 0:
            self.show_game_over(self._computer)
            return True

        else:
            return False
    
    def show_game_over(self, winner):
        if winner.is_computer:
            print("\n=========================")
            print("G A M E  O V E R")
            print("=========================")
            print("\nCOMPUTER WON")
        else:
            print("\n=========================")
            print("G A M E  O V E R")
            print("=========================")
            print("YOU WON")
p_die = Die()
c_die = Die()

pl = Player(p_die, is_computer = False)
cm = Player(c_die, is_computer = True)

game = DiceGame(pl, cm)

game.play()
