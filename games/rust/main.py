import keyboard

from classes.actionsManager import ActionsManager
from .playSong import playSong
from .chatTest import chatTest

def printintingText():
  print("XXXXX")

def printingNumbers():
  print(1, 2, 3, 4, 5)


def rust_actions():
  print("play song time")
  keyboard.unhook_all()

  actions_manager = ActionsManager()
  actions_manager.scripts = True
  
  actions_manager.register_action("1-True", printintingText)
  actions_manager.register_action('2-True', printingNumbers)
  actions_manager.register_action('3-True', playSong)
  actions_manager.register_action("4-True", chatTest)

  keyboard.on_press(actions_manager.perform_action)