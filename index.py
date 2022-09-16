#--Importar librerias necesarias
from msilib.schema import Icon
from tkinter import * 
from tkinter import ttk

#--Crear ventana de tamaño "500x300" permanente con su respectivo titulo y un fondo de color blanco
root = Tk() #Crear la ventana
root.geometry("550x300") #Ponerlo de tamño "550x300"
root.title("Conversor de temperatura") #Titulo
root.config(bg="#fff") #Ponerlo de fondo blanco
root.iconbitmap("Icono.ico") # Colocar un icono de un termómetro para que se vea mas estetico
root.resizable(False,False) #Hacer que no se pueda cambiar el tamño

#--Escribir encabezadode color azul claro y de tamaño arial 30 en negritas. Despues se proyecta en ventana
Cabeza=Label(root,text="Conversor de temperatura", font="arial 30 bold", bg = "#fff", fg="cyan")#Crear etiqueta con las especificaciones ya mencionadas
Cabeza.pack(pady=10) #Ponerlo arriba en la ventana, con una separacion de 10 px

#--Crear la primera entrada de texto donde insertaras los grados
celcius=StringVar() #Variable que almacena los grados 
EntradaCel=Entry(root,textvariable=celcius,width=8,font="arial 35", bg="#fff",fg="#000",bd=0).place(x=30,y=100)#Crear entrada de texto con todas las especificaciones necesarias
celcius.set("0") #Dejar como texto predeterminado "000"

#--Crear una etiqueta de texto, que sera el resultado
farenheit=StringVar() #Al igual que la entrada de texto anterior, se crea una variable
EntradaFar=Label(root,textvariable=farenheit,width=8,font="arial 35", bg="#fff",fg="#000",bd=0).place(x=300,y=100)#Crear etiqueta de texto con todas las especificaciones necesarias
farenheit.set("000") #Dejar como texto predeterminado "000"

#--Crear una etiqueta de texto para saber que estas convirtiendo
labeltext2 = StringVar() #Crear una variable de texto para poder modificarla despues
Etiqueta = Label(root,textvariable=labeltext2,font="arial 15", bg="#fff",fg="#000",bd=0).place(x=350,y=150)#Crear la etiqueta
labeltext2.set("Farenheit")#Ponerle como prederteminado "Farenheit"

#--Añadir un simbolo "=" para que se vea mas estetico
Label(root,text="=",font="arial 40", bg="#fff", fg="red").place(x=250,y=100)#Crear la etiqueta con el simbolo =

#--Crear funcion que convertira los grados celcius a farenheit
def ConvertirCaF():
    #Preceso matematico
    GradosCel=int(celcius.get()) #Obtener los grados que estan en la entrada de texto de celcius y meterlos en una variable
    Resultado = GradosCel*9/5+32 #Usar la formula "(x °C . 9/5) + 32 =" para sacar el resultado (En el codigo se simplifica esto)

    farenheit.set(str(Resultado)) #Actualizar la etiqueta de los farenheit al nuevo resultado
    root.update() #Actualizar toda la ventana tambien

#--Crear funcion que convierta los grados farenheit a celcius
def ConvertirFaC():
    #Preceso matematico
    GradosFar =int(celcius.get()) #Obtener los grados que estan en la entrada de texto de farenheit y meterlos en una variable
    Resultado = GradosFar- 32  #Usar la formula "(32 °F − 32) × 5/9 =" para sacar el resultado (En el codigo se simplifica esto)
    Resultado2 = Resultado * 5/9 #Se sigue la jerarquia de operaciones para lleguar al resultado correcto

    farenheit.set(str(round(Resultado2))) #Actualizar la etiqueta de los farenheit al nuevo resultado, redondeando los decimales
    root.update() #Actualizar toda la ventana tambien

#--Que hacer en caso de que se cambie de opcion
def CambioCombobox(event):
    r = Combo1.get() #Almacenar lo que se eligio en una variable
    if r == "Celcius": #En caso de que sea ceulcius poner la funcion del boton para que convierta celcius a farenheit
        Boton.config(command=ConvertirCaF)
        labeltext2.set("Farenheit") #Cambiar la otra etiqueta para saber que vas a convertir celcius a ferenheit
        
    else: #Si es farenheit poner la funcion del boton pra que convierta farenheit a celcius
        Boton.config(command=ConvertirFaC)
        labeltext2.set("Celcius") #Cambiar la otra etiqueta para saber que vas a convertir farenehit a celcius

#--Añadir un boton
Boton=Button(root,text="¡Convertir!",font="arial 20", bg="white", fg="black", command=ConvertirCaF) #Crear un boton con su texto, fuente, color de fondo y de texto
Boton.pack(padx=5,pady=40,side=BOTTOM)#Colocar el boton en la parte de abajo de la ventana, con su respectivo tamaño

#--Añadir dropbox para poder eligir que quieres converitr
Combo1 = ttk.Combobox(root,values=["Farenheit","Celcius"])#Poner una etiqueta para la entrada de celcius
Combo1.current(1) #Dejar como varlor por defecto a los Celcius, se coloca 1 porque la lista empieza del 0 y el 0 es Farenheit
Combo1.bind("<<ComboboxSelected>>", CambioCombobox) #Hacer que se detecte si el usuario cambia de opcion y poner la funcion antes creada
Combo1.place(x=30,y=150) #Colocar la dropbox en "X: 30 Y:150"

#--Dejar como predeterminado 0 celcius = 33.0 Farenheit
ConvertirCaF() #Para eso llamamos a la funcion de convertir celcius a farenheit sin necesidad de pulsar el boton.

#--Bucle de ventana
root.mainloop() #Esto hace que la ventana se mantenga abierta, debe de estar al final del codigo y si se borra nada de esto funcionara