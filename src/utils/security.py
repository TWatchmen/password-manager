


class PasswordSecurity:
    def __init__(self, popup_ui):
        self.popup_window = popup_ui
        return

    def check_password_strength(self, event=None):
        password = self.popup_window.password_entry.get()

        self.popup_window.password_strength_indicator_1.configure(bg="lightgrey")
        self.popup_window.password_strength_indicator_2.configure(bg="lightgrey")
        self.popup_window.password_strength_indicator_3.configure(bg="lightgrey")

        length = len(password)

        if length >= 5:
            self.popup_window.password_strength_indicator_1.config(bg="red")

        if length >= 5 and (password.isalpha() is False or password.isalnum() is False):
            self.popup_window.password_strength_indicator_1.config(bg="red")
            self.popup_window.password_strength_indicator_2.config(bg="yellow")

        if length >= 5 and password.isalnum() is False and password.isalpha() is False:
            self.popup_window.password_strength_indicator_1.config(bg="yellow")
            self.popup_window.password_strength_indicator_2.config(bg="yellow")
            self.popup_window.password_strength_indicator_3.config(bg="yellow")

        if length >= 8:
            self.popup_window.password_strength_indicator_2.config(bg="yellow")

        if length >= 8 and password.isalpha() is False:
            self.popup_window.password_strength_indicator_3.config(bg="green")

        if length >= 8 and password.isalpha() is False and password.isalnum() is False:
            self.popup_window.password_strength_indicator_1.config(bg="green")
            self.popup_window.password_strength_indicator_2.config(bg="green")
            self.popup_window.password_strength_indicator_3.config(bg="green")



class DatabaseSecurity:
    def __init__(self):
        return

