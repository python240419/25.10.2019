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

def time_printer():
    global answer_correct
    counter = 10;
    while counter > 0:
        time.sleep(1)
        counter = counter - 1
        print(counter)
        if answer_correct == True:
            return
    # reach here only if no correct answer recieved
    print("game over...")

def math_game():
    global answer_correct
    correct_answer = 35
    print("5 * 7 ")
    answer = 0
    while answer != correct_answer:
        answer = int(input("Your solution?"))
    answer_correct = True

answer_correct = False

timer_thread = threading.Thread(target=time_printer)
timer_thread.start()

game_thread = threading.Thread(target=math_game)
game_thread.daemon = True
game_thread.start()




