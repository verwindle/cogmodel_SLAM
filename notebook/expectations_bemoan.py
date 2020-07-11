
from ipywidgets import Button
from IPython.display import display, Markdown, clear_output

button = Button(
    description='Секция неудач',
    disabled=False,
    button_style='danger',
    tooltip="danger"
)

OPEN = 0

def eventhandler(b):
    if not OPEN:
        display(Markdown('expectations_bemoan.md'))
        b.description = 'Не смотреть'
        globals()['OPEN'] = 1
    else:
        clear_output(wait=True)
        b.description = 'Секция неудач'
        display(button)
        globals()['OPEN'] = 0
    
button.on_click(eventhandler)
display(button)
