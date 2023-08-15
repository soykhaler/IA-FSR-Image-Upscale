import customtkinter as ctk
from tkinter import filedialog
import os
import subprocess
from PIL import Image

iconFile = 'icon.ico' 

def select_file():
    filename = filedialog.askopenfilename()
    entry.delete(0, 'end')
    entry.insert(0, filename)

def run_commands():
    filename = entry.get()
    # Obtener el directorio donde se encuentra el archivo ejecutable
    executable_dir = os.path.dirname(sys.executable)
    #obtener directorio donde se encuentra el ejecutable

    script_dir = os.path.dirname(os.path.abspath(__file__))


    #fidelityfx_path = os.path.join(current_dir, 'FidelityFX_CLI.exe')
    
    # Construir la ruta al ejecutable FidelityFX_CLI
    fidelityfx_path = os.path.join(executable_dir, 'FidelityFX_CLI.exe')
    # Abrir la imagen y obtener sus dimensiones
    with Image.open(filename) as img:
        width, height = img.size
    # Calcular las dimensiones escaladas
    scaled_width = width * 4
    scaled_height = height * 4
    # Construir el comando para escalar la imagen
    scale_command = [fidelityfx_path, '-Mode', 'EASU', '-Scale', str(scaled_width), str(scaled_height), filename, filename + '_Scaled.png']
    # Ejecutar el comando para escalar la imagen
    subprocess.run(scale_command)
    # Construir el comando para afilar la imagen escalada
    sharpen_command = [fidelityfx_path, '-Mode', 'RCAS', '-Sharpness', '0.2', filename + '_Scaled.png', filename + '_Sharpened.png']
    # Ejecutar el comando para afilar la imagen escalada
    subprocess.run(sharpen_command)


app = ctk.CTk()
app.title("FSR Upscale GUI by SoyKhaler")
app.geometry("350x200")
app.resizable(False, False)


label = ctk.CTkLabel(app, text="Select a file to upscale:")
label.pack()

entry = ctk.CTkEntry(app)
entry.pack()

label = ctk.CTkLabel(app, text="")
label.pack()

button = ctk.CTkButton(app, text="Select File", command=select_file)
button.pack()

label = ctk.CTkLabel(app, text="")
label.pack()

button = ctk.CTkButton(app, text="Upscale", command=run_commands)
button.pack()

label = ctk.CTkLabel(app, text="")
label.pack()

app.mainloop()
