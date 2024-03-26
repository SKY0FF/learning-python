from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.scatter import Scatter
from kivy.uix.boxlayout import BoxLayout

#Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '350')

class MyApp(App):
    def build(self):
        bl = BoxLayout(orientation = "horizontal", padding=[50], spacing=50)
        #bl = BoxLayout(size = (300, 300))
        bl.add_widget(Button(
                text = "This my first button!", 
                font_size = 30,
                on_press = self.btn_press,
                background_normal = '',
                background_color = [1, 0, 0, 1],))
                #size_hint = (.5, .25),
                #pos = (700/2 - (700 * 0.5 / 2), 350/2 - (350 * 0.25 / 2))))

        bl.add_widget(Button(
                text = "This my first button!(2)", 
                font_size = 30,
                on_press = self.btn_press,
                background_normal = '',
                background_color = [1, 0, 0, 1],))
                #size_hint = (.5, .25),
                #pos = (700/2 - (700 * 0.5 / 2), 350/2 - (350 * 0.25 / 2))))
        
        bl.add_widget(Button(
                text = "This my first button!(3)", 
                font_size = 30,
                on_press = self.btn_press,
                background_normal = '',
                background_color = [1, 0, 0, 1],))
                #size_hint = (.5, .25),
                #pos = (700/2 - (700 * 0.5 / 2), 350/2 - (350 * 0.25 / 2))))

        return bl
    
    def btn_press(self, instance):
        print("Кнопка нажата")
        instance.text = "Я нажата!"
        instance.background_color = [0, 1, 0, 1]
    

if __name__ == "__main__":
    MyApp().run()