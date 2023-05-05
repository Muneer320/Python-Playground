import win32api
import keyboard

while keyboard.is_pressed('q') == False:
    x, y = win32api.GetCursorPos()
    print(x, y)