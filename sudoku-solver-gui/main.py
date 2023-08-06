import PySimpleGUI as sg

square: dict = {'size': (2, 1), 'font': ('Franklin Gothic Book', 14), 'justification': 'center',
                'background_color': 'white', 'text_color': 'black'}


def nine_squares():
    return [
        [sg.Text('', **square), sg.Text('', **square), sg.Text('', **square)],
        [sg.Text('', **square), sg.Text('', **square), sg.Text('', **square)],
        [sg.Text('', **square), sg.Text('', **square), sg.Text('', **square)]
    ]


def nine_horizontal_squares():
    return [
        sg.Text('', **square), sg.Text('', **square), sg.Text('', **square),
        sg.Text('|'),
        sg.Text('', **square), sg.Text('', **square), sg.Text('', **square),
        sg.Text('|'),
        sg.Text('', **square), sg.Text('', **square), sg.Text('', **square)
    ]


def vertical_separators():
    return [
        sg.Text('-------------------------------------------'
                '-------------------------------------------')
    ]


layout: list = [
    nine_horizontal_squares(), nine_horizontal_squares(), nine_horizontal_squares(),
    vertical_separators(),
    nine_horizontal_squares(), nine_horizontal_squares(), nine_horizontal_squares(),
    vertical_separators(),
    nine_horizontal_squares(), nine_horizontal_squares(), nine_horizontal_squares()
]

window = sg.Window('Sudoku Solver', layout=layout, background_color="black", size=(380, 600),
                   return_keyboard_events=True)

while True:
    event, values = window.read()
    print(event)
    if event is None:
        break
