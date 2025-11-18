from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Kivy App that dynamically adds labels."""

    def __init__(self, **kwargs):
        """Initialize list of names."""
        super().__init__(**kwargs)
        self.names = ["Jim", "Joe", "John", "Jon", "Jose", "Robert", "Rob", "Dude"]

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_label()
        return self.root

    def create_label(self):
        """Create labels from list and add them dynamically."""
        for name in self.names:
            dynamic_label = Label(text=name)
            self.root.ids.main.add_widget(dynamic_label)


DynamicLabelsApp().run()
