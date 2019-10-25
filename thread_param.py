import threading
import time

def time_printer(start_count):
    counter = 10;
    while counter > 0:
        time.sleep(1)
        counter = counter - 1
        print(counter)

timer_thread = threading.Thread(target=time_printer
                                ,args = (int(input()),))
timer_thread.start()

