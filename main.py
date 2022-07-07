# Importar Librerías
import tkinter as tk
import pymysql
from tkinter import *
from tkinter import messagebox

"""
Atributos para la tabla (solo se utiliza para crear la tabla)
cursor.execute("CREATE TABLE Alumnos (id int PRIMARY KEY AUTO_INCREMENT NOT NULL, nombre "
               "VARCHAR(50), apellido_p VARCHAR(50), apellido_m VARCHAR(50), cuil VARCHAR(50),"
               "email VARCHAR(50) NOT NULL)")
"""

def insertar_datos():  # Crear función para agregar datos
    bd = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="bd4"
    )

    # Crear variable cursor
    cursor = bd.cursor()

    sql = "INSERT INTO Alumnos(id, nombre, apellido_p, apellido_m, cuil, email)\
          VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')".format(id1.get(), nom.get(), apep.get(), apem.get(), cuil.get(), email.get())

    try:
        cursor.execute(sql)
        bd.commit()
        id1.delete(0, 'end')
        nom.delete(0, 'end')
        apep.delete(0, 'end')
        apem.delete(0, 'end')
        cuil.delete(0, 'end')
        email.delete(0, 'end')
        show()
        messagebox.showinfo(message="Registro Exitoso", title="Aviso")
    except:
        bd.rollback()
        messagebox.showinfo(message="No registrado", title="Aviso")

        bd.close()

def actualizar():  # Función para actualizar datos
    bd = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="bd4"
    )

    # Crear variable cursor
    cursor = bd.cursor()

    sql = "UPDATE Alumnos SET apellido_p='"+apep.get()+"', apellido_m='"+apem.get()+"', cuil='"+cuil.get()+"', " \
                                                "email='"+email.get()+"', nombre='"+nom.get()+"' WHERE id='"+id1.get()+"'"

    try:
        cursor.execute(sql)
        bd.commit()
        id1.delete(0, 'end')
        nom.delete(0, 'end')
        apep.delete(0, 'end')
        apem.delete(0, 'end')
        cuil.delete(0, 'end')
        email.delete(0, 'end')
        show()
        messagebox.showinfo(message="Actualización Exitosa", title="Aviso")
    except:
        bd.rollback()
        messagebox.showinfo(message="No se actualizo", title="Aviso")

        bd.close()


def consulta():  # Función para consultar un dato
    if(id1.get() == ""):
        messagebox.showinfo("Obteniendo consulta")
    else:
        bd = pymysql.connect(host="localhost", user="root", password="", db="bd4")
        cursor = bd.cursor()
        cursor.execute("SELECT * FROM Alumnos WHERE id='"+id1.get()+"'")
        id1.delete(0, 'end')
        nom.delete(0, 'end')
        apep.delete(0, 'end')
        apem.delete(0, 'end')
        cuil.delete(0, 'end')
        email.delete(0, 'end')
        show()
        rows = cursor.fetchall()

        for row in rows:
            nom.insert(0, row[1])
            apep.insert(0, row[2])
            apem.insert(0, row[3])
            cuil.insert(0, row[4])
            email.insert(0, row[5])

        bd.close()


def eliminar():  # Función para eliminar un dato
    bd = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="bd4"
    )
    cursor = bd.cursor()

    sql = "DELETE FROM Alumnos WHERE id='"+id1.get()+"'"

    try:
        cursor.execute(sql)
        bd.commit()
        id1.delete(0, 'end')
        nom.delete(0, 'end')
        apep.delete(0, 'end')
        apem.delete(0, 'end')
        cuil.delete(0, 'end')
        email.delete(0, 'end')
        show()
        messagebox.showinfo(message="Eliminado Exitoso", title="Aviso")
    except:
        bd.rollback()
        messagebox.showinfo(message="No eliminado", title="Aviso")

        bd.close()

def show():
    bd = pymysql.connect(host="localhost", user="root", password="", db="bd4")
    cursor = bd.cursor()
    cursor.execute("SELECT * FROM Alumnos")
    rows = cursor.fetchall()
    list.delete(0, list.size())

    for row in rows:
        insertardatos = str(row[0])+''+row[1]
        list.insert(list.size()+1, insertardatos)

    bd.close()



def cerrar() :  # Función para cerrar ventana
    vn.destroy()

# Creación de ventana
vn = tk.Tk()
vn.title("Formulario de Registro")  # (.title) se utiliza para darle un titulo
vn.geometry("500x700")  # (.geometry) se utiliza para asignarle un tamaño a la ventana
vn.configure(background="light grey")  # (.configure) se utiliza para hacer varias configuraciones

# Insertar y dimensionar imagen
image = tk.PhotoImage(file="Hyundai.png")  # (tk.PhotoImage) se utiliza para insertar una imagen
image = image.subsample(9, 9)  # (.subsample) se utiliza para dimensionar la imagen
image_label = tk.Label(image=image)  # (label) se utiliza para crear una etiqueta
image_label.pack()  # (.pack) se utiliza para visualizarlo

# Insertar etiquetas y cuadros de texto

# Etiqueta de "ID"
e = tk.Label(vn, text="ID", bg="gray", fg="white")
# (text=) Texto de la etiqueta (bg=) Color del sombreado (fg=) Color de la fuente
e.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
# (padx, pady, ipadx e ipady) Establecen el tamaño en pixeles
# (fill) = Llenar y (tk.X) Indica que rellena en forma horizontal

# Cuadro de texto de "ID"
id1 = tk.Entry(vn)
id1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)


# Etiqueta y cuadro de texto de "Nombre"
e0 = tk.Label(vn, text="NOMBRE", bg="gray", fg="white")
e0.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
nom = tk.Entry(vn)
nom.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

# Etiqueta y cuadro de texto de "Apellido Paterno"
e1 = tk.Label(vn, text="APELLIDO PATERNO", bg="gray", fg="white")
e1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
apep = tk.Entry(vn)
apep.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

# Etiqueta y cuadro de texto de "Apellido Materno"
e2 = tk.Label(vn, text="APELLIDO MATERNO", bg="gray", fg="white")
e2.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
apem = tk.Entry(vn)
apem.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

# Etiqueta y cuadro de texto de "CUIL"
e3 = tk.Label(vn, text="CUIL", bg="gray", fg="white")
e3.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
cuil = tk.Entry(vn)
cuil.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

# Etiqueta y cuadro de texto de "EMAIL"
e4 = tk.Label(vn, text="EMAIL", bg="gray", fg="white")
e4.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
email = tk.Entry(vn)
email.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

# Botones

# Registrar
boton = tk.Button(vn, text="Registrar", fg="black", command=insertar_datos)
boton.pack(side=tk.LEFT)

# Consultar
boton1 = tk.Button(vn, text="Consultar", fg="black", command=consulta)
boton1.pack(side=tk.LEFT)

# Actualizar
boton2 = tk.Button(vn, text="Actualizar", fg="black", command=actualizar)
boton2.pack(side=tk.LEFT)

# Eliminar
boton3 = tk.Button(vn, text="Eliminar", fg="black", command=eliminar)
boton3.pack(side=tk.LEFT)

# Ver Datos
boton4 = tk.Button(vn, text="Ver Datos", fg="black", command=show)
boton4.pack(side=tk.LEFT)

# Salir
boton5 = tk.Button(vn, text="Salir", fg="black", command=cerrar)
boton5.pack(side=tk.LEFT)

list = Listbox(vn)
list.place(x=400, y=70)

vn.mainloop()
# muestra en pantalla y responde a la entrada del usuario.
