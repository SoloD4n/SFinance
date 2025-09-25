from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from ui_layouts import LoginScreen, MainMenu, Operations, Analytics, Goals, History, Profile
import app_logic


class MainApp(App):
    def build(self):
        app_logic.init_db()

        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(MainMenu(name="main"))
        sm.add_widget(Operations(name="ops"))
        sm.add_widget(Analytics(name="analytics"))
        sm.add_widget(Goals(name="goals"))
        sm.add_widget(History(name="history"))
        sm.add_widget(Profile(name="profile"))

        sm.current = "login"
        return sm


if __name__ == "__main__":
    MainApp().run()
