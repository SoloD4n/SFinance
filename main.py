from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from ui_layouts import MainMenu, Operations, Analytics, Goals, History, Profile


class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenu(name="main"))
        sm.add_widget(Operations(name="ops"))
        sm.add_widget(Analytics(name="analytics"))
        sm.add_widget(Goals(name="goals"))
        sm.add_widget(History(name="history"))
        sm.add_widget(Profile(name="profile"))
        return sm


if __name__ == "__main__":
    MainApp().run()
