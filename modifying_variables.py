from microbit import *

hungryness = 0

while True: 
    if button_a.is_pressed():
      hungryness = hungryness + 1
      sleep(500)
      display.show(hungryness)  
    if button_b.is_pressed():
        hungryness = 0
        display.show(hungryness)
    