from tkinter import *
from tkinter import ttk
from tkinter.ttk import Style
from tkinter import messagebox
from PIL import Image, ImageTk
from sentencias import *



def insertar():
	usuarios = Sentencias()
	usuarios.insertar(officeCode.get(),City.get(),Phone.get(),AddressLine1.get(),AddressLine2.get(),State.get(),Country.get(),PostalCode.get(),Territory.get())
	officeCode.set("")
	City.set("")
	Phone.set("")
	AddressLine1.set("")
	AddressLine2.set("")
	State.set("")
	Country.set("")
	PostalCode.set("")
	Territory.set("")
	messagebox.showinfo("Informacion", "La oficina se registro correctamente =3")
	listar()


def listar():
	r.config(state = NORMAL)
	r.delete("1.0",END)
	r.insert(INSERT,"officeCode\t\tCity\t\tPhone\t\t\tAddressLine1\t\t\tAddressLine2\t\tState\t\tCountry\t\tPostalCode\t\tTerritory\n")
	usuarios = Sentencias()
	lista = usuarios.listar()
	for a in lista:
		r.insert(INSERT,a[0]+"\t\t"+a[1]+"\t\t"+a[2]+"\t\t\t"+a[3]+"\t\t\t"+a[4]+"\t\t"+a[5]+"\t\t"+a[6]+"\t\t"+a[7]+"\t\t"+a[8]+"\n")
	r.place(x=20,y=60)
	r.config(state=DISABLED)


def buscar(Key):
	if(cajaB.get() == ""):
		listar()
	
	else:
		r.config(state = NORMAL)
		r.delete("1.0",END)
		r.insert(INSERT,"officeCode\t\tCity\t\tPhone\t\t\tAddressLine1\t\t\tAddressLine2\t\tState\t\tCountry\t\tPostalCode\t\tTerritory\n")
		usuarios = Sentencias()
		lista = usuarios.buscar(cajaB.get())
		for a in lista:
			r.insert(INSERT,a[0]+"\t\t"+a[1]+"\t\t"+a[2]+"\t\t\t"+a[3]+"\t\t\t"+a[4]+"\t\t"+a[5]+"\t\t"+a[6]+"\t\t"+a[7]+"\t\t"+a[8]+"\n")
		r.place(x=20,y=60)
		r.config(state=DISABLED)


def modificar():
	usuarios = Sentencias()
	usuarios.modificar(officeCode.get(),City.get(),Phone.get(),AddressLine1.get(),AddressLine2.get(),State.get(),Country.get(),PostalCode.get(),Territory.get())
	officeCode.set("")
	City.set("")
	Phone.set("")
	AddressLine1.set("")
	AddressLine2.set("")
	State.set("")
	Country.set("")
	PostalCode.set("")
	Territory.set("")
	messagebox.showinfo("Informacion", "La oficina se modifico correctamente =3")
	listar()


def eliminar():
	usuarios = Sentencias()
	usuarios.eliminar(officeCode.get())
	messagebox.showinfo("Informacion", "La oficina se elimino correctamente =3")
	listar()


def PesInsertar():
	pes0 = ttk.Frame(notebook,style = 'My.TFrame')
	notebook.add(pes0,text = "Insertar")
	Label(pes0,text = "officeCode",fg = colorletra,bg = colorfondo).place(x= 35,y=50)
	Label(pes0,text = "City",fg = colorletra,bg = colorfondo).place(x= 35,y=100)
	Label(pes0,text = "Phone",fg = colorletra,bg = colorfondo).place(x= 35,y=150)
	Label(pes0,text = "AddressLine1",fg = colorletra,bg = colorfondo).place(x= 35,y=200)
	Label(pes0,text = "AddressLine2",fg = colorletra,bg = colorfondo).place(x= 35,y=250)
	Label(pes0,text = "State",fg = colorletra,bg = colorfondo).place(x= 35,y=300)
	Label(pes0,text = "Country",fg = colorletra,bg = colorfondo).place(x= 35,y=350)
	Label(pes0,text = "PostalCode",fg = colorletra,bg = colorfondo).place(x= 35,y=400)
	Label(pes0,text = "Territory",fg = colorletra,bg = colorfondo).place(x= 35,y=450)
	
	
	Entry(pes0,textvariable = officeCode).place(x = 120,y = 50)
	Entry(pes0,textvariable = City).place(x = 120,y = 100)
	Entry(pes0,textvariable = Phone).place(x = 120,y = 150)
	Entry(pes0,textvariable = AddressLine1).place(x = 120,y = 200)
	Entry(pes0,textvariable = AddressLine2).place(x = 120,y = 250)
	Entry(pes0,textvariable = State).place(x = 120,y = 300)
	Entry(pes0,textvariable = Country).place(x = 120,y = 350)
	Entry(pes0,textvariable = PostalCode).place(x = 120,y = 400)
	Entry(pes0,textvariable = Territory).place(x = 120,y = 450)
	Button(pes0,text="Guardar",bg="white",fg="black",command=insertar).place(x=120,y=500)




