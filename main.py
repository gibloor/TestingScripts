import keyboard
from colorama import init

from classes.actionsManager import ActionsManager
from games.rust.main import rust_actions
from games.tarkov.main import tarkov_actions

init()

actions_manager = ActionsManager()
actions_manager.register_action("1-True", rust_actions)
actions_manager.register_action('2-True', tarkov_actions)

def start():
  games = [
    "1-numpad-Rust",
    "2-numpad-Tarkov"
  ]

  for game in games:
    print(game)

  print("Choose the game")
  keyboard.on_press(actions_manager.perform_action)
  keyboard.wait("esc")

start()