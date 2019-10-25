import threading
import time


# targil:
# print numbers 1-10 MainThread + thread-name
#   sleep(1)
# create another thread called "counter-2"
#    this thread will also print numbers 1-10 + thread-name
#    sleep(1)
# create another thread which prints out the time
#    sleep(1)
#    as a daemon thread

def time_printer():
    while True:
        time.sleep(1)
        print(time.ctime())

def count_1_10():
    for x in range(1, 11):
        print(f'{threading.currentThread().name} {x}')
        time.sleep(1)

timer_thread = threading.Thread(target=time_printer,
                             name="time-worker")
timer_thread.daemon = True
timer_thread.start()

counter_thread = threading.Thread(target=count_1_10,
                             name="counter-1")
counter_thread.start()

count_1_10()


# Main -- 1..10 X
# Counter -- 1..10 X 
# Timer -- print time every second