def PesModificar():
	pes2 = ttk.Frame(notebook,style = 'My.TFrame')
	notebook.add(pes2,text = "Modificar")
	Label(pes2,text = "officeCode",fg = colorletra,bg = colorfondo).place(x= 35,y=50)
	Label(pes2,text = "City",fg = colorletra,bg = colorfondo).place(x= 35,y=100)
	Label(pes2,text = "Phone",fg = colorletra,bg = colorfondo).place(x= 35,y=150)
	Label(pes2,text = "AddressLine1",fg = colorletra,bg = colorfondo).place(x= 35,y=200)
	Label(pes2,text = "AddressLine2",fg = colorletra,bg = colorfondo).place(x= 35,y=250)
	Label(pes2,text = "State",fg = colorletra,bg = colorfondo).place(x= 35,y=300)
	Label(pes2,text = "Country",fg = colorletra,bg = colorfondo).place(x= 35,y=350)
	Label(pes2,text = "PostalCode",fg = colorletra,bg = colorfondo).place(x= 35,y=400)
	Label(pes2,text = "Territory",fg = colorletra,bg = colorfondo).place(x= 35,y=450)
	
	
	Entry(pes2,textvariable = officeCode).place(x = 120,y = 50)
	Entry(pes2,textvariable = City).place(x = 120,y = 100)
	Entry(pes2,textvariable = Phone).place(x = 120,y = 150)
	Entry(pes2,textvariable = AddressLine1).place(x = 120,y = 200)
	Entry(pes2,textvariable = AddressLine2).place(x = 120,y = 250)
	Entry(pes2,textvariable = State).place(x = 120,y = 300)
	Entry(pes2,textvariable = Country).place(x = 120,y = 350)
	Entry(pes2,textvariable = PostalCode).place(x = 120,y = 400)
	Entry(pes2,textvariable = Territory).place(x = 120,y = 450)
	Button(pes2,text="Modificar",bg="white",fg="black",command=modificar).place(x=120,y=500)


def PesEliminar():
	pes3 = ttk.Frame(notebook,style = 'My.TFrame')
	notebook.add(pes3,text = "Eliminar")
	Label(pes3,text = "officeCode",fg = colorletra,bg = colorfondo).place(x= 35,y=50)
	Entry(pes3,textvariable = officeCode).place(x = 120,y = 50)
	Button(pes3,text="Eliminar",bg="white",fg="black",command=eliminar).place(x=120,y=78)

	

ventana = Tk()
colorfondo = "#4d79ff"
colorletra = "white"
stilos = Style()
stilos.configure('My.TFrame',background=colorfondo,foreground=colorletra)

officeCode = StringVar()
City = StringVar()
Phone = StringVar()
AddressLine1 = StringVar()
AddressLine2 = StringVar()
State = StringVar()
Country = StringVar()
PostalCode = StringVar()
Territory = StringVar()
cajaB = StringVar()


notebook = ttk.Notebook(ventana)
notebook.pack(fill = 'both', expand = 'yes')
PesInsertar()

pes1 = ttk.Frame(notebook,style = 'My.TFrame')
notebook.add(pes1,text = "Listar")
r = Text(pes1,width =500,height=15)
listar()
Label(pes1,text="Buscar: ",fg = colorletra, bg= colorfondo).place(x=20,y=30)
entry = Entry(pes1,textvariable= cajaB)
entry.place(x=80,y=30)
entry.bind("<KeyRelease>",buscar)

pes2 = ttk.Frame(notebook,style = 'My.TFrame')
PesModificar()

pes3 = ttk.Frame(notebook,style = 'My.TFrame')
PesEliminar()





ventana.geometry("900x350")
ventana.mainloop()




