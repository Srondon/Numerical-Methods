from tkinter import *
from tkinter import messagebox
from math import *
from tkinter import font
import tkinter
from typing import List
import numpy as np 
import sympy as sy
from matplotlib import pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from scipy.optimize.zeros import bisect
from tabulate import tabulate
from tkinter import ttk

#---- Ventana Principal ----
root = Tk()
root.title("Métodos Númericos T.de.A")
root.resizable(False, False)
menuMetodos = Menu(root)
root.config(menu = menuMetodos)
#Ancho y largo ventana
alturaVentana = 500
anchoVentana = 400

lblBienvenido = Label(root, text="¡BIENVENIDO!", font=('Arial',30))
lblBienvenido.pack(padx=10, pady=10)
lblTexto= Label(root, text="Esta es una aplicación para calcular raices de ecuaciones.", font=('Arial',13))
lblTexto.pack(side="left")
btnSalir = Button(root, text="Salir", font=('Arial',15), command = root.quit)
btnSalir.pack(side="bottom", pady=15)

#---- Centrar la Ventana ----
anchoPantalla = root.winfo_screenwidth()
alturaPantalla = root.winfo_screenheight()
x = (anchoPantalla / 2) - (anchoVentana / 2)
y = (alturaPantalla / 2) - (alturaVentana / 2)
root.geometry(f'{alturaVentana}x{anchoVentana}+{int(x)}+{int(y)}')

#---- Funciones Menu barra ----
def IrIntegrantes():
    vtnIntegrantes = Toplevel()
    vtnIntegrantes.resizable(0, 0)
    vtnIntegrantes.title("Integrantes del Proyecto")
    vtnIntegrantes.geometry(f'{alturaVentana}x{anchoVentana}+{int(x)}+{int(y)}')

    info = Label(vtnIntegrantes, 
    text="Realizado por: \n Santiago Rondón Galvis",
    font=('Arial',16))

    infoU = Label(vtnIntegrantes, text="Técnológico de Antioquia I.U 2021", font=('Arial',14))
    infoU.pack(side="bottom")

    info.pack(pady=20)
    btn1 = Button(vtnIntegrantes, text="Volver", font=('Arial',15), command= vtnIntegrantes.destroy)
    btn1.pack()

