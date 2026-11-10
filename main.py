from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class ScreenMenu(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        button1 = Button(text="play")
        label1 = Label(text="clicker")
        box = BoxLayout(orientation="vertical")

        button1.on_press = self.go_game

        box.add_widget(label1)
        box.add_widget(button1)

        self.add_widget(box)

    def go_game(self):
        self.manager.current = "game"

    
class ScreenGame(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        button1 = Button(text="back")
        label1 = Label(text="game start")
        box = BoxLayout(orientation="vertical")

        button1.on_press = self.back
        
        box.add_widget(label1)
        box.add_widget(button1)

        self.add_widget(box)

    def back(self):
            self.manager.current = "menu"

class ClickerApp(App):
    def build(self):
        screen_menu = ScreenMenu(name="menu")
        screen_game = ScreenGame(name="game")

        screen_manager = ScreenManager()
        screen_manager.add_widget(screen_menu)
        screen_manager.add_widget(screen_game)

        return screen_manager

app = ClickerApp()

app.run()
