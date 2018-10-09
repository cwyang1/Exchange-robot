#-*- coding=utf-8 -*-
import threading
from test_robot import robot

while 1:
    a = robot()

    run1 = threading.Thread(target=a.run_robot, args=('ethusdt',))
    run2 = threading.Thread(target=a.run_robot, args=('btcusdt',))
    run3 = threading.Thread(target=a.run_robot, args=('etcusdt',))

    run1.start()
    run2.start()
    run3.start()

    run1.join()
    run2.join()
    run3.join()




