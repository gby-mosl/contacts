import json
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox, simpledialog
import tkinter as tk

JSON_FILE = "../sandbox/entreprises.json"

def load_data():
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"entreprises": []}

def save_data(data):
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

class DashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📊 Tableau de bord - Gestion des entreprises")
        self.data = load_data()

        # 🧱 Layout principal
        self.main_frame = ttk.Frame(root, padding=10)
        self.main_frame.pack(fill="both", expand=True)

        self.left_frame = ttk.LabelFrame(self.main_frame, text="👥 Personnel", padding=10)
        self.left_frame.pack(side="left", fill="both", expand=True, padx=5)

        self.right_frame = ttk.LabelFrame(self.main_frame, text="🏢 Entreprises", padding=10)
        self.right_frame.pack(side="right", fill="both", expand=True, padx=5)

        # 🔸 Liste du personnel
        self.personnel_listbox = tk.Listbox(self.left_frame, height=15)
        self.personnel_listbox.pack(fill="both", expand=True)

        self.add_staff_btn = ttk.Button(self.left_frame, text="➕ Ajouter", bootstyle=SUCCESS, command=self.add_personnel)
        self.add_staff_btn.pack(fill="x", pady=2)
        self.mod_staff_btn = ttk.Button(self.left_frame, text="✏️ Modifier", bootstyle=WARNING, command=self.mod_personnel)
        self.mod_staff_btn.pack(fill="x", pady=2)
        self.del_staff_btn = ttk.Button(self.left_frame, text="🗑️ Supprimer", bootstyle=DANGER, command=self.del_personnel)
        self.del_staff_btn.pack(fill="x", pady=2)

        # 🔹 Liste des entreprises
        self.entreprise_listbox = tk.Listbox(self.right_frame, height=15)
        self.entreprise_listbox.pack(fill="both", expand=True)
        self.entreprise_listbox.bind("<<ListboxSelect>>", self.on_entreprise_select)

        self.add_ent_btn = ttk.Button(self.right_frame, text="➕ Ajouter", bootstyle=SUCCESS, command=self.add_entreprise)
        self.add_ent_btn.pack(fill="x", pady=2)
        self.mod_ent_btn = ttk.Button(self.right_frame, text="✏️ Modifier", bootstyle=WARNING, command=self.mod_entreprise)
        self.mod_ent_btn.pack(fill="x", pady=2)
        self.del_ent_btn = ttk.Button(self.right_frame, text="🗑️ Supprimer", bootstyle=DANGER, command=self.del_entreprise)
        self.del_ent_btn.pack(fill="x", pady=2)

        self.refresh_entreprise_list()

    def refresh_entreprise_list(self):
        self.entreprise_listbox.delete(0, "end")
        for ent in self.data["entreprises"]:
            self.entreprise_listbox.insert("end", ent["nom"])
        self.personnel_listbox.delete(0, "end")

    def on_entreprise_select(self, event=None):
        self.personnel_listbox.delete(0, "end")
        ent = self.get_selected_entreprise()
        if ent:
            for p in ent["personnel"]:
                self.personnel_listbox.insert("end", f"{p['prenom']} {p['nom']} - {p['email']}")

    def get_selected_entreprise(self):
        selection = self.entreprise_listbox.curselection()
        if selection:
            index = selection[0]
            return self.data["entreprises"][index]
        return None

    def add_entreprise(self):
        nom = simpledialog.askstring("Nom", "Nom de l'entreprise :")
        rue = simpledialog.askstring("Rue", "Rue :")
        ville = simpledialog.askstring("Ville", "Ville :")
        cp = simpledialog.askstring("Code postal", "Code postal :")
        pays = simpledialog.askstring("Pays", "Pays :")

        if nom and ville and cp:
            new_ent = {
                "nom": nom,
                "adresse": {
                    "rue": rue or "",
                    "ville": ville,
                    "code_postal": cp,
                    "pays": pays or "France"
                },
                "personnel": []
            }
            self.data["entreprises"].append(new_ent)
            save_data(self.data)
            self.refresh_entreprise_list()

    def mod_entreprise(self):
        ent = self.get_selected_entreprise()
        if ent:
            ent["nom"] = simpledialog.askstring("Nom", "Modifier le nom :", initialvalue=ent["nom"]) or ent["nom"]
            ent["adresse"]["rue"] = simpledialog.askstring("Rue", "Modifier la rue :", initialvalue=ent["adresse"]["rue"])
            ent["adresse"]["ville"] = simpledialog.askstring("Ville", "Modifier la ville :", initialvalue=ent["adresse"]["ville"])
            ent["adresse"]["code_postal"] = simpledialog.askstring("Code postal", "Modifier le code postal :", initialvalue=ent["adresse"]["code_postal"])
            ent["adresse"]["pays"] = simpledialog.askstring("Pays", "Modifier le pays :", initialvalue=ent["adresse"]["pays"])
            save_data(self.data)
            self.refresh_entreprise_list()

    def del_entreprise(self):
        selection = self.entreprise_listbox.curselection()
        if selection:
            index = selection[0]
            del self.data["entreprises"][index]
            save_data(self.data)
            self.refresh_entreprise_list()

    def add_personnel(self):
        ent = self.get_selected_entreprise()
        if ent:
            prenom = simpledialog.askstring("Prénom", "Prénom du personnel :")
            nom = simpledialog.askstring("Nom", "Nom du personnel :")
            email = simpledialog.askstring("Email", "Email du personnel :")
            if prenom and nom and email:
                ent["personnel"].append({"prenom": prenom, "nom": nom, "email": email})
                save_data(self.data)
                self.on_entreprise_select()

    def mod_personnel(self):
        ent = self.get_selected_entreprise()
        selection = self.personnel_listbox.curselection()
        if ent and selection:
            index = selection[0]
            pers = ent["personnel"][index]
            pers["prenom"] = simpledialog.askstring("Prénom", "Modifier le prénom :", initialvalue=pers["prenom"])
            pers["nom"] = simpledialog.askstring("Nom", "Modifier le nom :", initialvalue=pers["nom"])
            pers["email"] = simpledialog.askstring("Email", "Modifier l'email :", initialvalue=pers["email"])
            save_data(self.data)
            self.on_entreprise_select()

    def del_personnel(self):
        ent = self.get_selected_entreprise()
        selection = self.personnel_listbox.curselection()
        if ent and selection:
            index = selection[0]
            del ent["personnel"][index]
            save_data(self.data)
            self.on_entreprise_select()

# 🚀 Lancement
if __name__ == "__main__":
    root = ttk.Window(themename="cosmo", size=(900, 500))
    app = DashboardApp(root)
    root.mainloop()