#---- Ventana de Bisección
def IrBiseccion():
    vtnBiseccion = Toplevel()
    vtnBiseccion.resizable(0, 0)
    vtnBiseccion.title("Bisección")
    vtnBiseccion.geometry(f'{alturaVentana}x{anchoVentana}+{int(x)}+{int(y)}')    
   
    #---- Entradas de la Ventana ----
    #Entrada de la Función
    LblFuncion = Label(vtnBiseccion, text="Función:", font=(13))
    LblFuncion.place(x=10, y=10)
    funcion = DoubleVar()
    entryfuncion = Entry(vtnBiseccion, textvariable = funcion, bd=5)
    entryfuncion.place(x=170, y=10)
    
    #Entrada del Limite Inferior
    LblLimInferior = Label(vtnBiseccion, text="Limite Inferior:", font=(13))
    LblLimInferior.place(x=10, y=40)
    liminferior = DoubleVar()
    entryLimInferior = Entry(vtnBiseccion, textvariable = liminferior, bd=5)
    entryLimInferior.place(x=170, y=40)

    #Entrada del Limite Superior
    LblLimSuperior = Label(vtnBiseccion, text="Limite Superior:", font=(13))
    LblLimSuperior.place(x=10, y=70)    
    limSuperior = DoubleVar()
    entryLimSuperior = Entry(vtnBiseccion, textvariable = limSuperior, bd=5) 
    entryLimSuperior.place(x=170, y=70)

    #Entrada de la Tolerancia
    LblTolerancia = Label(vtnBiseccion, text="Tolerancia:", font=(13))
    LblTolerancia.place(x=10, y=100)
    tolerancia = DoubleVar()
    entryTolerancia = Entry(vtnBiseccion, textvariable = tolerancia, bd=5) 
    entryTolerancia.place(x=170, y=100)

    #Muestra resultado del calculo
    respt = DoubleVar()
    entryRespuesta = Entry(vtnBiseccion, textvariable = respt, bd=5)
    entryRespuesta.place(x=170, y=150)

    #---- Funciones de los Botones ----
    def Limpiar():
        entryfuncion.delete(0,"end")
        entryLimInferior.delete(0, "end")
        entryLimSuperior.delete(0, "end")  
        entryTolerancia.delete(0, "end")
        entryRespuesta.delete(0, "end")

    #Con esto evaluamos la ecuación del Entry de la Función 
    def f(x):
        import math
        ecu = entryfuncion.get()
        return eval(ecu)

    #--- Método de Bisección ---
    def FormulaBiseccion():    
                
        LimiteIn = float(entryLimInferior.get())
        LimiteSup = float(entryLimSuperior.get())
        error = float(entryTolerancia.get())        

        Limite1=float(LimiteIn)
        Limite2=float(LimiteSup)
        error=float(error)
        xm=(Limite1+Limite2)/2

        fa=f(Limite1)
        fb=f(Limite2)
        fxm=f(xm)
        error_ac=abs(fxm)
        n=1
        arreglo=([1, Limite1 ,Limite2 ,xm ,fa ,fb ,fxm , error_ac ]) 
        valores=([arreglo])     

        while (error_ac>error):
            if xm*fxm <0.0:
                Limite2=xm
            else: 
                Limite1=xm
            xmm=xm
            xm=(Limite1+Limite2)/2
            fa=f(Limite1)
            fb=f(Limite2)
            fxm=f(xm)
            error_ac = abs(xm-xmm)
            n+=1
            valores.append([n, Limite1, Limite2, xm, fa, fb, fxm, error_ac])

        print(tabulate(valores,['iteraciones','a','b','xm','f(a)','f(b)','f(xm)','Error']))
        print(error_ac)
        print(error)
        entryRespuesta.insert(0, error_ac)

    def GraficaBiseccion():
        x = np.linspace(-5,5,1000)
        fig = plt.figure()        
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_position('center')
        ax.spines['top'].set_position('zero')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        #Trazar la funcion
        plt.plot(x,[f(i) for i in x])
        plt.show()
       
    #--- Botones ----
    btnCalcular = Button(vtnBiseccion, text="Calcular", command = FormulaBiseccion, font=('Arial',11))
    btnCalcular.place(x=10, y=150)

    btnGraph = Button(vtnBiseccion, text="Graficar", command = GraficaBiseccion, font=('Arial',11))
    btnGraph.place(x=10, y=200)

    btnLimpiar = Button(vtnBiseccion, text="Limpiar", command = Limpiar, font=('Arial',11))
    btnLimpiar.place(x=10, y=250)
    
    btnCerrar = Button(vtnBiseccion, text="Volver", command = vtnBiseccion.destroy, font=('Arial',11))
    btnCerrar.pack(side="bottom")



