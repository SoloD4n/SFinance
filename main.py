from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen


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


class MainMenu(Screen):
    def on_enter(self, *args):
        self.clear_widgets()
        btn_layout = BoxLayout(orientation="horizontal", padding=40, spacing=5)
        lb_greet = Label(text="Добро пожаловать в SFinance!", font_size=96)
        btn_ops = Button(text="Операции", size_hint=(0.2, 0.3))
        btn_analytics = Button(text="Аналитика", size_hint=(0.2, 0.3))
        btn_goals = Button(text="Цели/бюджет", size_hint=(0.2, 0.3))
        btn_history = Button(text="История", size_hint=(0.2, 0.3))
        btn_profile = Button(text="Профиль", size_hint=(0.2, 0.3))
        main_layout = BoxLayout(orientation="vertical", padding=40, spacing=5)

        btn_layout.add_widget(btn_ops)
        btn_layout.add_widget(btn_analytics)
        btn_layout.add_widget(btn_goals)
        btn_layout.add_widget(btn_history)
        btn_layout.add_widget(btn_profile)
        main_layout.add_widget(lb_greet)
        main_layout.add_widget(btn_layout)

        btn_ops.bind(on_press=self.btn_ops_clicked)
        btn_analytics.bind(on_press=self.btn_analyse_clicked)
        btn_goals.bind(on_press=self.btn_goals_clicked)
        btn_history.bind(on_press=self.btn_history_clicked)
        btn_profile.bind(on_press=self.btn_profile_clicked)
        self.add_widget(main_layout)

    def btn_ops_clicked(self, instance):
        self.manager.current = "ops"

    def btn_analyse_clicked(self, instance):
        self.manager.current = "analytics"

    def btn_goals_clicked(self, instance):
        self.manager.current = "goals"

    def btn_history_clicked(self, instance):
        self.manager.current = "history"

    def btn_profile_clicked(self, instance):
        self.manager.current = "profile"


class Operations(Screen):
    def on_enter(self, *args):
        self.clear_widgets()
        layout = BoxLayout(orientation="vertical", padding=40, spacing=5)
        label = Label(text="Скоро тут что то появится", font_size=48)
        btn_back = Button(text="В главное меню", size_hint=(0.2, 0.3))
        btn_layout = BoxLayout(orientation="horizontal", padding=40, spacing=5)
        layout.add_widget(label)
        btn_layout.add_widget(btn_back)
        layout.add_widget(btn_layout)

        btn_back.bind(on_press=self.btn_back_clicked)
        self.add_widget(layout)

    def btn_back_clicked(self, instance):
        self.manager.current = "main"


class Analytics(Screen):
    def on_enter(self, *args):
        self.clear_widgets()
        layout = BoxLayout(orientation="vertical", padding=40, spacing=5)
        label = Label(text="Скоро тут что то появится", font_size=48)
        btn_back = Button(text="В главное меню", size_hint=(0.2, 0.3))
        btn_layout = BoxLayout(orientation="horizontal", padding=40, spacing=5)
        layout.add_widget(label)
        btn_layout.add_widget(btn_back)
        layout.add_widget(btn_layout)

        btn_back.bind(on_press=self.btn_back_clicked)
        self.add_widget(layout)

    def btn_back_clicked(self, instance):
        self.manager.current = "main"


class Goals(Screen):
    def on_enter(self, *args):
        self.clear_widgets()
        layout = BoxLayout(orientation="vertical", padding=40, spacing=5)
        label = Label(text="Скоро тут что то появится", font_size=48)
        btn_back = Button(text="В главное меню", size_hint=(0.2, 0.3))
        btn_layout = BoxLayout(orientation="horizontal", padding=40, spacing=5)
        layout.add_widget(label)
        btn_layout.add_widget(btn_back)
        layout.add_widget(btn_layout)

        btn_back.bind(on_press=self.btn_back_clicked)
        self.add_widget(layout)

    def btn_back_clicked(self, instance):
        self.manager.current = "main"


class History(Screen):
    def on_enter(self, *args):
        self.clear_widgets()
        layout = BoxLayout(orientation="vertical", padding=40, spacing=5)
        label = Label(text="Скоро тут что то появится", font_size=48)
        btn_back = Button(text="В главное меню", size_hint=(0.2, 0.3))
        btn_layout = BoxLayout(orientation="horizontal", padding=40, spacing=5)
        layout.add_widget(label)
        btn_layout.add_widget(btn_back)
        layout.add_widget(btn_layout)

        btn_back.bind(on_press=self.btn_back_clicked)
        self.add_widget(layout)

    def btn_back_clicked(self, instance):
        self.manager.current = "main"


class Profile(Screen):
    def on_enter(self, *args):
        self.clear_widgets()
        layout = BoxLayout(orientation="vertical", padding=40, spacing=5)
        label = Label(text="Скоро тут что то появится", font_size=48)
        btn_back = Button(text="В главное меню", size_hint=(0.2, 0.3))
        btn_layout = BoxLayout(orientation="horizontal", padding=40, spacing=5)
        layout.add_widget(label)
        btn_layout.add_widget(btn_back)
        layout.add_widget(btn_layout)

        btn_back.bind(on_press=self.btn_back_clicked)
        self.add_widget(layout)

    def btn_back_clicked(self, instance):
        self.manager.current = "main"


if __name__ == '__main__':
    MainApp().run()
