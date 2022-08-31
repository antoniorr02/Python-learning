import tkinter

#Componente raíz
raiz = tkinter.Tk()
raiz.title("Mi programa")

#Componente frame
frame = tkinter.Frame(raiz)
frame.config(bg="grey", width=5000, height=300)
frame.pack()

#Componente etiqueta
texto = "Hola mundo"
etiqueta = tkinter.Label(raiz, text=texto)
etiqueta.config(fg="red", bg="blue", font="Cortana,30")
etiqueta.pack()

#Componente entry
entrada = tkinter.Entry(raiz)
entrada.config(justify="center", show="*")
entrada.pack()

#Componente text
entrada_larga = tkinter.Text()
entrada_larga.config(width=20, height=10, font="Verdana,15", padx=10, pady=10, fg="green", selectbackground="yellow")
entrada_larga.pack()

#Componente buttom
def accion():
    print("Hola mundo!")

boton = tkinter.Button(raiz, text="Ejecutar", command=accion)
boton.config(fg="orange")
boton.pack()

#Componente radiobuttom
def seleccionar():
    print(f"La opcion seleccionada es {opcion.get()}")

opcion = tkinter.IntVar()

boton1 = tkinter.Radiobutton(raiz, text="Opcion 1", variable=opcion, value=1, command=seleccionar)
boton1.pack()

boton2 = tkinter.Radiobutton(raiz, text="Opcion 2", variable=opcion, value=2, command=seleccionar)
boton2.pack()

boton3 = tkinter.Radiobutton(raiz, text="Opcion 3", variable=opcion, value=3, command=seleccionar)
boton3.pack()

#Componente checkbuttom
def verificar():
    valor = check1.get()
    if (valor == 1):
        print("El check está activado")
    else:
        print("El check está desactivado")

check1 = tkinter.IntVar()
primero = tkinter.Checkbutton(raiz, text="Opcion check", variable=check1, onvalue=1, offvalue=0, command=verificar)
primero.pack()

#Componente messagebox
from tkinter import messagebox
def avisar():
    tkinter.messagebox.showinfo("Titulo", "Mensaje con la informacion")
    print("Este es el aviso")

aviso = tkinter.Button(raiz, text="Pulsar para aviso", command=avisar)
aviso.pack()

#Componente messagebox (para preguntar)
def preguntar():
    resultado = tkinter.messagebox.askquestion("Titulo pregunta", "¿Borrar fichero?")
    if(resultado == "yes"):
        print("Si quiere")
    else:
        print("No quiere")

pregunta = tkinter.Button(raiz, text="Pulsar para preguntar", command=preguntar)
pregunta.pack()

#Componente filedialog para abrir un fichero
from tkinter import filedialog

def abrir_fichero():
    ruta = filedialog.askopenfilename(title="Abrir un fichero")
    print(ruta)

apertura_fichero = tkinter.Button(raiz, text="Pulsa para empezar", command=abrir_fichero)
apertura_fichero.pack()

raiz.mainloop()