#---- Ventana de Regla Falsa
def IrReglaFalsa():
    vtnReglaFalsa = Toplevel()
    vtnReglaFalsa.resizable(0, 0)
    vtnReglaFalsa.title("Regla Falsa")
    vtnReglaFalsa.geometry(f'{alturaVentana}x{anchoVentana}+{int(x)}+{int(y)}')    
    
    #---- Entradas de la Ventana ----
    #Entrada de la Función
    LblFuncion = Label(vtnReglaFalsa, text="Función:", font=(13))
    LblFuncion.place(x=10, y=10)
    funcion = DoubleVar()
    entryfuncion = Entry(vtnReglaFalsa, textvariable = funcion, bd=5)
    entryfuncion.place(x=170, y=10)
    
    #Entrada del Limite Inferior
    LblLimInferior = Label(vtnReglaFalsa, text="Limite Inferior:", font=(13))
    LblLimInferior.place(x=10, y=40)
    liminferior = DoubleVar()
    entryLimInferior = Entry(vtnReglaFalsa, textvariable = liminferior, bd=5)
    entryLimInferior.place(x=170, y=40)

    #Entrada del Limite Superior
    LblLimSuperior = Label(vtnReglaFalsa, text="Limite Superior:", font=(13))
    LblLimSuperior.place(x=10, y=70)    
    limSuperior = DoubleVar()
    entryLimSuperior = Entry(vtnReglaFalsa, textvariable = limSuperior, bd=5) 
    entryLimSuperior.place(x=170, y=70)

    #Entrada de la Tolerancia
    LblTolerancia = Label(vtnReglaFalsa, text="Tolerancia:", font=(13))
    LblTolerancia.place(x=10, y=100)
    tolerancia = DoubleVar()
    entryTolerancia = Entry(vtnReglaFalsa, textvariable = tolerancia, bd=5) 
    entryTolerancia.place(x=170, y=100)

    #Muestra resultado del calculo
    respt = DoubleVar()
    entryRespuesta = Entry(vtnReglaFalsa, textvariable = respt, bd=5)
    entryRespuesta.place(x=170, y=150)

    #---- Funciones de los Botones ----
    def Limpiar():
        entryfuncion.delete(0,"end")
        entryLimInferior.delete(0, "end")
        entryLimSuperior.delete(0, "end")  
        entryTolerancia.delete(0, "end")
        entryRespuesta.delete(0, "end")

    #Con esto evaluamos la ecuación del Entry de la Función 
    def f(x):
        import math
        ecu = entryfuncion.get()
        return eval(ecu)


    #---- Método de Regla Falsa ----
    def FalseRule():  
        LimiteIn=float(entryLimInferior.get())
        LimiteSup=float(entryLimSuperior.get())
        error=float(entryTolerancia.get())
        entryRespuesta.get()
        res=0
        Limite1=float(LimiteIn)
        Limite2=float(LimiteSup)
        error=float(error)
        if Limite1>Limite2:
                raise ValueError("Intervalo mal definido")
        if f(Limite1) * f(Limite2) >= 0.0:
                raise ValueError("La funcion debe cambiar de signo en el intervalo")
        if error <= 0:
            raise ValueError("La cota de error debe ser un numero positivo")
        x=Limite1-(f(Limite1)*(Limite1-Limite2))/(f(Limite1)-f(Limite2))
        ar=np.array([1,Limite1, Limite2, x, f(Limite1), f(Limite2), f(x)])
        lista=([ar])
        idx=1
        while True:
            if(Limite2-Limite1) < error or Limite2-x < error or x-Limite1 < error:
                print(x)
                return lista
            elif np.sign(f(Limite1))*np.sign(f(Limite2))>0:
                Limite1=x
            else:
                Limite2=x
                x=Limite1-(f(Limite1)*(Limite1-Limite2))/(f(Limite1)-f(Limite2))
                idx+=1
                lista.append([idx, Limite1, Limite2,x,f(Limite1),f(Limite2),f(x)])
            return x

    #--- Para poder mostrar
    def CalcularReglaFalsa():        
        res=FalseRule()
        print(res)
        entryRespuesta.insert(0, res)

    #--- Gráfica del Método
    def GraficaReglaFalsa():
        x= np.linspace(-5,5,1000)
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_position('center')
        ax.spines['top'].set_position('zero')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.plot(x,[f(i) for i in x])
        plt.show()

    #--- Botones ----
    btnCalcular = Button(vtnReglaFalsa, text="Calcular", command = CalcularReglaFalsa, font=('Arial',11))
    btnCalcular.place(x=10, y=150)

    btnGraph = Button(vtnReglaFalsa, text="Graficar", command = GraficaReglaFalsa, font=('Arial',11))
    btnGraph.place(x=10, y=200)

    btnLimpiar = Button(vtnReglaFalsa, text="Limpiar", command = Limpiar, font=('Arial',11))
    btnLimpiar.place(x=10, y=250)
    
    btnCerrar = Button(vtnReglaFalsa, text="Volver", command=vtnReglaFalsa.destroy, font=('Arial',11))
    btnCerrar.pack(side="bottom")


