from IPython.display import display, HTML, clear_output
from ipywidgets import FloatSlider

fSlider = FloatSlider(
    value=8.,
    min=0,     
    max=10.,  
    step=0.5,
    description='Балл:',
    continuous_update=False,
    orientation='horizontal'  # Горизонтальное или вертикальное расположение
)

def on_value_change(b):
    msg = 'Спасибо за высокую оценку' if fSlider.value >= 8. else 'Понял, в следующий раз будет лучше'
    clear_output(wait=True)
    display(fSlider)
    display(HTML(f"<font color=#D61100 size=4>{msg}</font>"))

fSlider.observe(on_value_change, names='value')
display(fSlider)
