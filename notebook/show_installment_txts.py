
from ipywidgets import Dropdown
from IPython.display import display, HTML, clear_output

txts = ['../media/installments_ros_ml_main.txt', '../media/installments_aftermath_cartographer.txt']
EMPTY = '--'

def display_txt(file):
    with open (file) as f:
        text = f.read().split('\n')
        display(*text)
        
def dropdown_eventhandler(change):
    if (change.new == EMPTY):
        clear_output(wait=True)
        display(dropdown)
    else:
        clear_output(wait=True)
        display(dropdown)
        digit = change.new.split()[-1]
        display_txt(txts[0]) if digit == 1 else display_txt(txts[1])
        
dropdown = Dropdown(
    options=['--', 'Заметки часть 1', 'Заметки часть 2'],
    value='--',
    description='Пара .txt',
    disabled=False)

dropdown.observe(dropdown_eventhandler, names='value')
display(dropdown)
