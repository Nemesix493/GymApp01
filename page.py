from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label


class Page(StackLayout):
    def __init__(self, name: str, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.label = Label(text=self.name)
        self.add_widget(self.label)
