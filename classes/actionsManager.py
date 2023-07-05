import keyboard
from colorama import Fore

class ActionsManager:
  def __init__(self):
    self.actions = {}
    self.scripts = False

  def register_action(self, key, action):
    self.actions[key] = action

  def perform_action(self, event):
    print(event)

    key = "{}-{}".format(event.name, event.is_keypad)
    if key in self.actions:
      if self.scripts:
        keyboard.unhook_all()

      action = self.actions[key]
      action()

      if self.scripts:
        keyboard.on_press(self.perform_action)
    else:
      print(Fore.RED + "You should press the correct button")
      print(Fore.RESET, end="")
