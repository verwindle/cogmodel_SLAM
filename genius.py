
from ipywidgets import Button
from IPython.display import display, Markdown, clear_output


button = Button(
    description='К чему?',
    disabled=False,
    button_style='danger',
    tooltip="I'm waiting"
)

OPEN = 0

def eventhandler(b):
    if not OPEN:
        display(Markdown('genius.md'))
        globals()['OPEN'] = 1
    else:
        b.description = 'No way back'
        display(button)
        globals()['OPEN'] = 0
    
button.on_click(eventhandler)
display(button)
