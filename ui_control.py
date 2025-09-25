import app_logic


def btn_ops_clicked(screen, instance):
    screen.manager.current = "ops"


def btn_analyse_clicked(screen, instance):
    screen.manager.current = "analytics"


def btn_goals_clicked(screen, instance):
    screen.manager.current = "goals"


def btn_history_clicked(screen, instance):
    screen.manager.current = "history"


def btn_profile_clicked(screen, instance):
    screen.manager.current = "profile"


def btn_back_clicked(screen, instance):
    screen.manager.current = "main"


def try_login(self, instance):
    username = self.txt_username.text.strip()
    password = self.txt_password.text.strip()

    if app_logic.check_credentials(username, password):
        self.manager.current = "main"
    else:
        self.lbl_info.text = "Доступ запрещен!"
        self.lbl_info.color = (1, 0, 0, 1)
