import customtkinter as ctk


class BasePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

class ApplicationsPage(BasePage):
    def __init__(self, parent, controller):
            super().__init__(parent, controller)

            self.title = ctk.CTkLabel(self, text="PROTON'S PERSONAL CV TRACKER", border_width=3, corner_radius=10)
            self.title.grid(padx=40, pady=40)

class ApplicationPage(BasePage):
    pass

class Add_ApplicationPage(BasePage):
    pass

class AppController(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Proton's CV Application")
        self.geometry("600x600")
        self.resizable(True,True)

        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        self.current_page = None

        self.show_page(ApplicationsPage)

    def show_page(self, page_class):
        if self.current_page is not None:
            self.current_page.destroy()

        self.current_page = page_class(self.container, self)
        self.current_page.pack(fill="both", expand=True)

app = AppController()
app.mainloop()