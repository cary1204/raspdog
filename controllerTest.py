#!/usr/bin/env python3
import time
from pidog import Pidog
from preset_actions import *
import pygame

# Initialize Pygame and joystick
pygame.init()
pygame.joystick.init()

# Initialize Pidog
my_dog = Pidog()
time.sleep(0.5)

# Global variables
STATUS_STAND = 0
STATUS_SIT = 1
STATUS_LIE = 2
HEAD_SPEED = 80
HEAD_ANGLE = 20

head_yrp = [0, 0, 0]
head_pitch_init = 0
current_status = STATUS_LIE

# Define button mappings (adjust as needed)
BUTTONS = {
    0: "bark",          # A button
    1: "sit",           # B button
    2: "stand",         # X button
    3: "lie",           # Y button
    4: "turn left",     # Left bumper
    5: "turn right",    # Right bumper
    6: "stop",          # Back button
    7: "stretch",       # Start button
}

AXES = {
    0: "turn left",    # Left stick X-axis
    1: "forward",      # Left stick Y-axis
    3: "backward",     # Right stick Y-axis
}

OPERATIONS = {
    "forward": lambda: my_dog.do_action('forward', speed=98),
    "backward": lambda: my_dog.do_action('backward', speed=98),
    "turn left": lambda: my_dog.do_action('turn_left', speed=98),
    "turn right": lambda: my_dog.do_action('turn_right', speed=98),
    "sit": lambda: my_dog.do_action('sit', speed=70),
    "stand": lambda: my_dog.do_action('stand', speed=70),
    "lie": lambda: my_dog.do_action('lie', speed=70),
    "bark": lambda: bark(my_dog, head_yrp, pitch_comp=head_pitch_init),
    "stretch": lambda: my_dog.do_action('stretch', speed=80),
    "stop": lambda: my_dog.stop(),
}

def run_operation(operation):
    if operation in OPERATIONS:
        OPERATIONS[operation]()

def main():
    joystick = None
    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        print(f"Controller connected: {joystick.get_name()}")
    else:
        print("No controller detected. Exiting...")
        return

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.JOYBUTTONDOWN:
                button = event.button
                if button in BUTTONS:
                    operation = BUTTONS[button]
                    run_operation(operation)
            elif event.type == pygame.JOYAXISMOTION:
                axis = event.axis
                value = event.value
                if abs(value) > 0.5:  # Deadzone threshold
                    if axis in AXES:
                        operation = AXES[axis]
                        run_operation(operation)
        
        time.sleep(0.1)

if __name__ == "__main__":
    main()
