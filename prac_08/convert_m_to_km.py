from kivy.app import App
from kivy.lang import Builder


MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km.kv')
        return self.root

    def handle_convert(self):
        miles = self.get_valid_miles()
        km = miles * MILES_TO_KM
        self.root.ids.output_label.text = f"{km:.5f}"

    def handle_increment(self, amount):
        miles = self.get_valid_miles()
        miles += amount
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert()

    def get_valid_miles(self):
        text = self.root.ids.input_miles.text
        try:
            return float(text)
        except ValueError:
            return 0.0

MilesConverterApp().run()