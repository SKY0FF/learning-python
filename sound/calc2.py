from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
#from kivy.core.window import Window
from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '450')
#Window.set_title("Calculator")
#Window.clearcolor = [32/255, 32/255, 32/255, 1]

class CalculatorApp(App):

    def update_lbl(self):
        self.lbl.text = self.formula

    def add_numb(self, instance):
        if self.formula == "0":
            self.formula = ""
        self.formula += str(instance.text)
        self.update_lbl()
    
    def add_oper(self, instance):
        if str(instance.text).lower() == "x":
            self.formula += "*"
        else:
            self.formula += str(instance.text)
        self.update_lbl()
    
    def result(self, instance):
        self.lbl.text = str(eval(self.lbl.text))
        self.formula = "0"

    def build(self):
        gl = GridLayout(cols=4, spacing=3, size_hint = (1, .65))

        bl = BoxLayout(orientation="vertical", padding=5)
        self.lbl = Label(text="0", size_hint=(1, .35), halign="right", valign="center", font_size=40, text_size=(300-10, 450*.35-10))
        self.formula = "0"

        gl.add_widget(Button(text="7", on_press=self.add_numb))
        gl.add_widget(Button(text="8", on_press=self.add_numb))
        gl.add_widget(Button(text="9", on_press=self.add_numb))
        gl.add_widget(Button(text="X", on_press=self.add_oper))

        gl.add_widget(Button(text="4", on_press=self.add_numb))
        gl.add_widget(Button(text="5", on_press=self.add_numb))
        gl.add_widget(Button(text="6", on_press=self.add_numb))
        gl.add_widget(Button(text="-", on_press=self.add_oper))

        gl.add_widget(Button(text="1", on_press=self.add_numb))
        gl.add_widget(Button(text="2", on_press=self.add_numb))
        gl.add_widget(Button(text="3", on_press=self.add_numb))
        gl.add_widget(Button(text="+", on_press=self.add_oper))

        gl.add_widget(Button(text="/", on_press=self.add_oper))
        gl.add_widget(Button(text="0", on_press=self.add_numb))
        gl.add_widget(Button(text=".", on_press=self.add_numb))
        gl.add_widget(Button(text="=", on_press=self.result))

        bl.add_widget(self.lbl)
        bl.add_widget(gl)

        return bl

if __name__ == "__main__":
    CalculatorApp().run()