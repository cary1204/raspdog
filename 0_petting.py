import time
import random
from math import sin, cos, pi
from pidog import Pidog
my_dog = Pidog()

def scratch(my_dog):
    h1 = [[0, 0, -40]]
    h2 = [[30, 70, -10]]
    f_up = [
        [30, 60, 50, 50, 80, -45, -80, 38],  # Note 1
    ]
    f_scratch = [
        [30, 60, 40, 40, 80, -45, -80, 38],  # Note 1
        [30, 60, 50, 50, 80, -45, -80, 38],  # Note 1
    ]
    my_dog.do_action('sit', speed=80)
    my_dog.head_move(h2, immediately=False, speed=80)
    my_dog.legs_move(f_up, immediately=False, speed=80)
    my_dog.wait_all_done()
    for _ in range(10):
        my_dog.legs_move(f_scratch, immediately=False, speed=94)
        my_dog.wait_all_done()

    my_dog.head_move(h1, immediately=False, speed=80)
    my_dog.do_action('sit', speed=80)
    my_dog.wait_all_done()

prev_touch_status = "N"

while True:
    touch_status = my_dog.dual_touch.read()
    print(f"touch_status: {touch_status}")
    time.sleep(0.5)
    
    if touch_status != prev_touch_status:  # Detect a change in status
        if touch_status != "N":
            print("Scratchdog on touch detected!")
            scratch(my_dog)  # Scratch when it first becomes not "N"
        elif touch_status == "N":
            print("Scratchdog on no touch detected!")
            scratch(my_dog)  # Scratch when it becomes "N"
    
    prev_touch_status = touch_status  # Update the previous status