#---- Ventana de Newton
def IrNewton():
    vtnNewton = Toplevel()
    vtnNewton.resizable(0, 0)
    vtnNewton.title("Newton")
    vtnNewton.geometry(f'{alturaVentana}x{anchoVentana}+{int(x)}+{int(y)}')    
    
    #---- Entradas de la Ventana ----
    #Entrada de la Función
    LblFuncion = Label(vtnNewton, text="Función:", font=(13))
    LblFuncion.place(x=10, y=10)
    funcion = DoubleVar()
    entryfuncion = Entry(vtnNewton, textvariable = funcion, bd=5)
    entryfuncion.place(x=170, y=10)
    
    #Entrada de la Derivada
    LblDerivada = Label(vtnNewton, text="Derivada:", font=(13))
    LblDerivada.place(x=10, y=40)
    derivada = DoubleVar()
    entryDerivada = Entry(vtnNewton, textvariable = derivada, bd=5)
    entryDerivada.place(x=170, y=40)

    #Entrada del valor de X
    LblValorX = Label(vtnNewton, text="Valor de X:", font=(13))
    LblValorX.place(x=10, y=70)    
    valorX = DoubleVar()
    entryValorX = Entry(vtnNewton, textvariable = valorX, bd=5) 
    entryValorX.place(x=170, y=70)

    #Entrada de la Tolerancia
    LblTolerancia = Label(vtnNewton, text="Tolerancia:", font=(13))
    LblTolerancia.place(x=10, y=100)
    tolerancia = DoubleVar()
    entryTolerancia = Entry(vtnNewton, textvariable = tolerancia, bd=5) 
    entryTolerancia.place(x=170, y=100)

    #Muestra resultado del calculo
    respt = DoubleVar()
    entryRespuesta = Entry(vtnNewton, textvariable = respt, bd=5)
    entryRespuesta.place(x=170, y=150)

    #---- Funciones de los Botones ----
    def Limpiar():
        entryfuncion.delete(0,"end")
        entryDerivada.delete(0, "end")
        entryValorX.delete(0, "end")  
        entryTolerancia.delete(0, "end")
        entryRespuesta.delete(0, "end")

    #Con esto evaluamos la ecuación del Entry de la Función 
    def Funcion(x):
        return np.e**(-x)-x

    def DerivadaFuncion(x):
       return -(np.e**(-x)) -1

    def Newton(x,f,df,tol):
        entryRespuesta.get()
        xn = x
        n=0
        ar = np.array([n, x, f(xn), df(xn)])
        lista = ([ar])

        while True:
            if(np.abs(f(xn)) < tol):
                print(xn)
                return xn  
            fxn=f(xn)
            Dfxn = df(xn)
            n+=1
            lista.append([n, xn, fxn, Dfxn])
            if Dfxn == 0:
                print('derivada de 0. sin solucion.')
                return None
            xn = xn - fxn/Dfxn
        return xn
   
    def CalcularNewton():
        resultado = Newton(0.1, Funcion, DerivadaFuncion, 1.0e-6)
        print(resultado)
        entryRespuesta.insert(0, resultado)

    #Gráfica de Newton
    def f(x):
        import math
        ecu = entryfuncion.get()
        return eval(ecu)

    def GraficarNewton():
        x= np.linspace(-1,1,1000)
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_position('center')
        ax.spines['top'].set_position('zero')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.plot(x,[f(i) for i in x])
        plt.show()

    #--- Botones ----
    btnCalcular = Button(vtnNewton, text="Calcular", command = CalcularNewton, font=('Arial',11))
    btnCalcular.place(x=10, y=150)

    btnGraph = Button(vtnNewton, text="Graficar", command= GraficarNewton, font=('Arial',11))
    btnGraph.place(x=10, y=200)

    btnLimpiar = Button(vtnNewton, text="Limpiar", command = Limpiar, font=('Arial',11))
    btnLimpiar.place(x=10, y=250)
    
    btnCerrar = Button(vtnNewton, text="Volver", command= vtnNewton.destroy, font=('Arial',11))
    btnCerrar.pack(side="bottom")


