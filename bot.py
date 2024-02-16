# pip install pyautogui
# The line `import pyautogui as pt` is importing the `pyautogui` module and assigning it the alias
# `pt`. This allows us to refer to the module using the shorter name `pt` throughout the code.
import pyautogui as pt
import time

# The line `from pygments import highlight` is importing the `highlight` function from the `pygments`
# module. This allows us to use the `highlight` function in our code without having to reference the
# module name.
from pygments import highlight

print("____START____")
print("Now open Whatsapp web and Click on person to send message")
time.sleep(5)
msg = input("Enter Your message :- ")
run = int(input("Enter How many times you want to message :- "))
counter = 1
print("Now Open Whatsapp Web And Not change The screen")
time.sleep(5)
print("Now Just Sit Back")
for i in range(run):
    pt.write(msg)
    time.sleep(0.0001)
    pt.press("Enter")
    counter += 1
    print(counter)

print("____END____")

