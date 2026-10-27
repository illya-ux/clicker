from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class ClickerApp(App):
    def build(self):
        button1 = Button(text="text")
        label1 = Label(text="clicker")
        box = BoxLayout(orientation="vertical")
        box.add_widget(label1)
        box.add_widget(button1)

        return box


app = ClickerApp()

app.run()
