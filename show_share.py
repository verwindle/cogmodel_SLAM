from ipywidgets import Button
from IPython.display import display, Markdown, clear_output


button = Button(
    description='Показать все',
    disabled=False,
    button_style='danger',
    tooltip="I'm waiting"
)

OPEN = 0

def eventhandler(b):
    if not OPEN:
        display(Markdown('ros_share.md'))
        b.description = 'Скрыть все'
        globals()['OPEN'] = 1
    else:
        clear_output(wait=True)
        b.description = 'Показать все'
        display(button)
        globals()['OPEN'] = 0
    
button.on_click(eventhandler)
display(button)
