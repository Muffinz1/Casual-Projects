import PySimpleGUI as Sg
from time import time


def convert_pos_to_pixel(cell):
    t1 = cell[0] * cell_size, cell[1] * cell_size
    b1 = t1[0] + cell_size, t1[1] + cell_size
    return t1, b1


field_size = 400
cell_count = 10
cell_size = field_size/cell_count
# Snake
snake_body = [(4, 4), (3, 4), (2, 4)]
x_directions = {'left': (-1, 0), 'right': (1, 0),
                'down': (0, -1), 'up': (0, 1)}
directions = x_directions['up']
# fruit
fruit_spawn = (0, 0)

Sg.theme('GreenMono')
field = Sg.Graph(
        canvas_size=(field_size, field_size),
        graph_bottom_left=(0, 0),
        graph_top_right=(field_size, field_size),
        background_color='Azure'
        )
layout = [[field]]
window = Sg.Window('الثعبان الثحلان', layout, return_keyboard_events=True)
start_time = time()
while True:
    event, values = window.read(timeout=10)
    if event == Sg.WIN_CLOSED:
        break

    if event == 'Left:37':
        print('left')
    if event == 'Up:38':
        print('up')
    if event == 'Right:39':
        print('right')
    if event == 'Down:40':
        print('down')

    time_since_start = time() - start_time
    if time_since_start >= 0.5:
        start_time = time()
        # snake drawing renders update
        new_head = (snake_body[0][0] + directions[0], snake_body[0][1] + directions[1])
        snake_body.insert(0, new_head)
        snake_body.pop()
        field.DrawRectangle((0, 0),(field_size, field_size),'azure')
        # draw fruit
        f1, f2 = convert_pos_to_pixel(fruit_spawn)
        field.DrawRectangle(f1, f2, 'yellow')
        # draw snake
        for index, section in enumerate(snake_body):
            s1, s2 = convert_pos_to_pixel(section)
            color = 'black' if index == 0 else 'green'
            field.DrawRectangle(s1, s2, color)
window.close()
