import tkinter as tk
from tkinter import messagebox

class VentanaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Reservas de Buses")
        
        # Configurar el tamaño de la ventana similar al de un smartphone
        ancho_smartphone = 360
        alto_smartphone = 640
        self.root.geometry(f"{ancho_smartphone}x{alto_smartphone}")
        self.root.configure(bg='lightblue')  # Color de fondo celeste

        # Crear widgets
        self.label_usuario = tk.Label(root, text="Usuario:")
        self.entry_usuario = tk.Entry(root)

        self.label_contrasena = tk.Label(root, text="Contraseña:")
        self.entry_contrasena = tk.Entry(root, show="*")

        self.boton_ingresar = tk.Button(root, text="Ingresar", command=self.iniciar_sesion)

        # Ubicar widgets en la ventana
        self.label_usuario.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
        self.entry_usuario.grid(row=0, column=1, padx=10, pady=10)
        self.label_contrasena.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
        self.entry_contrasena.grid(row=1, column=1, padx=10, pady=10)
        self.boton_ingresar.grid(row=2, column=0, columnspan=2, pady=10)

    def iniciar_sesion(self):
        # Lógica de inicio de sesión
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()

        # Verificación de credenciales
        if usuario == "71450443" and contrasena == "2024":
            messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso.")
            # Después del inicio de sesión, abrir la ventana de búsqueda y reserva de buses
            self.abrir_ventana_busqueda()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas.")

    def abrir_ventana_busqueda(self):
        # Crear una nueva ventana para buscar y reservar buses
        ventana_busqueda = tk.Toplevel(self.root)
        ventana_busqueda.title("Búsqueda y Reserva de Buses")

        # Boseto de la ventana de búsqueda y reserva (puedes completar según tus necesidades)
        label_busqueda = tk.Label(ventana_busqueda, text="Buscar Buses:")
        entry_busqueda = tk.Entry(ventana_busqueda)
        boton_buscar = tk.Button(ventana_busqueda, text="Buscar", command=self.realizar_busqueda)

        label_busqueda.grid(row=0, column=0, padx=10, pady=10)
        entry_busqueda.grid(row=0, column=1, padx=10, pady=10)
        boton_buscar.grid(row=0, column=2, padx=10, pady=10)

    def realizar_busqueda(self):
        # Lógica de búsqueda (puedes completar según tus necesidades)
        messagebox.showinfo("Búsqueda", "Mostrar resultados de búsqueda aquí.")

# Crear la aplicación
root = tk.Tk()
app = VentanaApp(root)

# Iniciar la aplicación
root.mainloop()
