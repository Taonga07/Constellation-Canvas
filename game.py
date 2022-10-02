from ursina import *

app = Ursina()

wp = WindowPanel(
    title='Custom Window',
    content=(
        Text('Name:'),
        InputField(name='name_field'),
        Button(text='Submit', color=color.azure),
        ,
        Slider(),
        ),
        popup=False,
        enabled=False
    )

def input(key):
    if key == 'space':
        wp.enabled = True


app.run()