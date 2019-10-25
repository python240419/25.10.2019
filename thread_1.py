import threading
import time
print(threading.currentThread().name)

def time_printer():
    print(threading.currentThread().name)
    print(time.ctime())
    while keep_running_my_thread:
        time.sleep(2)
        print(time.ctime())

def long_running_operation():
    time.sleep(30)

my_thread = threading.Thread(target=time_printer,
                             name="time-worker")
my_thread.daemon = True
keep_running_my_thread = True
my_thread.start()

a = input('Enter number')
print(f'{threading.currentThread().name} is saying bye')

if my_thread.isAlive():
    print(my_thread.isAlive())

# keep_running_my_thread = False

# targil:
# print numbers 1-10 MainThread + thread-name
#   sleep(1)
# create another thread called "counter-2"
#    this thread will also print numbers 1-10 + thread-name
#    sleep(1)
# create another thread which prints out the time
#    sleep(1)
#    as a daemon thread
