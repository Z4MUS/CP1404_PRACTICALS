from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.label import Label


class DynamicLabels(App):

    def __init__(self,):
        super().__init__()
        self.names = ["smith", "jones", "sam", "sarah", "bob", "stephanie"]

    def build(self):
        """Build the Kivy app from the kv file """
        Window.size = (300, 300)
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create label from list entries and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabels().run()