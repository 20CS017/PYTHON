import threading
import time

def func():
    print('ran')
    time.sleep(1)
    print("done")
    time.sleep(0.85)
    print("now done")

    x = threading.Thread(target=func)
    x.start()
    print(threading.activeCount())
    time.sleep(1.2)
    print('finally')
    
    #20CS017
    #20CS012
    #20CS008
