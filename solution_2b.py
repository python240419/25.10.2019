import threading
import time


# **Etgar:
# present a calculation i.e. 5 * 7 = ?
# wait for the user to input a number until
# he enters the correct number
# in the background run a timer of 5 seconds
# after 5 seconds, if no correct input was given
# print "too bad..." and exit the program
# if during the 5 secodns a correct input was given
# print "correct" and exit the program

class Game:
    def __init__(self):
        self.answer_correct = False

    def time_printer(self):
        counter = 10;
        while counter > 0:
            time.sleep(1)
            counter = counter - 1
            if self.answer_correct == True:
                return
            print(counter)

        # reach here only if no correct answer recieved
        print("game over...")

    def math_input(self):
        correct_answer = 35
        print("5 * 7 ")
        temp = 0
        answer = 0
        while answer != correct_answer:
            temp = input("Your solution?")
            answer = int(temp)
        self.answer_correct = True

    def start_game(self):
        timer_thread = threading.Thread(target=self.time_printer)
        timer_thread.start()

        game_thread = threading.Thread(target=self.math_input)
        game_thread.daemon = True
        game_thread.start()

game = Game()
game.start_game()




