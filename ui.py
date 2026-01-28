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
    def get_input(gameState: GameState):
        player = sum([cell for row in gameState.data for cell in row]) * -1
        if not player: player = 1
        player_char = "X" if player == 1 else "O"
        print("player: ", player_char, " ist dran.")

