import json
import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox, simpledialog
import tkinter as tk

FICHIER_JSON = "entreprises.json"

def charger_entreprises():
    if os.path.exists(FICHIER_JSON):
        with open(FICHIER_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def sauvegarder_entreprises(entreprises):
    with open(FICHIER_JSON, "w", encoding="utf-8") as f:
        json.dump({"tech_be": entreprises}, f, indent=2, ensure_ascii=False)

class GestionEntrepriseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion des entreprises")
        self.entreprises = charger_entreprises()
        self.selection_index = None

        self.setup_ui()

    def setup_ui(self):
        style = ttk.Style()
        style.theme_use("lumen")
        style.configure("Treeview", font=("Segoe UI", 11))
        style.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"))
        style.configure("Custom.Treeview", rowheight=28)

        # Liste des entreprises
        self.left_frame = ttk.LabelFrame(self.root, text="Entreprises", padding=10)
        self.left_frame.pack(side="left", fill="both", expand=True, padx=5, pady=10)

        self.ent_tree = ttk.Treeview(self.left_frame, columns="Nom", show="headings", bootstyle="info")
        self.ent_tree.heading("Nom", text="Nom", anchor="w")
        self.ent_tree.column("Nom", anchor="w", width=40)
        self.ent_tree.configure(style="Custom.Treeview")

        self.ent_tree.pack(padx=10, pady=10, fill="both", expand=True)
        self.ent_tree.bind("<Double-1>", self.selectionner_entreprise)

        # Formulaire des entreprises
        # Champs de saisie
        ent_form_frame = ttk.Frame(self.left_frame)
        ent_form_frame.pack(pady=10, padx=10, fill="x")

        ent_labels_title = ["Entreprise", "Rue", "Code postal", "Ville", "Pays"]
        ent_labels_widths = [50, 50, 50, 50, 50]
        self.ent_entries = []

        for i, (label, width) in enumerate(zip(ent_labels_title, ent_labels_widths)):
            ttk.Label(ent_form_frame, text=label).grid(row=i, column=0, padx=5, sticky="e")
            entry = ttk.Entry(ent_form_frame, width=width)
            entry.grid(row=i, column=1, padx=5, pady=5,  sticky="we")
            self.ent_entries.append(entry)

        self.entreprise_entry, self.rue_entry, self.cp_entry, self.ville_entry, self.pays_entry = self.ent_entries

        # Boutons
        self.btn_ajouter_modifier = ttk.Button(ent_form_frame, text="Ajouter", width=50, command=self.ajouter_ou_modifier_entreprise,
                                               bootstyle="primary")
        self.btn_ajouter_modifier.grid(row=6, column=1, pady=5)


        # Liste des employés
        self.right_frame = ttk.LabelFrame(self.root, text="Personnel", padding=10)
        self.right_frame.pack(side="right", fill="both", expand=True, padx=5, pady=10)

        self.emp_tree = ttk.Treeview(self.right_frame, columns="Nom", show="headings", bootstyle="info")
        self.emp_tree.heading("Nom", text="Nom", anchor="w")
        self.emp_tree.column("Nom", anchor="w", width=40)
        self.emp_tree.configure(style="Custom.Treeview")
        self.emp_tree.pack(padx=10, pady=10, fill="both", expand=True)
        self.emp_tree.bind("<Double-1>", self.selectionner_personnel)

        # Formulaire des employés
        # Champs de saisie
        emp_form_frame = ttk.Frame(self.right_frame)
        emp_form_frame.pack(pady=10, padx=10, fill="x")

        emp_labels_title = ["Nom", "Prénom", "Email", "Téléphone"]
        emp_labels_widths = [50, 50, 50, 50]
        self.emp_entries = []

        for i, (label, width) in enumerate(zip(emp_labels_title, emp_labels_widths)):
            ttk.Label(emp_form_frame, text=label).grid(row=i, column=0, padx=5, sticky="e")
            entry = ttk.Entry(emp_form_frame, width=width)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="we")
            self.emp_entries.append(entry)

        self.nom_entry, self.prenom_entry, self.email_entry, self.telephone_entry = self.emp_entries

        # Boutons
        self.btn_ajouter_modifier_peronnel = ttk.Button(emp_form_frame, text="Ajouter", width=50,
                                               command=self.ajouter_ou_modifier_personnel,
                                               bootstyle="primary")
        self.btn_ajouter_modifier_peronnel.grid(row=4, column=1, pady=5)

        self.actualiser_tableau()

    def actualiser_tableau(self):
        self.ent_tree.delete(*self.ent_tree.get_children())

        # entrprises_tries = sorted(self.entreprises["entreprises"], key=lambda t: t["nom"].upper())

        for ent in self.entreprises["entreprises"]:
            nom_entreprise = ent["nom"].upper()

        self.ent_tree.insert("", "end", values=(nom_entreprise,))

    def ajouter_ou_modifier_entreprise(self):
        pass
    def selectionner_entreprise(self, event):
        pass

    def ajouter_ou_modifier_personnel(self):
        pass
    def selectionner_personnel(self, event):
        pass
