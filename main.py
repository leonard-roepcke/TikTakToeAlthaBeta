from core import Core
from gameState import GameState
from ui import Ui
core = Core(GameState())
ui = Ui
ui.draw(core.gameState)
ui.get_input(core.gameState)
