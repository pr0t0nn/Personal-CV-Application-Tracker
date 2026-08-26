import customtkinter as ctk
from tkinter import filedialog
import backend

class BasePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

class ApplicationsPage(BasePage):
    def __init__(self, parent, controller, application_amount: int = 0):
        super().__init__(parent, controller)

        self.application_amount = application_amount

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.TitleLabel = ctk.CTkLabel(self, text="PROTON'S PERSONAL CV TRACKER", border_width=3, corner_radius=10)
        self.TitleLabel.grid(row=0, column=1, padx=20, pady=20)

        self.AddApplicationButton = ctk.CTkButton(self, text="Add Application", command=self.add_new_application, border_width=3, corner_radius=10)
        self.AddApplicationButton.grid(row=0, column=2, padx=20, pady=20, sticky="e")

        self.ApplicationContainer = ctk.CTkScrollableFrame(self)
        self.ApplicationContainer.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=20, pady=10)

        self.refresh_applications_list()

    def refresh_applications_list(self):
        for widget in self.ApplicationContainer.winfo_children():
            widget.destroy()

        for i in range(self.application_amount):
            ApplicationButton = ctk.CTkButton(
                self.ApplicationContainer, 
                text=f"Application #{i + 1}", 
                height=40,
                command=lambda num=i+1: self.controller.show_page(ApplicationPage, application_number=num)
            )
            ApplicationButton.pack(fill="x", expand=True, padx=5, pady=5)

    def add_new_application(self):
        self.application_amount += 1
        self.refresh_applications_list()

import customtkinter as ctk
from tkinter import filedialog

class ApplicationPage(BasePage):
    def __init__(self, parent, controller, application_number):
        super().__init__(parent, controller)
        
        self.application_number = application_number
        
        self.ViewText = ctk.CTkLabel(self, text=f"Viewing Application #{application_number}", font=("Arial", 20, "bold"))
        self.ViewText.pack(pady=40)
        
        self.BackButton = ctk.CTkButton(self, text="Back to List", command=lambda: controller.show_page(ApplicationsPage, application_amount=controller.app_count))
        self.BackButton.pack(pady=10)

        self.AddCVButton = ctk.CTkButton(self, text="Add CV", command=self.OpenFileExplorer)
        self.AddCVButton.pack(pady=10)

    def OpenFileExplorer(self):
        file_path = filedialog.askopenfilename(
            title="Select ur CV File",
            filetypes=[
                ("PDF Files", "*.pdf"),
                ("Word Documents", "*.docx"), 
                ("All files", "*.*")
            ]
        )

        if file_path:
            FileSuccess = ctk.CTkLabel(self, text="CV Selected", fg_color="green", corner_radius=10, text_color="white")
            FileSuccess.pack(pady=10)
            self.SendFileToDB(file_path)
            self.after(1500, FileSuccess.destroy)
        else:
            FileFail = ctk.CTkLabel(self, text="CV Not Selected", fg_color="red", corner_radius=10, text_color="white")
            FileFail.pack(pady=10)
            self.after(1500, FileFail.destroy)

    def SendFileToDB(self, FilePath):
        backend.SaveCV(FilePath)

class AppController(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.applications_data = backend.GetApplications()
        self.app_count = len(self.applications_data)

        self.title("Proton's CV Application")
        self.geometry("600x600")
        self.resizable(True, True)

        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        self.current_page = None

        self.show_page(ApplicationsPage, application_amount=self.app_count)

    def show_page(self, page_class, **kwargs):
        if self.current_page is not None:
            self.current_page.destroy()

        self.current_page = page_class(self.container, self, **kwargs)
        self.current_page.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = AppController()
    app.mainloop()