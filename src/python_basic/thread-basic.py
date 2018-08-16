# import the threading module
import threading


class MyThread(threading.Thread):
    def __init__(self, thread_name, thread_id):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_id = thread_id

        # helper function to execute the threads

    def run(self):
        print(str(self.thread_name) + " " + str(self.thread_id))


thread1 = MyThread("GFG", 1000)
thread2 = MyThread("GeeksforGeeks", 2000);

thread1.start()
thread2.start()

print("Exit")
