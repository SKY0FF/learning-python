from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.textinput import TextInput
from random import randint

Window.size = (300, 300)
Window.title = "Конвертер"
Config.set('graphics', 'resizable', False)


class MyApp(App):

    def __init__(self):
        super().__init__()
        self.label = Label(text="Конвертер", font_size = 30)
        self.mili = Label(text="Мили: ")
        self.metr = Label(text="Метры: ")
        self.cantimetr = Label(text="Сантиметры: ")
        self.input_data = TextInput(hint_text="Введите значение (км): ", multiline = False)
        self.input_data.bind(text=self.text)

    def build(self):
        bl = BoxLayout(orientation = "vertical")
        bl.add_widget(self.label)
        bl.add_widget(self.input_data)
        bl.add_widget(self.mili)
        bl.add_widget(self.metr)
        bl.add_widget(self.cantimetr)

        return bl
    
    def text(self, *args):
        data = self.input_data.text
        if data.isdigit():
            self.mili.text = f"Мили: {(float(data)*0.62)}"
            self.metr.text = f"Метры: {float(data)*1000}"
            self.cantimetr.text = f"Сантиметры: {float(data)*100000}"
        else:
            self.input_data.text = ''

    def yes(self, instance):
        instance.text = "Thx u"
        instance.background_color = [0, 1, 0, 1]
        self.label.color=(randint(0, 255)/255, randint(0, 255)/255, randint(0, 255)/255)
    
if __name__ == "__main__":
    MyApp().run()