from gameState import GameState
class Ui:
    
    def __init__(self):
        pass

    def draw(gameState: GameState):
        CHAR_MAP = {0:" ", 1:"X", -1:"O"}
        board = gameState.data
        for i in range(3):
            print(
                f" {CHAR_MAP[board[i][0]]} | {CHAR_MAP[board[i][1]]} | {CHAR_MAP[board[i][2]]} "
            )
            if i < 2:
                print("---+---+---")
