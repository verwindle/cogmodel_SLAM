
from ipywidgets import ToggleButtons
from IPython.display import display, Markdown, HTML, clear_output


button = ToggleButtons(
    options=['Желаемое', 'Действительное'],
    button_style='danger',
    tooltips=["I'm waiting", "I'm waiting"],
    icons=['check'] * 2
)

OUT = 1

def eventhandler(b):
    if not OUT:
        clear_output(wait=True)
        display(button)
        display(HTML('<iframe width="720" height="480" src="https://www.youtube.com/embed/EOdA5X-K8H8" frameborder="1" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'));
        globals()['OUT'] = 1
    else:
        clear_output(wait=True)
        display(button)
        display(Markdown('fail.md'))
        globals()['OUT'] = 0
    
    
button.observe(eventhandler)
display(button)
display(HTML('<iframe width="720" height="480" src="https://www.youtube.com/embed/EOdA5X-K8H8" frameborder="1" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'));
