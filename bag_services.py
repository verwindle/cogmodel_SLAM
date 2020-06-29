
from ipywidgets import ToggleButtons
from IPython.display import display, Markdown, clear_output


button = ToggleButtons(
    options=['Улица', 'Помещение'],
    button_style='danger',
    tooltips=["I'm waiting", "I'm waiting"],
    icons=['check'] * 2
)

OUT = 1

def eventhandler(b):
    if not OUT:
        clear_output(wait=True)
        display(button)
        display(Markdown('outdoor.md'))
        globals()['OUT'] = 1
    else:
        clear_output(wait=True)
        display(button)
        display(Markdown('indoor.md'))
        globals()['OUT'] = 0
    
    
button.observe(eventhandler)
display(button)
display(Markdown('outdoor.md'))
