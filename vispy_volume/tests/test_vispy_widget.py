import numpy as np
from ..vispy_widget import QtVispyWidget

class Event(object):
    def __init__(self, text):
        self.text = text

def test_widget():

    # Create fake data
    data = np.arange(1000).reshape((10,10,10))

    # Set up widget
    w = QtVispyWidget()
    w.set_data(data)
    w.set_canvas()
    w.canvas.render()

    # Test changing colormap
    w.set_colormap()

    # Test key presses
    w.on_key_press(Event(text='1'))
    w.on_key_press(Event(text='2'))
    w.on_key_press(Event(text='3'))