#         # Formulaire
#         form_frame = ttk.Frame(self.root)
#         form_frame.pack(pady=10, padx=10, fill="x")
#
#         labels = ["Nom", "Prénom", "Email", "Téléphone"]
#         widths = [20, 20, 40, 20]
#         self.entries = []
#
#         for i, (label, width) in enumerate(zip(labels, widths)):
#             ttk.Label(form_frame, text=label).grid(row=0, column=i, padx=5, sticky="w")
#             entry = ttk.Entry(form_frame, width=width)
#             entry.grid(row=1, column=i, padx=5, sticky="we")
#             self.entries.append(entry)
#
#         self.nom_entry, self.prenom_entry, self.email_entry, self.telephone_entry = self.entries
#
#         self.actif_var = ttk.BooleanVar(value=True)
#         ttk.Checkbutton(form_frame, text="Actif", variable=self.actif_var, bootstyle="success").grid(row=1, column=4, padx=10)
#
#         self.btn_ajouter_modifier = ttk.Button(form_frame, text="Ajouter", command=self.ajouter_ou_modifier_technicien, bootstyle="primary")
#         self.btn_ajouter_modifier.grid(row=1, column=5, padx=10)
#
#         form_frame.columnconfigure((0, 1, 2, 3), weight=1)  # responsive columns
#
#         self.actualiser_tableau()
#
#     def actualiser_tableau(self):
#         self.tree.delete(*self.tree.get_children())
#
#         # Tri par nom (majuscules pour uniformiser)
#         techniciens_tries = sorted(self.techniciens, key=lambda t: t["nom"].upper())
#
#         for tech in techniciens_tries:
#             nom_maj = tech["nom"].upper()
#             actif_icon = "✓" if tech["actif"] else "✗"
#             self.tree.insert(
#                 "", "end",
#                 values=(
#                     nom_maj,
#                     tech["prenom"],
#                     tech["email"],
#                     tech.get("telephone", ""),
#                     actif_icon
#                 )
#             )
#
#     def ajouter_ou_modifier_technicien(self):
#         nom = self.nom_entry.get().strip()
#         prenom = self.prenom_entry.get().strip()
#         email = self.email_entry.get().strip()
#         telephone = self.telephone_entry.get().strip()
#         actif = self.actif_var.get()
#
#         if not nom or not prenom or not email:
#             ttk.Messagebox.show_warning("Champs manquants", "Veuillez remplir tous les champs obligatoires.")
#             return
#
#         tech_data = {
#             "nom": nom,
#             "prenom": prenom,
#             "email": email,
#             "telephone": telephone,
#             "actif": actif
#         }
#
#         if self.selection_index is not None:
#             self.techniciens[self.selection_index] = tech_data
#             self.selection_index = None
#             self.btn_ajouter_modifier.config(text="Ajouter")
#         else:
#             self.techniciens.append(tech_data)
#
#         self.vider_formulaire()
#         self.actualiser_tableau()
#         sauvegarder_techniciens(self.techniciens)
#
#     def selectionner_technicien(self, event):
#         item = self.tree.focus()
#         if not item:
#             return
#         values = self.tree.item(item)["values"]
#         for idx, tech in enumerate(self.techniciens):
#             if tech["nom"].upper() == values[0] and tech["prenom"] == values[1] and tech["email"] == values[2]:
#                 self.selection_index = idx
#                 self.nom_entry.delete(0, "end")
#                 self.nom_entry.insert(0, tech["nom"])
#                 self.prenom_entry.delete(0, "end")
#                 self.prenom_entry.insert(0, tech["prenom"])
#                 self.email_entry.delete(0, "end")
#                 self.email_entry.insert(0, tech["email"])
#                 self.telephone_entry.delete(0, "end")
#                 self.telephone_entry.insert(0, tech.get("telephone", ""))
#                 self.actif_var.set(tech["actif"])
#                 self.btn_ajouter_modifier.config(text="Modifier")
#                 break
#
#     def vider_formulaire(self):
#         for entry in self.entries:
#             entry.delete(0, "end")
#         self.actif_var.set(True)
#         self.selection_index = None
#         self.btn_ajouter_modifier.config(text="Ajouter")
#
if __name__ == "__main__":
    app = ttk.Window("Gestion des entreprises", size=(1080, 600), resizable=(True, True))
#     app.iconbitmap("omexom.ico")
    GestionEntrepriseApp(app)
    app.mainloop()