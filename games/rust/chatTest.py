import pyautogui
import time

def writeText(text):
  pyautogui.press('enter')
  pyautogui.typewrite(text)
  pyautogui.press('enter')
  time.sleep(5)

def chatTest():
  pyautogui.keyDown('altleft')
  pyautogui.press('shift')
  pyautogui.press('1')
  pyautogui.keyUp('altleft')

  writeText("Naruto sucks")
  writeText("Kaiji is the best - 21, Kaiji is the best - 43, Kaiji is the best - 65, Kaiji is the best - 87, Kaiji is the best - 109, Kaiji is the best - 131, Kaiji is the best - 153, Kaiji is the best - 175, Kaiji is the best - 197, Kaiji is the best - 219, Kaiji is the best - 241, Kaiji is the best - 263") 
  writeText("!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~")
  writeText("<script>alert(“I hacked this!”)</script>")
  writeText("'; SELECT * FROM users; --")
  writeText("          ")