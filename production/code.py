from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
import board

keyboard = KMKKeyboard()
#col 1,2,3,4
keyboard.col_pins = (board.D1, board.D2, board.D3, board.D4)
#row 1,2,3
keyboard.row_pins = (board.D0, board.D5, board.D6)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
    KC.Q,       KC.E,       KC.W,       KC.R,
    KC.LSFT,    KC.A,       KC.S,       KC.D,
    KC.LCTL,    KC.SPC,     KC.C,       KC.F,
    ]
]

if __name__== '__main__':
        keyboard.go()