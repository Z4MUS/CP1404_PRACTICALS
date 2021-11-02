from kivy.app import App
from kivy.lang import Builder
# from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class ConvertMilesToKm(App):

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, increment):
        value = self.get_validated_miles() + increment
        self.root.ids.input_number.text = str(value)
        self.handle_conversion()

    def handle_conversion(self):
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_number.text = str(result)

    def get_validated_miles(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


ConvertMilesToKm().run()
