import json
import os
import ttkbootstrap as ttk

FICHIER_JSON = "contacts.json"


def load_data():
    try:
        if os.path.exists(FICHIER_JSON):
            with open(FICHIER_JSON, "r", encoding="utf-8") as f:
                return json.load(f)
    except FileNotFoundError:
        return {"entreprises": []}


def save_data(data):
    with open(FICHIER_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


class ContactsApp:
    def __init__(self, root):
        self.root = root
        self.data = load_data()
        self.selection_index = None

        self.setup_ui()

    def setup_ui(self):
        style = ttk.Style()
        style.theme_use("lumen")
        style.configure("Treeview", font=("Segoe UI", 11))
        style.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"))
        style.configure("Custom.Treeview", rowheight=28)

        # Fenêtre gauche : "Treeview" des entreprises et contacts
        self.left_frame = ttk.Frame(self.root, padding=10)
        self.left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(self.left_frame, columns="info", show="tree")
        self.tree.configure(style="Custom.Treeview")
        self.tree.tag_configure("entreprise", font=("Segoe UI", 11, "bold"), foreground="#158cba")  # bleu Bootstrap

        self.tree.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        # Fenêtre droite : Formulaires
        self.right_frame = ttk.Frame(self.root, padding=10)
        self.right_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        # Formulaire "Entreprise"
        self.company_form_frame = ttk.LabelFrame(self.right_frame, text="Entreprise", padding=10)
        self.company_form_frame.pack(fill="x", padx=10, pady=(0, 10))

        company_labels = ["     Nom", "Rue", "CP", "Ville", "Pays"]
        self.company_entries = []

        for i, label in enumerate(company_labels):
            ttk.Label(self.company_form_frame, text=label).grid(row=i, column=0, sticky="e", padx=5, pady=5)
            entry = ttk.Entry(self.company_form_frame, width=40)
            entry.grid(row=i, column=1, sticky="w", padx=5, pady=5)
            self.company_entries.append(entry)

        self.c_name_entry, self.c_street_entry, self.c_zip_entry, self.c_city_entry, self.c_country_entry = self.company_entries

        self.company_action_button = ttk.Button(self.company_form_frame, text="Ajouter",command=self.add_update_company)
        self.company_action_button.grid(row=len(company_labels), column=0, columnspan=2, pady=10)



        # Formulaire "Contact"
        self.employee_form_frame = ttk.LabelFrame(self.right_frame, text="Contact", padding=10)
        self.employee_form_frame.pack(fill="x", padx=10, pady=(0, 10))

        employee_labels = ["Nom", "Prénom", "Email"]
        self.employees_entries = []

        for i, label in enumerate(employee_labels):
            ttk.Label(self.employee_form_frame, text=label).grid(row=i, column=0, sticky="e", padx=5, pady=5)
            entry = ttk.Entry(self.employee_form_frame, width=40)
            entry.grid(row=i, column=1, sticky="w", padx=5, pady=5)
            self.employees_entries.append(entry)

        self.e_lastname_entry, self.e_firstname_entry, self.c_email_entry  = self.employees_entries

        self.employee_action_button = ttk.Button(self.employee_form_frame, text="Ajouter", command=self.add_update_employee())
        self.employee_action_button.grid(row=len(company_labels), column=0, columnspan=2, pady=10)

        self.refresh_list()

    def refresh_list(self):
        self.tree.delete(*self.tree.get_children())

        sorted_companies = sorted(self.data["entreprises"], key=lambda c: c["nom"].upper())

        for company in sorted_companies:
            item = self.tree.insert("", "end", text=company["nom"], tags=("entreprise",))
            sorted_employees = sorted(company["personnel"], key=lambda e: e["nom"].upper())
            for employee in sorted_employees:
                self.tree.insert(item, "end", text=(f'👤 {employee["nom"].upper()} {employee["prenom"]}'))

    def add_update_company(self):
        pass

    def add_update_employee(self):
        pass




if __name__ == "__main__":
    app = ttk.Window(title="Gestion des contacts", size=(1080, 600), resizable=(True, True))
    ContactsApp(app)
    app.mainloop()
