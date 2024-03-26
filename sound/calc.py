from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.size = (300, 450)
Window.clearcolor = (32/255, 32/255, 32/255, 1)
Window.set_title("Калькулятор")

class MyApp(App):

    def update_label(self):
        self.lbl.text = self.formula

    def add_numb(self, instance):
        if self.formula == "0":
            self.formula = ""
        
        self.formula += str(instance.text)
        self.update_label()

    def add_oper(self, instance):
        if str(instance.text).lower() == "x":
            self.formula += "*"
        else:
            self.formula += str(instance.text)
        self.update_label()
    
    def res(self, instance):
        self.lbl.text = str(eval(self.lbl.text))
        self.formula = "0"

    def build(self):
        self.formula = "0"
        gl = GridLayout(cols=4, size_hint=(1, .65), spacing=2)
        bl = BoxLayout(orientation="vertical", padding=10)
        
        self.lbl = Label(text="0", font_size=40, size_hint = (1, .35), color=[1, 1, 1, 1], text_size=(300-20, 450*.35-20), halign="right", valign="center")

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

        gl.add_widget(Widget())
        gl.add_widget(Button(text="0", on_press=self.add_numb))
        gl.add_widget(Button(text=".", on_press=self.add_numb))
        gl.add_widget(Button(text="=", on_press=self.res))

        bl.add_widget(self.lbl)
        bl.add_widget(gl)

        return bl

if __name__ == "__main__":
    MyApp().run()