#---- Ventana de Secante
def IrSecante():
    vtnSecante = Toplevel()
    vtnSecante.resizable(0, 0)
    vtnSecante.title("Secante")
    vtnSecante.geometry(f'{alturaVentana}x{anchoVentana}+{int(x)}+{int(y)}')

    #---- Entradas de la Ventana ----
    #Entrada de la Función
    LblFuncion = Label(vtnSecante, text="Función:", font=(13))
    LblFuncion.place(x=10, y=10)
    funcion = DoubleVar()
    entryfuncion = Entry(vtnSecante, textvariable = funcion, bd=5)
    entryfuncion.place(x=170, y=10)
    
    #Entrada del Limite Inferior
    Lbl1erX = Label(vtnSecante, text="Primer valor X:", font=(13))
    Lbl1erX.place(x=10, y=40)
    primerValorX = DoubleVar()
    entryPrimerValorX = Entry(vtnSecante, textvariable = primerValorX, bd=5)
    entryPrimerValorX.place(x=170, y=40)

    #Entrada del Limite Superior
    Lbl2daX = Label(vtnSecante, text="Segundo valor X:", font=(13))
    Lbl2daX.place(x=10, y=70)    
    segundoValorX = DoubleVar()
    entrySegundoValorX = Entry(vtnSecante, textvariable = segundoValorX, bd=5)
    entrySegundoValorX.place(x=170, y=70)

    #Entrada de la Tolerancia
    LblTolerancia = Label(vtnSecante, text="Tolerancia:", font=(13))
    LblTolerancia.place(x=10, y=100)
    tolerancia = DoubleVar()
    entryTolerancia = Entry(vtnSecante, textvariable = tolerancia, bd=5) 
    entryTolerancia.place(x=170, y=100)

    #Muestra resultado del calculo
    respt = DoubleVar()
    entryRespuesta = Entry(vtnSecante, textvariable = respt, bd=5)
    entryRespuesta.place(x=170, y=150)

    #---- Funciones de los Botones ----
    def Limpiar():
        entryfuncion.delete(0,"end")
        entryPrimerValorX.delete(0, "end")
        entrySegundoValorX.delete(0, "end")  
        entryTolerancia.delete(0, "end")
        entryRespuesta.delete(0, "end")

    #Método de la Secante
    def fs(x):
        ecu = entryfuncion.get()
        return eval(ecu)

    def Secante(f, a, b, tol):
        an = a
        bn = b
        idx = 1
        entryRespuesta.get()
        ar = np.array([0, a, f(a)])
        lista = ([ar])    
        lista.append([1, b, f(b)])    
        while (True):
            if(f(b) - f(a) == 0):
                return c
            c = b - (f(b)*(b - a))/(f(b) - f(a))    
            idx += 1 
            lista.append([idx, c, f(c)])
            if(np.abs(f(c)) <= tol):
                return c                 
            a=b        
            b=c   
        return b - (f(b)*(b - a))/(f(b) - f(a))
    
    def CalcularSecante(): 
        a = float(entryPrimerValorX.get())
        b = float(entrySegundoValorX.get())
        c = float(entryTolerancia.get())
        
        res = Secante(fs, a, b, c)
        print(res)
        entryRespuesta.insert(0, res)
    
    def GraficarSecante():
        x= np.linspace(-1,1,1000)
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_position('center')
        ax.spines['top'].set_position('zero')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.plot(x,[fs(i) for i in x])
        plt.show()

    #--- Botones ----
    btnCalcular = Button(vtnSecante, text="Calcular", command = CalcularSecante, font=('Arial',11))
    btnCalcular.place(x=10, y=150)

    btnGraph = Button(vtnSecante, text="Graficar", command = GraficarSecante, font=('Arial',11))
    btnGraph.place(x=10, y=200)

    btnLimpiar = Button(vtnSecante, text="Limpiar", command = Limpiar, font=('Arial',11))
    btnLimpiar.place(x=10, y=250)
    
    btnCerrar = Button(vtnSecante, text="Volver", command= vtnSecante.destroy, font=('Arial',11))
    btnCerrar.pack(side="bottom")

