import pyautogui
import time

def playSong():
  sequence = [
    ('num1', 0.4), ('num1', 0.2), ('num1', 0.4), ('num2', 0.2),
    ('num3', 0.4), ('num3', 0.2), ('num3', 0.4), ('num2', 0.2),
    ('num1', 0.4), ('num1', 0.2), ('num1', 0.4), ('num2', 0.2),
    ('num3', 0.4), ('num3', 0.2), ('num3', 0.4), ('num2', 0.2),
    ('num1', 0.4), ('num2', 0.2), ('num3', 0.4), ('num4', 0.2),
    ('num5', 0.4), ('num5', 0.2), ('num5', 0.4), ('num4', 0.2),
    ('num3', 0.4), ('num3', 0.2), ('num3', 0.4), ('num2', 0.2),
    ('num1', 0.4), ('num2', 0.2), ('num3', 0.4), ('num4', 0.2),
    ('num5', 0.4), ('num5', 0.2), ('num5', 0.4), ('num4', 0.2),
    ('num3', 0.4), ('num3', 0.2), ('num3', 0.4), ('num2', 0.2),
    ('num2', 0.4), ('num2', 0.2), ('num2', 0.4), ('num1', 0.2),
    ('num1', 0.4), ('num1', 0.2), ('num1', 0.4), ('num2', 0.2),
    ('num3', 0.4), ('num3', 0.2), ('num3', 0.4), ('num2', 0.2),
    ('num1', 0.4), ('num2', 0.2), ('num3', 0.4), ('num4', 0.2),
    ('num5', 0.4), ('num5', 0.2), ('num5', 0.4), ('num4', 0.2),
    ('num3', 0.4), ('num3', 0.2), ('num3', 0.4), ('num2', 0.2),
    ('num1', 0.4), ('num2', 0.2), ('num3', 0.4), ('num4', 0.2),
    ('num5', 0.4), ('num5', 0.2), ('num5', 0.4), ('num4', 0.2),
    ('num3', 0.4), ('num3', 0.2), ('num3', 0.4), ('num2', 0.2),
    ('num2', 0.4), ('num2', 0.2), ('num2', 0.4), ('num1', 0.2),
    ('num1', 0.4), ('num1', 0.2), ('num1', 0.4), ('num2', 0.2),
    ('num3', 0.4), ('num3', 0.2), ('num3', 0.4), ('num2', 0.2),
    ('num1', 0.4), ('num2', 0.2), ('num3', 0.4), ('num4', 0.2),
    ('num5', 0.4), ('num5', 0.2), ('num5', 0.4), ('num4', 0.2),
    ('num3', 0.4), ('num3', 0.2), ('num3', 0.4), ('num2', 0.2),
  ]

  for key, delay in sequence:
    pyautogui.keyDown(key)
    time.sleep(delay)
    pyautogui.keyUp(key) 
