
from ipywidgets import Dropdown
from IPython.display import display, clear_output, Markdown, HTML

def _display(arg):
    display(HTML("""
        <style>
        .output {
            display: flex;
            align-items: center;
            text-align: right;
        }
        </style>
        """), arg)

EMPTY = '--'
def dropdown_eventhandler(change):
    if (change.new == EMPTY):
        clear_output(wait=True)
        _display(dropdown)
    else:
        clear_output(wait=True)
        _display(dropdown)
        _display(Markdown(f'{change.new}.md'))

dropdown = Dropdown(
    options=['--', 'ros', 'rosdep', 'gazebo', 'rtabmap'],
    value='--',
    description='tools:',
    disabled=False)

dropdown.observe(dropdown_eventhandler, names='value')
_display(dropdown)