#---- Ventana de Diferencia Numérica
def IrDiferenciaNumerica():
    vtnDifNumerica = Toplevel()
    vtnDifNumerica.resizable(0, 0)
    vtnDifNumerica.title("Diferenciación Numérica")
    x = (anchoPantalla / 2) - (anchoVentana / 2)
    y = (alturaPantalla / 2) - (alturaVentana / 2)
    vtnDifNumerica.geometry(f'{alturaVentana}x{anchoVentana}+{int(x)}+{int(y)}')

    #---- Entradas de la Ventana ----
    #Entrada de la Función
    LblFuncion = Label(vtnDifNumerica, text="Función:", font=(13))
    LblFuncion.place(x=10, y=10)
    funcion = DoubleVar()
    entryFuncion = Entry(vtnDifNumerica, textvariable = funcion, bd=5)
    entryFuncion.place(x=170, y=10)
    
    #Entrada del Punto Xo
    LblPuntoX0 = Label(vtnDifNumerica, text="Punto Xo:", font=(13))
    LblPuntoX0.place(x=10, y=40)
    PuntoXo = DoubleVar()
    entryPuntoXo = Entry(vtnDifNumerica, textvariable = PuntoXo, bd=5)
    entryPuntoXo.place(x=170, y=40)

    #Entrada del Valor de H
    LblValorH = Label(vtnDifNumerica, text="Valor de H:", font=(13))
    LblValorH.place(x=10, y=70)
    valorH = DoubleVar()
    entryValorH = Entry(vtnDifNumerica, textvariable = valorH, bd=5)
    entryValorH.place(x=170, y=70)

    #---- ListBox de resultado del calculo
    listaCaja = tkinter.Listbox(vtnDifNumerica)
    listaCaja.place(x=110, y=200, relwidth = 0.7)

    #---- DropDown Menu ----
    opcFormulas = [
    "Dos Puntos",
    "Tres Puntos",
    "Cinco Puntos Centrada",
    "Cinco Puntos Adelante y Atras"]

    escogerMetodo = StringVar()
    escogerMetodo.set(opcFormulas[0]) #Acá está por defecto el método de Dos Puntos
    menuAbajo = OptionMenu(vtnDifNumerica, escogerMetodo, *opcFormulas)
    menuAbajo.place(x=170, y=150)

    #---- Funciones de los Botones ----
    def Limpiar():
        entryFuncion.delete(0,"end")
        entryPuntoXo.delete(0, "end")
        entryValorH.delete(0, "end")  
        listaCaja.delete(0, "end")

    #Implementación del Método
    def CalcularDiferenciacion():
        ecu = entryFuncion.get()
        x = np.double(entryPuntoXo.get())
        h = np.double(entryValorH.get())

        def f(x):
            return eval(ecu)
        
        if escogerMetodo.get() == 'Dos Puntos':
            formaDosPuntos = ( f(x + h) - f(x) ) / h
            listaCaja.insert(0, "Formula Implementada : ( f(x + h) - f(x) ) / h")            
            listaCaja.insert(0, "Formula Dos Puntos : ", formaDosPuntos)
            listaCaja.insert(0, "\n  ")
        
        elif escogerMetodo.get() == 'Tres Puntos':
            formaTresPuntos = 1 / (2 * h) * (- f(x - h) + f(x + h))
            listaCaja.insert(0, "Formula Implementada : 1 / (2 * h) * (- f(x - h) + f(x + h))")        
            listaCaja.insert(0, "Formula Tres Puntos : ", formaTresPuntos)
            listaCaja.insert(0, "\n  ")
        
        elif escogerMetodo.get() == 'Cinco Puntos Centrada':
            formaCincoPuntosCentrada = (f(x - 2*h) - 8 * f(x - h) + 8 * f(x + h) - f(x + 2*h)) / (12 * h)
            listaCaja.insert(0, "Formula Implementada : (f(x - 2*h) - 8 * f(x - h) + 8 * f(x + h) - f(x + 2*h)) / (12 * h)")            
            listaCaja.insert(0, "Formula cinco puntos Centrada : ", formaCincoPuntosCentrada)
            listaCaja.insert(0, "\n  ")
        
        elif escogerMetodo.get() == 'Cinco Puntos Adelante y Atras':
            formaCincoPuntosAdlAtl = 1 / (12 * h) * (-25 * f(x) + 48 * f(x + h) - 36 * f(x + 2*h) + 16 * f(x + 3*h) - 3 * f(x + 4*h))
            listaCaja.insert(0, "Formula Implementada : 1 / (12 * h) * (-25 * f(x) + 48 * f(x + h) - 36 * f(x + 2*h) + 16 * f(x + 3*h) - 3 * f(x + 4*h))")            
            listaCaja.insert(0, "Formula cinco puntos Adelante y Atrás : ", formaCincoPuntosAdlAtl)
            listaCaja.insert(0, "\n  ")
        
        return

    #--- Botones ----
    btnCalcular = Button(vtnDifNumerica, text="Calcular", command = CalcularDiferenciacion, font=('Arial',11))
    btnCalcular.place(x=10, y=150)

    btnLimpiar = Button(vtnDifNumerica, text="Limpiar", command = Limpiar, font=('Arial',11))
    btnLimpiar.place(x=10, y=200)
    
    btnCerrar = Button(vtnDifNumerica, text="Volver", command= vtnDifNumerica.destroy, font=('Arial',11))
    btnCerrar.pack(side="bottom")

    #---- Ventana de Integración Numérica
