from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
import ui_control


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
        ui_control.btn_ops_clicked(self, instance)

    def btn_analyse_clicked(self, instance):
        ui_control.btn_analyse_clicked(self, instance)

    def btn_goals_clicked(self, instance):
        ui_control.btn_goals_clicked(self, instance)

    def btn_history_clicked(self, instance):
        ui_control.btn_history_clicked(self, instance)

    def btn_profile_clicked(self, instance):
        ui_control.btn_profile_clicked(self, instance)


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
        ui_control.btn_back_clicked(self, instance)


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
        ui_control.btn_back_clicked(self, instance)


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
        ui_control.btn_back_clicked(self, instance)


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
        ui_control.btn_back_clicked(self, instance)


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
        ui_control.btn_back_clicked(self, instance)


class LoginScreen(Screen):
    def on_enter(self, *args):
        self.clear_widgets()
        layout = BoxLayout(orientation="vertical", padding=40, spacing=20)

        self.lbl_info = Label(text="Введите логин и пароль", font_size=48)
        self.txt_username = TextInput(hint_text="Логин", multiline=False, size_hint=(0.4, 0.15),
                                      pos_hint={"x": 0.3})
        self.txt_password = TextInput(hint_text="Пароль", password=True, multiline=False, size_hint=(0.4, 0.15),
                                      pos_hint={"x": 0.3})
        btn_login = Button(text="Войти", size_hint=(0.4, 0.2), pos_hint={"x": 0.3})

        btn_login.bind(on_press=self.try_login)

        layout.add_widget(self.lbl_info)
        layout.add_widget(self.txt_username)
        layout.add_widget(self.txt_password)
        layout.add_widget(btn_login)

        self.add_widget(layout)

    def try_login(self, instance):
        ui_control.try_login(self, instance)
