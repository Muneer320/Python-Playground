import pyperclip

text = input("What do you want to copy: ")
times = int(input("How many times: "))

pyperclip.copy(text * times)