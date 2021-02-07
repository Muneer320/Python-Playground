import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

while True:
    speed = input("Please set the speed\n[1] Very Slow\n[2] Slow\n[3] Medium\n[4] Fast\n[5] Faster\n[6] Even more faster\n[7] Extreme\n")

    if speed == "1":
        delay = 2
    elif speed == "2":
        delay = 1
    elif speed == "3":
        delay = 0.1
    elif speed == "4":
        delay = 0.01
    elif speed == "5":
        delay = 0.001
    elif speed == "6":
        delay = 0.0001
    elif speed == "7":
        delay = 0.00001
    else:
        delay = 0.01

    print("Press 's' to start and then 's' to stop.\nPress 'e' to exit.")

    # delay = 0.0001
    button = Button.left
    start_stop_key = KeyCode(char='s')
    exit_key = KeyCode(char='e')


    class ClickMouse(threading.Thread):
        def __init__(self, delay, button):
            super(ClickMouse, self).__init__()
            self.delay = delay
            self.button = button
            self.running = False
            self.program_running = True

        def start_clicking(self):
            self.running = True

        def stop_clicking(self):
            self.running = False

        def exit(self):
            self.stop_clicking()
            self.program_running = False

        def run(self):
            while self.program_running:
                while self.running:
                    mouse.click(self.button)
                    time.sleep(self.delay)
                time.sleep(0.1)


    mouse = Controller()
    click_thread = ClickMouse(delay, button)
    click_thread.start()


    def on_press(key):
        if key == start_stop_key:
            if click_thread.running:
                click_thread.stop_clicking()
            else:
                click_thread.start_clicking()
        elif key == exit_key:
            click_thread.exit()
            listener.stop()


    with Listener(on_press=on_press) as listener:
        listener.join()
