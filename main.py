from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window


class ScreenMenu(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def go_game(self):
        self.manager.current = "game"

    def go_shop(self):
        self.manager.current = "shop"


class ScreenGame(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def back(self):
        self.manager.current = "menu"


class ScreenShop(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def back(self):
        self.manager.current = "menu"


class ClickerApp(App):
    def build(self):
        screen_menu = ScreenMenu(name="menu")
        screen_game = ScreenGame(name="game")
        screen_shop = ScreenShop(name="shop")

        screen_manager = ScreenManager()
        screen_manager.add_widget(screen_menu)
        screen_manager.add_widget(screen_game)
        screen_manager.add_widget(screen_shop)

        return screen_manager


Window.size = (350, 810)
Window.top = 30
app = ClickerApp()

app.run()