def IrIntegracionNumerica():
    vtnIntegraNumerica = Toplevel()
    vtnIntegraNumerica.resizable(0, 0)
    vtnIntegraNumerica.title("Integración Numérica")
    x = (anchoPantalla / 2) - (anchoVentana / 2)
    y = (alturaPantalla / 2) - (alturaVentana / 2)
    vtnIntegraNumerica.geometry(f'{alturaVentana}x{anchoVentana}+{int(x)}+{int(y)}')

    #---- Entradas de la Ventana ----
     #Entrada de la Función
    LblFuncion = Label(vtnIntegraNumerica, text="Función:", font=(13))
    LblFuncion.place(x=10, y=10)
    funcion = DoubleVar()
    entryFuncion = Entry(vtnIntegraNumerica, textvariable = funcion, bd=5)
    entryFuncion.place(x=170, y=10)
    
    #Entrada valor de Xo (Limite Inferior)
    Lbl1erX = Label(vtnIntegraNumerica, text="Xo:", font=(13))
    Lbl1erX.place(x=10, y=40)
    primerValorX = DoubleVar()
    entryValorXo = Entry(vtnIntegraNumerica, textvariable = primerValorX, bd=5)
    entryValorXo.place(x=170, y=40)

    #Entrada valor de Xn (Limite Superior)
    Lbl2daX = Label(vtnIntegraNumerica, text="Xn:", font=(13))
    Lbl2daX.place(x=10, y=70)    
    segundoValorX = DoubleVar()
    entryValorXn = Entry(vtnIntegraNumerica, textvariable = segundoValorX, bd=5)
    entryValorXn.place(x=170, y=70)

    #Entrada valor de H
    LblValorN = Label(vtnIntegraNumerica, text="N:", font=(13))
    LblValorN.place(x=10, y=100)
    n = DoubleVar()
    entryValorN = Entry(vtnIntegraNumerica, textvariable = n, bd=5) 
    entryValorN.place(x=170, y=100)
    #---- ListBox de resultado del calculo
    listaCaja = tkinter.Listbox(vtnIntegraNumerica)
    listaCaja.place(x=170, y=200, relwidth = 0.6)

    #---- DropDown Menu ----
    opcFormulas = [
    "Trapecio",
    "Simpson 1/3",
    "Simpson 3/8"]

    escogerMetodo = StringVar()
    escogerMetodo.set(opcFormulas[0]) #Acá está por defecto el método del Trapecio
    menuAbajo = OptionMenu(vtnIntegraNumerica, escogerMetodo, *opcFormulas)
    menuAbajo.place(x=170, y=150)

    #---- Funciones de los Botones ----
    def Limpiar():
        entryFuncion.delete(0,"end")
        entryValorXo.delete(0, "end")
        entryValorXn.delete(0, "end")
        entryValorN.delete(0, "end")  
        listaCaja.delete(0, "end")

    #Implementación del Método
    def CalcularIntegracion():
        
        #-- Método del Trapecio
        if escogerMetodo.get() == 'Trapecio':

            def f(x):
                return eval(ecu)

            def Trapecio(x0,xn,n):    
                h = (xn - x0) / n
                listaCaja.insert(0,"Valor obtenido de H: ", h)
                print("Valor de H obtenido: ", h)
    
                integration = f(x0) + f(xn)
    
                for i in range(1,n):
                    k = x0 + i*h
                    integration = integration + 2 * f(k)
    
                integration = integration * h/2
    
                return integration
    
            #-- Ingreso datos
            ecu = entryFuncion.get()
            Xo = float(entryValorXo.get())
            Xn = float(entryValorXn.get())
            n = int(entryValorN.get())

            resultado = Trapecio(Xo, Xn, n)
            print(" \n Integración por método del Trapecio: %0.6f" % (resultado)) 
            listaCaja.insert(0," \n Integración por método del Trapecio: %0.6f" % (resultado))
            listaCaja.insert(0, "\n  ")
        
         #-- Método de Simpson 1/3
        elif escogerMetodo.get() == 'Simpson 1/3':            
            
            def f(x):
                return eval(ecu)

            def Simpson13(x0, xn, n):
                h = (xn - x0) / n
                listaCaja.insert(0,"Valor obtenido de H: ", h)
                print("Valor obtenido de H: ", h)
                listaCaja.insert(0, "\n  ")
                integration = f(x0) + f(xn)    
                for i in range(1,n):
                    k = x0 + i*h
                    if i%2 == 0:
                        integration = integration + 2 * f(k)
                    else:
                        integration = integration + 4 * f(k)
        
                integration = integration * h/3    
                return integration

            #-- Ingreso datos
            ecu = entryFuncion.get()
            Xo = float(entryValorXo.get())
            Xn = float(entryValorXn.get())
            n = int(entryValorN.get())

            #-- Muestro resultado
            resul = Simpson13(Xo, Xn, n)
            listaCaja.insert(0,"\n Integración por Simpson 1/3 es: %0.6f" % (resul))
            print("\n Resultado de integración por Simpson 1/3 es: %0.6f" % (resul))
            listaCaja.insert(0, "\n  ")

        #-- Método de Simpson 3/8
        elif escogerMetodo.get() == 'Simpson 3/8':            
            def f(x):
                return eval(ecu)

            def Simpson38(x0,xn,n):
                h = (xn - x0) / n
                listaCaja.insert(0,"Valor obtenido de H: ", h)
                print("Valor de H obtenido: ", h)
                integration = f(x0) + f(xn)
    
                for i in range(1,n):
                    k = x0 + i*h
        
                    if i%2 == 0:
                        integration = integration + 2 * f(k)
                    else:
                        integration = integration + 3 * f(k)
        
                integration = integration * 3 * h / 8    
                return integration

            #-- Ingreso datos
            ecu = entryFuncion.get()
            Xo = float(entryValorXo.get())
            Xn = float(entryValorXn.get())
            n = int(entryValorN.get())

            #-- Muestro resultado
            resul = Simpson38(Xo, Xn, n)
            listaCaja.insert(0,"\n Integración por Simpson 3/8 es: %0.6f" % (resul))
            print("\n Resultado de integración por Simpson 3/8 es: %0.6f" % (resul))
            listaCaja.insert(0, "\n  ")
                
        return #-- retorno del método padre
        
 #--- Botones ----
    btnCalcular = Button(vtnIntegraNumerica, text="Calcular", command = CalcularIntegracion, font=('Arial',11))
    btnCalcular.place(x=10, y=150)

    btnLimpiar = Button(vtnIntegraNumerica, text="Limpiar", command = Limpiar, font=('Arial',11))
    btnLimpiar.place(x=10, y=200)
    
    btnCerrar = Button(vtnIntegraNumerica, text="Volver", command= vtnIntegraNumerica.destroy, font=('Arial',11))
    btnCerrar.pack(side="bottom")

