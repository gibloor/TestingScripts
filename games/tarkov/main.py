import keyboard

from classes.actionsManager import ActionsManager

def printintingText():
  print("XXXXX")

def printingNumbers():
  print(1, 2, 3, 4, 5)

def tarkov_actions():
  keyboard.unhook_all()

  actions_manager = ActionsManager()
  actions_manager.register_action("1-True", printintingText)
  actions_manager.register_action('2-True', printingNumbers)

  keyboard.on_press(actions_manager.perform_action)
