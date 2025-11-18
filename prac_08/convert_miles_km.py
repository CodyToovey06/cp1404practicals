from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KM_CONVERSION = 1.60934


class ConvertMilesToKmApp(App):
    """Program to convert miles to km."""
    output_message = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (200, 100)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculation(self):
        """Handle Kilometers conversion."""
        miles = self.get_valid_number()
        self.handle_update(miles)

    def handle_increment(self, increment):
        """Update text input based on up and down button increments."""
        miles = self.get_valid_number() + increment
        self.root.ids.input_miles.text = str(miles)

    def handle_update(self, miles):
        """Update display with calculated conversions."""
        self.output_message = str(miles * MILES_TO_KM_CONVERSION)

    def get_valid_number(self):
        """Get valid float from text input."""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0.0


ConvertMilesToKmApp().run()