#---- Menú de Barra: Métodos ----
menuPorIntervalos = Menu(menuMetodos, tearoff = 0)
menuPorIntervalos.add_command(label="Bisección", command = IrBiseccion)
menuPorIntervalos.add_command(label="Regla Falsa", command = IrReglaFalsa)

menuPorAbiertos = Menu(menuMetodos, tearoff = 0)
menuPorAbiertos.add_command(label="Newton", command = IrNewton)
menuPorAbiertos.add_command(label="Secante", command = IrSecante)

menuDiferencias = Menu(menuMetodos, tearoff = 0)
menuDiferencias.add_command(label="Diferenciación Numérica", command = IrDiferenciaNumerica)
menuDiferencias.add_command(label="Integración Numérica", command = IrIntegracionNumerica)

menuIntegrantes = Menu(menuMetodos, tearoff = 0)
menuIntegrantes.add_command(label="Integrantes", command = IrIntegrantes)

menuMetodos.add_cascade(label="Métodos por Intervalos", menu = menuPorIntervalos)
menuMetodos.add_cascade(label="Métodos Abiertos", menu = menuPorAbiertos)
menuMetodos.add_cascade(label="Derivación e Integración", menu = menuDiferencias)
menuMetodos.add_cascade(label="Información", menu = menuIntegrantes)

#--- Mostrador ----
root.mainloop()