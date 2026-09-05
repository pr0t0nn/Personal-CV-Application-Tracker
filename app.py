import customtkinter as ctk
from tkinter import filedialog
from datetime import date
import backend

class BasePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

class ApplicationsPage(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

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

        for record in self.controller.applications_data:
            company_name = record[1]
            application_date = record[2]
            status = record[4]
            ApplicationButton = ctk.CTkButton(
                self.ApplicationContainer,
                text=f"{company_name}    {application_date}    {status}",
                height=40,
                command=lambda application=record: self.controller.show_page(ApplicationPage, application=application)
            )
            ApplicationButton.pack(fill="x", expand=True, padx=5, pady=5)

    def add_new_application(self):
        self.controller.show_page(ApplicationPage)

class ApplicationPage(BasePage):
    def __init__(self, parent, controller, application=None):
        super().__init__(parent, controller)

        self.application = application
        self.cv_path = application[3] if application else ""

        header = f"Viewing {application[1]}" if application else "New Application"
        self.HeaderLabel = ctk.CTkLabel(self, text=header, font=("Arial", 20, "bold"))
        self.HeaderLabel.pack(pady=20)

        self.CompanyEntry = ctk.CTkEntry(self, placeholder_text="Company Name", width=300)
        self.CompanyEntry.pack(pady=10)

        self.DateEntry = ctk.CTkEntry(self, placeholder_text="Application Date", width=300)
        self.DateEntry.pack(pady=10)

        if application:
            self.CompanyEntry.insert(0, application[1])
            self.DateEntry.insert(0, application[2])
        else:
            self.DateEntry.insert(0, str(date.today()))

        self.AddCVButton = ctk.CTkButton(self, text="Add CV", command=self.OpenFileExplorer)
        self.AddCVButton.pack(pady=10)

        self.CVLabel = ctk.CTkLabel(self, text=self.cv_path if self.cv_path else "No CV Selected")
        self.CVLabel.pack(pady=5)

        if application:
            self.StatusLabel = ctk.CTkLabel(self, text=f"Status: {application[4]}", font=("Arial", 14, "bold"))
            self.StatusLabel.pack(pady=10)

            self.StatusButtons = ctk.CTkFrame(self, fg_color="transparent")
            self.StatusButtons.pack(pady=5)

            self.PassedButton = ctk.CTkButton(self.StatusButtons, text="Passed", fg_color="green", hover_color="darkgreen", command=lambda: self.SetStatus("Passed"))
            self.PassedButton.pack(side="left", padx=10)

            self.FailedButton = ctk.CTkButton(self.StatusButtons, text="Failed", fg_color="red", hover_color="darkred", command=lambda: self.SetStatus("Failed"))
            self.FailedButton.pack(side="left", padx=10)
        else:
            self.SaveButton = ctk.CTkButton(self, text="Save Application", command=self.SaveApplication)
            self.SaveButton.pack(pady=10)

        self.BackButton = ctk.CTkButton(self, text="Back to List", command=lambda: controller.show_page(ApplicationsPage))
        self.BackButton.pack(pady=10)

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
            self.cv_path = file_path
            self.CVLabel.configure(text=file_path)

    def SaveApplication(self):
        company_name = self.CompanyEntry.get()
        application_date = self.DateEntry.get()

        backend.SaveApplication(company_name, application_date, self.cv_path)
        self.controller.applications_data = backend.GetApplications()
        self.controller.show_page(ApplicationsPage)

    def SetStatus(self, status):
        backend.UpdateStatus(self.application[0], status)
        self.controller.applications_data = backend.GetApplications()
        self.StatusLabel.configure(text=f"Status: {status}")

class AppController(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.applications_data = backend.GetApplications()

        self.title("Proton's CV Application")
        self.geometry("600x600")
        self.resizable(True, True)

        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        self.current_page = None

        self.show_page(ApplicationsPage)

    def show_page(self, page_class, **kwargs):
        if self.current_page is not None:
            self.current_page.destroy()

        self.current_page = page_class(self.container, self, **kwargs)
        self.current_page.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = AppController()
    app.mainloop()
