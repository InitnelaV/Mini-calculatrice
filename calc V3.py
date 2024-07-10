import tkinter as tk
from tkinter import messagebox


def calculate():
    try:
        left_number = float(entry_left.get())
        right_number = float(entry_right.get())
        operation = entry_operation.get()

        if operation not in ["+", "-", "*", "/"]:
            messagebox.showerror("Erreur", "Le symbole d'opération doit être '+', '-', '*' ou '/'.")
            return

        result = 0
        if operation == "+":
            result = left_number + right_number
        elif operation == "-":
            result = left_number - right_number
        elif operation == "*":
            result = left_number * right_number
        elif operation == "/":
            if right_number == 0:
                messagebox.showerror("Erreur", "Impossible de diviser par 0.")
                return
            result = left_number / right_number

        label_result.config(text=f"Résultat: {left_number} {operation} {right_number} = {result}")
    except ValueError:
        messagebox.showerror("Erreur", "Les entrées doivent être des nombres valides.")


# Calculatrice
root = tk.Tk()
root.title("Calculatrice")

# Champs de saisie
tk.Label(root, text="Nombre de gauche:").grid(row=0, column=0)
entry_left = tk.Entry(root)
entry_left.grid(row=0, column=1)

tk.Label(root, text="Nombre de droite:").grid(row=1, column=0)
entry_right = tk.Entry(root)
entry_right.grid(row=1, column=1)

tk.Label(root, text="Opération (+, -, *, /):").grid(row=2, column=0)
entry_operation = tk.Entry(root)
entry_operation.grid(row=2, column=1)

# Bouton pour calculer
button_calculate = tk.Button(root, text="Calculer", command=calculate)
button_calculate.grid(row=3, columnspan=2)

# Label pour afficher le résultat
label_result = tk.Label(root, text="Résultat: ")
label_result.grid(row=4, columnspan=2)

# Boucle principale
root.mainloop()
