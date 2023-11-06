#LIBRERIAS DEL PROGRAMA
import tkinter as tk #LIBRERIA PARA INTERFAZ DE USARIO
from tkinter import ttk #MODULO PARA BOTONES,
from tkinter import font as tkFont #PARA DEFINIR Y MANIPULAR FUENTES DE TEXTO
from tkinter import messagebox as mb #MODULO PARA MENSAJES DE ERROR O ADVERTENCIAS E INFORMACION 
import re #MODULO PARA PATRONES DE BUSQUEDA
import hashlib #MODULO PARA ENCRIPTACION DE CONTRASEÑAS
import os #MODULO PARA ELIMINACION DE ARCHIVOS .TXT
from email.message import EmailMessage #MODULO PARA ORGANIZAR LOS DATOS PARA EL ENVIO DE CORREO
import ssl #MODULO DE SOPORTE EN PROTOCOLOS, PARA GARANTIZAR LA SEGURIDAD EN LA COMUNICACION ATREVEZ DEL INTERNET   
import smtplib #BIBLIOTECA PARA EL ENVIO DE CORREOS ATRAVEZ DEL PROTOCOLO SMTP
from tkinter.scrolledtext import ScrolledText #PROPORCIONA UN WIDGET COMBINADO CON UNA BARRA DE DESPLAZAMIENTO
import secrets #BIBLIOTECA PARA GENERACION DE CONTRASEÑAS SEGURAS   
import string #CONTIENE UNA COLECCION DE CARACTERES COMO, EL ABECEDARIO, DIGITOS, CARACTERES ESPECIALES, ETC.
from tkinter import Text #PARA PODER SELECCIONAR EL TEXTO
import random #UTILIZADA PARA LA GENERACION DE NOTAS ALEATORIAS
import reportlab                                        #
from reportlab.pdfgen import canvas                     #
from reportlab.pdfbase.ttfonts import TTFont            #BIBLIOTECA Y MODULOS PARA LA GENERACION DE CERTIFICADOS TIPO PDF
from reportlab.pdfbase import pdfmetrics                #
from reportlab.lib import colors                        #
import cv2 #LIBRERIA PARA DETECCION DE ROSTRO
import imutils #
import numpy as np #MODULO PARA TOMAR CADA CAPTURA GUARDADA
import shutil


# PROGRAMA TIPO APLICACION
class ACADEMIA:
    
    #VENTANA DE INICIO
    def __init__(self):

        #VENTANA DE INICIO

        self.ventana1=tk.Tk()

        #TITULO DE VENTANA
        
        self.ventana1.title("ACADEMIA USAC")
        
        #FUENTES PARA LOS TEXTOS
        
        fuente_personalizada = tkFont.Font(family="Arial", size=16, weight="bold")
        fuente_personalizada2 = tkFont.Font(family="Arial", size=10, weight="bold")
        
        #IMAGEN USAC
        
        self.canvas1=tk.Canvas(self.ventana1, width=200, height=200)
        self.canvas1.grid(column=1, row=0)
        archi1=tk.PhotoImage(file="ASDF.png")
        self.canvas1.create_image(25,0, image=archi1, anchor="nw")
        
        
        #TEXTO PARA QUE USUARIO DECIDA
        
        self.label1=tk.Label(self.ventana1, text=" INICIAR COMO:", font=fuente_personalizada)
        self.label1.grid(column=1, row=5, padx=5, pady=5)

        # BOTON DE REGISTRO COMO ESTUDIANTE 

        self.Boton1=tk.Button(self.ventana1, text="REGISTRO ESTUDIANTE", font=fuente_personalizada2, command=self.Ingreso)
        self.Boton1.grid(column=1, row=10, padx=5, pady=5)

        # BOTON DE INICIO COMO ESTUDIANTE 

        self.Boton2=tk.Button(self.ventana1, text="ESTUDIANTE", font=fuente_personalizada2, command=self.INICIOEST)
        self.Boton2.grid(column=1, row=15, padx=5, pady=5)

        # BOTON DE INICIO COMO CATEDRATICO

        self.Boton3=tk.Button(self.ventana1, text="CATEDRATICO", font=fuente_personalizada2, command=self.CatedraticoUSAC)
        self.Boton3.grid(column=1, row=20, padx=5, pady=5)
        
        # BOTON DE INICIO COMO ADMINISTRADOR
        
        self.Boton4=tk.Button(self.ventana1, text="ADMINISTRADOR", font=fuente_personalizada2, command=self.AdminUSAC)
        self.Boton4.grid(column=1, row=25, padx=5, pady=5)
        self.ventana1.mainloop()

#----------------------------------------------------------------------------------------------------------#--------------------------------------------------------------      
    #REGISTRO DEL ESTUDIANTE/NOMBRE
    def Ingreso(self):
        #VENTANA          
        reg_ventana=tk.Toplevel()
        reg_ventana.title("INGRESO COMO ESTUDIANTE:NOMBRE")
        #FUENTES PARA TEXTOS
        fuente_personalizada = tkFont.Font(family="Arial", size=10, weight="bold")
        fuente_personalizada2 = tkFont.Font(family="Arial", size=10, weight="bold")
        #INFORMACION QUE SE PIDE
        self.Name=tk.Label(reg_ventana, text="INGRESE SU/S NOMBRE/S", font=fuente_personalizada)
        self.Name.grid(column=0, row=4)
        #INFORMACION INGRESADA
        self.Nombre=tk.StringVar()
        Entry1=ttk.Entry(reg_ventana, width=50, textvariable=self.Nombre)
        Entry1.grid(column=0, row=10)
        #BOTON PARA GUARDAR INFORMACION
        self.Boton=tk.Button(reg_ventana, text="GUARDAR", font=fuente_personalizada2, command=lambda: self.COMPROBAR(reg_ventana))
        self.Boton.grid(column=0, row=20, padx=5, pady=5)

    #FUNCION QUE COMPROBARA SI HAY DATOS    
    def COMPROBAR(self, ventana):
        #ASIGNACION DE VARIABLE
        nombre = self.Nombre.get()
        #VERIFICA SI HAY DATOS EN LA CELDA
        if nombre=="":
            mb.showerror("ALERTA","HEY, NO HAS ESCRITO NADA")
        else:
            self.GUARDARNOMBRE()
            ventana.destroy()
            
    #FUNCION QUE GUARDARA EL NOMBRE Y CONTINUA AL APELLIDO
    def GUARDARNOMBRE(self):
        nombre = self.Nombre.get() + "\n"
        #VERIFICA EN CONSOLA SI LOS DATOS HAN SIDO GUARDADOS
        print("El nombre es: ",nombre)
        try:
            with open("REGISTROSTEMP.txt","w",encoding="utf-8") as archi1:
                archi1.write(nombre)
            print("Nombre guardado exitosamente en el archivo.")
        except Exception as e:
            print(f"Error al guardar el nombre en el archivo: {e}")
 
        self.APELLIDOS()
    
    #APELLIDOS
    def APELLIDOS(self):
        #VENTANA
        reg1_ventana=tk.Toplevel()
        reg1_ventana.title("INGRESO COMO ESTUDIANTE:APELLIDOS")
        #FUENTES PARA TEXTOS
        fuente_personalizada = tkFont.Font(family="Arial", size=10, weight="bold")
        fuente_personalizada2 = tkFont.Font(family="Arial", size=10, weight="bold")
        #INFORMACION QUE SE PIDE
        self.LName=tk.Label(reg1_ventana, text="INGRESE SU/S APELLIDO/S", font=fuente_personalizada)
        self.LName.grid(column=0, row=4)
        #INFORMACION INGRESADA
        self.LNombre=tk.StringVar()
        Entry2=ttk.Entry(reg1_ventana, width=50, textvariable=self.LNombre)
        Entry2.grid(column=0, row=10, padx=5, pady=5)
        #BOTON PARA GUARDAR INFORMACION
        self.Boton=tk.Button(reg1_ventana, text="GUARDAR", font=fuente_personalizada2, command=lambda: self.COMPROBAR2(reg1_ventana))
        self.Boton.grid(column=0, row=20, padx=5, pady=5)

    #FUNCION QUE COMPROBARA SI HAY DATOS    
    def COMPROBAR2(self, ventana):
        #ASIGNACION DE VARIABLE
        apellido = self.LNombre.get()
        #VERIFICA SI HAY DATOS EN LA CELDA
        if apellido=="":
            mb.showerror("ALERTA","HEY, NO HAS ESCRITO NADA")
        else:
            self.GUARDARAPELLIDO()
            ventana.destroy()

    #FUNCION QUE GUARDA EL APELLIDO Y CONTINUA AL DPI   
    def GUARDARAPELLIDO(self):
        #ASIGNACION DE VARIABLE
        apellido = self.LNombre.get() + "\n"
        #VERIFICA EN CONSOLA SI LOS DATOS HAN SIDO GUARDADOS
        print("El apellido es: ",apellido)
        try:
            with open("REGISTROSTEMP.txt","a",encoding="utf-8") as archi1:
                archi1.write(apellido)
            print("Apellido guardado exitosamente en el archivo.")
        except Exception as e:
            print(f"Error al guardar el apellido en el archivo: {e}")
 
        self.DPI()
    
    #REGISTRO DE DPI
    def DPI(self):
        #VENTANA
        reg2_ventana=tk.Toplevel()
        reg2_ventana.title("INGRESO COMO ESTUDIANTE:DPI")
        #FUENTES PARA TEXTOS
        fuente_personalizada = tkFont.Font(family="Arial", size=10, weight="bold")
        fuente_personalizada2 = tkFont.Font(family="Arial", size=10, weight="bold")
        #INFORMACION QUE SE PIDE
        self.DPI1=tk.Label(reg2_ventana, text="INGRESE SU DPI", font=fuente_personalizada)
        self.DPI1.grid(column=0, row=4)
        #INFORMACION INGRESADA
        self.DPIS=tk.StringVar()
        Entry3=ttk.Entry(reg2_ventana, width=50, textvariable=self.DPIS)
        Entry3.grid(column=0, row=10, padx=5, pady=5)
        #BOTON PARA GUARDAR INFORMACION
        self.Boton=tk.Button(reg2_ventana, text="GUARDAR", font=fuente_personalizada2, command=lambda: self.COMPROBAR3(reg2_ventana))
        self.Boton.grid(column=0, row=20, padx=5, pady=5)

    #FUNCION QUE COMPROBARA SI HAY DATOS    
    def COMPROBAR3(self, ventana):
        #ASIGNACION DE VARIABLE
        DPI = self.DPIS.get()
        #VERIFICA SI HAY DATOS EN LA CELDA Y SI LLEVA LETRAS
        if DPI == "":
            mb.showerror("ALERTA", "HEY, NO HAS ESCRITO NADA")
        elif not re.match(r'^\d+$', DPI):
            mb.showerror("ALERTA", "El NUM DE DPI NO LLEVA LETRAS")
        elif len(DPI) < 13 or len(DPI) > 13:
            mb.showerror("ALERTA", "EL DPI TIENE 13 DIGITOS")
        else:
            self.GUARDARDPI()
            ventana.destroy()

    #FUNCION QUE GUARDA EL DPI Y CONTINUA A LA FECHA DE NACIMIENTO   
    def GUARDARDPI(self):
        #ASIGNACION DE VARIABLE
        DPI = self.DPIS.get() + "\n"
        #VERIFICA EN CONSOLA SI LOS DATOS HAN SIDO GUARDADOS
        print("El DPI es: ",DPI)
        try:
            with open("REGISTROSTEMP.txt","a") as archi1:
                archi1.write(DPI)
            print("DPI guardado exitosamente en el archivo.")
        except Exception as e:
            print(f"Error al guardar el DPI en el archivo: {e}")
 
        self.FDN()

    #REGISTRO DE FECHA DE NACIMIENTO
    def FDN(self):
        #VENTANA
        reg3_ventana=tk.Toplevel()
        reg3_ventana.title("INGRESO COMO ESTUDIANTE:FECHA DE NACIMIENTO")
        #FUENTES PARA TEXTOS
        fuente_personalizada = tkFont.Font(family="Arial", size=10, weight="bold")
        fuente_personalizada2 = tkFont.Font(family="Arial", size=10, weight="bold")
        #INFORMACION QUE SE PIDE
        self.FDN1=tk.Label(reg3_ventana, text="INGRESE SU FECHA DE NACIMIENTO DIA/MES/AÑO", font=fuente_personalizada)
        self.FDN1.grid(column=0, row=4)
        #INFORMACION INGRESADA
        self.FDNS=tk.StringVar()
        Entry4=ttk.Entry(reg3_ventana, width=50, textvariable=self.FDNS)
        Entry4.grid(column=0, row=10, padx=5, pady=5)
        #BOTON PARA GUARDAR INFORMACION
        self.Boton=tk.Button(reg3_ventana, text="GUARDAR", font=fuente_personalizada2, command=lambda: self.COMPROBAR4(reg3_ventana))
        self.Boton.grid(column=0, row=20, padx=5, pady=5)

    #FUNCION QUE COMPROBARA SI HAY DATOS    
    def COMPROBAR4(self, ventana):
        #ASIGNACION DE VARIABLE
        FDN = self.FDNS.get()
        #VERIFICA SI HAY DATOS EN LA CELDA
        if FDN=="":
            mb.showerror("ALERTA","HEY, NO HAS ESCRITO NADA")
        elif not re.match(r'^\d{2}/\d{2}/\d{4}$', FDN):
            mb.showerror("ALERTA", "LA FECHA NO DEBE LLEVAR LETRAS")
            mb.showerror("ALERTA","INGRESARLA EN NUMEROS COMO DIA/MES/AÑO")
        else:
            self.GUARDARFDN()
            ventana.destroy()

    #FUNCION QUE GUARDA FECHA DE NACIMIENTO Y CONTINUA AL TELEFONO   
    def GUARDARFDN(self):
        #ASIGNACION DE VARIABLE
        FDN = self.FDNS.get() + "\n"
        #VERIFICA EN CONSOLA SI LOS DATOS HAN SIDO GUARDADOS
        print("La fecha de nacimiento es: ",FDN)
        try:
            with open("REGISTROSTEMP.txt","a") as archi1:
                archi1.write(FDN)
            print("Fecha de nacimiento guardada exitosamente en el archivo.")
        except Exception as e:
            print(f"Error al guardar la fecha de nacimiento en el archivo: {e}")
 
        self.TEL()

    #REGISTRO DE TELEFONO
    def TEL(self):
        #VENTANA
        reg4_ventana=tk.Toplevel()
        reg4_ventana.title("INGRESO COMO ESTUDIANTE:NUMERO DE TELEFONO")
        #FUENTES PARA TEXTOS
        fuente_personalizada = tkFont.Font(family="Arial", size=10, weight="bold")
        fuente_personalizada2 = tkFont.Font(family="Arial", size=10, weight="bold")
        #INFORMACION QUE SE PIDE
        self.TELS=tk.Label(reg4_ventana, text="INGRESE SU NUMERO DE TELEFONO", font=fuente_personalizada)
        self.TELS.grid(column=0, row=4)
        #INFORMACION INGRESADA
        self.PHONE=tk.StringVar()
        Entry5=ttk.Entry(reg4_ventana, width=50, textvariable=self.PHONE)
        Entry5.grid(column=0, row=10, padx=5, pady=5)
        #BOTON PARA GUARDAR INFORMACION
        self.Boton=tk.Button(reg4_ventana, text="GUARDAR", font=fuente_personalizada2, command=lambda: self.COMPROBAR5(reg4_ventana))
        self.Boton.grid(column=0, row=20, padx=5, pady=5)

    #FUNCION QUE COMPROBARA SI HAY DATOS    
    def COMPROBAR5(self, ventana):
        #ASIGNACION DE VARIABLE
        PHONE = self.PHONE.get()
        #VERIFICA SI HAY DATOS EN LA CELDA
        if PHONE == "":
            mb.showerror("ALERTA", "HEY, NO HAS ESCRITO NADA")
        elif not re.match(r'^\d+$', PHONE):
            mb.showerror("ALERTA", "EL NUMERO DE TELEFONO NO DEBE LLEVAR LETRAS")
        elif len(PHONE) < 8 or len(PHONE) > 8:
            mb.showerror("ALERTA", "El número de teléfono debe tener exactamente 8 dígitos")
        else:
            self.GUARDARPHONE()
            ventana.destroy()

    #FUNCION QUE GUARDA EL NUMERO DE TELEFONO Y CONTINUA AL USUARIO   
    def GUARDARPHONE(self):
        #ASIGNACION DE VARIABLE
        PHONE = self.PHONE.get() + "\n"
        #VERIFICA EN CONSOLA SI LOS DATOS HAN SIDO GUARDADOS
        print("El numero de telefono es: ",PHONE)
        try:
            with open("REGISTROSTEMP.txt","a") as archi1:
                archi1.write(PHONE)
            print("Numero de telefono guardado exitosamente en el archivo.")
        except Exception as e:
            print(f"Error al guardar el numero de telefono en el archivo: {e}")
 
        self.USER()
        
    #REGISTRO DE TELEFONO
    def USER(self):
        #VENTANA
        reg5_ventana=tk.Toplevel()
        reg5_ventana.title("INGRESO COMO ESTUDIANTE:USUARIO")
        #FUENTES PARA TEXTOS
        fuente_personalizada = tkFont.Font(family="Arial", size=10, weight="bold")
        fuente_personalizada2 = tkFont.Font(family="Arial", size=10, weight="bold")
        #INFORMACION QUE SE PIDE
        self.USERS=tk.Label(reg5_ventana, text="INGRESE SU NOMBRE COMO USUARIO\nSE RECOMIENDA SU PRIMER NOMBRE Y PRIMER APELLIDO", font=fuente_personalizada)
        self.USERS.grid(column=0, row=4)
        #INFORMACION INGRESADA
        self.USERR=tk.StringVar()
        Entry6=ttk.Entry(reg5_ventana, width=50, textvariable=self.USERR)
        Entry6.grid(column=0, row=10, padx=5, pady=5)
        #BOTON PARA GUARDAR INFORMACION
        self.Boton=tk.Button(reg5_ventana, text="GUARDAR", font=fuente_personalizada2, command=lambda: self.COMPROBAR6(reg5_ventana))
        self.Boton.grid(column=0, row=20, padx=5, pady=5)

    #FUNCION QUE COMPROBARA SI HAY DATOS    
    def COMPROBAR6(self, ventana):
        #ASIGNACION DE VARIABLE
        USER = self.USERR.get()
        #RUTA DEL LOS ARCHIVOS
        rutauser = "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/ESTUDIANTES/"
        #NOMBRE DEL ARCHIVO A BUSCAR                    
        archiuser = USER
        #RUTA COMPLETA QUE SE VA A BUSCAR
        ruta_completa = os.path.join(rutauser, archiuser + ".txt")
        #ABRIR ARCHIVO, SI ES QUE ESTE EXISTE
        try:
            # ABRIR ARCHIVO, SI ES QUE ESTE EXISTE
            with open(ruta_completa, "r", encoding="utf-8") as archi1:
                contenido = archi1.read()
                if USER == "":
                    mb.showinfo("ALERTA", "¡Hey, no has escrito nada!")
                elif contenido.strip() != "":
                    mb.showinfo("USUARIO EN USO", "¡Este nombre de usuario ya está en uso!")
                else:
                    self.GUARDARUSUARIO()
                    ventana.destroy()
        except FileNotFoundError:
            if USER: 
                # EL ARCHIVO NO EXISTE, ENTONCES CONTINUA EL PROCESO
                self.GUARDARUSUARIO()
                ventana.destroy()

    #FUNCION QUE GUARDA EL USUARIO Y CONTINUA AL EMAIL
    def GUARDARUSUARIO(self):
        #ASIGNACION DE VARIABLE
        USER = self.USERR.get() + "\n"
        #VERIFICA EN CONSOLA SI LOS DATOS HAN SIDO GUARDADOS
        print("El nombre de usuario es: ",USER)
        try:
            with open("REGISTROSTEMP.txt","a",encoding="utf-8") as archi1:
                archi1.write(USER)
            print("Nombre de usuario guardado exitosamente en el archivo.")
        except Exception as e:
            print(f"Error al guardar el nombre de usuario en el archivo: {e}")
 
        self.EMAIL()
    
    #REGISTRO DE EMAIL
    def EMAIL(self):
        #VENTANA
        reg6_ventana=tk.Toplevel()
        reg6_ventana.title("INGRESO COMO ESTUDIANTE:EMAIL")
        #FUENTES PARA TEXTOS
        fuente_personalizada = tkFont.Font(family="Arial", size=10, weight="bold")
        fuente_personalizada2 = tkFont.Font(family="Arial", size=10, weight="bold")
        #INFORMACION QUE SE PIDE
        self.EMAILS=tk.Label(reg6_ventana, text="INGRESE SU CORREO ELECTRONICO", font=fuente_personalizada)
        self.EMAILS.grid(column=0, row=4)
        #INFORMACION INGRESADA
        self.EMAILL=tk.StringVar()
        Entry7=ttk.Entry(reg6_ventana, width=50, textvariable=self.EMAILL)
        Entry7.grid(column=0, row=10, padx=5, pady=5)
        #BOTON PARA GUARDAR INFORMACION
        self.Boton=tk.Button(reg6_ventana, text="GUARDAR", font=fuente_personalizada2, command=lambda: self.COMPROBAR7(reg6_ventana))
        self.Boton.grid(column=0, row=20, padx=5, pady=5)

    #FUNCION QUE COMPROBARA SI HAY DATOS    
    def COMPROBAR7(self, ventana):
        #ASIGNACION DE VARIABLE
        EMAIL = self.EMAILL.get()
        #VERIFICA SI HAY DATOS EN LA CELDA
        if EMAIL == "":
            mb.showerror("ALERTA", "HEY, NO HAS ESCRITO NADA")
        elif not re.match(r'^[a-zA-Z0-9._%+-]+@gmail\.com$', EMAIL):
            mb.showerror("ALERTA", "EL CORREO ELECTRONICO DEBE INGRESARSE COMO 'USER'@gmail.com")
        else:
            self.GUARDAREMAIL()
            ventana.destroy()

    #FUNCION QUE GUARDA EL EMAIL Y CONTINUA A LA CONTRASEÑA
    def GUARDAREMAIL(self):
        #ASIGNACION DE VARIABLE
        USER = self.EMAILL.get() + "\n"
        #VERIFICA EN CONSOLA SI LOS DATOS HAN SIDO GUARDADOS
        print("El Email es: ",USER)
        try:
            with open("REGISTROSTEMP.txt","a") as archi1:
                archi1.write(USER)
            print("Email guardado exitosamente en el archivo.")
        except Exception as e:
            print(f"Error al guardar el Email en el archivo: {e}")
 
        self.CONTRA()

    #REGISTRO DE CONTRASEÑA
    def CONTRA(self):
        #VENTANA
        reg7_ventana=tk.Toplevel()
        reg7_ventana.title("INGRESO COMO ESTUDIANTE:CONTRASEÑA")
        #FUENTES PARA TEXTOS
        fuente_personalizada = tkFont.Font(family="Arial", size=10, weight="bold")
        fuente_personalizada2 = tkFont.Font(family="Arial", size=10, weight="bold")
        #INFORMACION QUE SE PIDE
        self.CON=tk.Label(reg7_ventana, text="INGRESE SU CONTRASEÑA \n LA CONTRASEÑA DEBE TENER LETRAS,NUMEROS Y CARACTERES, MINIMO 8 DIGITOS", font=fuente_personalizada)
        self.CON.grid(column=0, row=4)
        #INFORMACION INGRESADA
        self.CONT=tk.StringVar()
        Entry8=ttk.Entry(reg7_ventana, width=50, textvariable=self.CONT, show="*")
        Entry8.grid(column=0, row=10, padx=5, pady=5)
        #BOTON PARA GUARDAR INFORMACION
        self.Boton=tk.Button(reg7_ventana, text="GUARDAR", font=fuente_personalizada2, command=lambda: self.COMPROBAR8(reg7_ventana))
        self.Boton.grid(column=0, row=20, padx=5, pady=5)

    #FUNCION QUE COMPROBARA SI HAY DATOS    
    def COMPROBAR8(self, ventana):
        #ASIGNACION DE VARIABLE
        CONTRA = self.CONT.get()
        #VERIFICA SI HAY DATOS EN LA CELDA
        if CONTRA=="":
            mb.showerror("ALERTA","HEY, NO HAS ESCRITO NADA")
        elif self.validar_contrasena(CONTRA):
            self.CONTRA2()
            ventana.destroy()
        else:
            mb.showerror("ALERTA", "LA CONTRASEÑA DEBE TENER LETRAS,NUMEROS Y CARACTERES, MINIMO 8 DIGITOS ")

    #COMPROBAR
    def validar_contrasena(self, contrasena):
        # Utiliza una expresión regular para verificar la contraseña
        patron = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@#$%^&+=]).{8}$")
        return patron.match(contrasena) is not None
        
    #CONFIRMACION DE CONTRASEÑA
    def CONTRA2(self):
        #VENTANA
        reg8_ventana=tk.Toplevel()
        reg8_ventana.title("INGRESO COMO ESTUDIANTE:CONFIRMACION DE CONTRASEÑA")
        #FUENTES PARA TEXTOS
        fuente_personalizada = tkFont.Font(family="Arial", size=10, weight="bold")
        fuente_personalizada2 = tkFont.Font(family="Arial", size=10, weight="bold")
        #INFORMACION QUE SE PIDE
        self.CON2=tk.Label(reg8_ventana, text="VUELVA A INGRESAR SU CONTRASEÑA", font=fuente_personalizada)
        self.CON2.grid(column=0, row=4)
        #INFORMACION INGRESADA
        self.CONT2=tk.StringVar()
        Entry9=ttk.Entry(reg8_ventana, width=50, textvariable=self.CONT2, show="*")
        Entry9.grid(column=0, row=10, padx=5, pady=5)
        #BOTON PARA GUARDAR INFORMACION
        self.Boton=tk.Button(reg8_ventana, text="GUARDAR", font=fuente_personalizada2, command=lambda: self.COMPROBAR9(reg8_ventana))
        self.Boton.grid(column=0, row=20, padx=5, pady=5)

    #FUNCION QUE COMPROBARA SI HAY DATOS Y SI LAS CONTRASEÑAS SON IGUALES    
    def COMPROBAR9(self, ventana):
        #ASIGNACION DE VARIABLES
        CONTRA = self.CONT.get()
        CONTRA2 = self.CONT2.get()
        #VERIFICA SI HAY DATOS EN LA CELDA
        if CONTRA2=="":
            mb.showerror("ALERTA","HEY, NO HAS ESCRITO NADA")
        elif CONTRA2==CONTRA:
            self.GUARDARCONTRA(ventana)
        elif CONTRA2!=CONTRA:
            mb.showerror("ALERTA","HEY, LAS CONTRASEÑAS NO SON IGUALES")

    #FUNCION QUE CODIFICA Y GUARDA LA CONTRASEÑA
    def GUARDARCONTRA(self, ventana):
        #NOMBRE DEL ARCHIVO.txt
        USER = self.USERR.get()
        #RUTA DE LOS ARCHIVOS  .TXT
        ruta = "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/ESTUDIANTES/"
        #VARIABLE DEL ARCHIVO .TXT
        nuevo = os.path.join(ruta, USER + ".txt")
        #ASIGNACION DE VARIABLE
        CONTRA3 = self.CONT.get()   
        #CODIFICACION    
        Encrip = hashlib.sha256(CONTRA3.encode()).hexdigest()
        print("La encrip de la contraseña es: ", Encrip)
        #TRASLADO DE DATOS Al .txt DEL USUARIO, Y ESCRITURA DE LA CONTRASEÑA
        try:
            #CIERRE DE ARACHIVO POR SI AUN ESTA ABIERTO Y LUEGO LO ABRE PARA EVITAR ERRORES
            if os.path.exists("REGISTROSTEMP.txt"):
                with open("REGISTROSTEMP.txt", "r", encoding="utf-8") as archi2:
                    contenido = archi2.read()
                #BORRADO DE ARCHIVO TEMPORAL
                os.remove("REGISTROSTEMP.txt")
            #ESCRITURA DE DATOS Al .txt DEL USUARIO, Y LA CONTRASEÑA
            with open(nuevo, "w", encoding="utf-8") as archi1:
                archi1.write(Encrip + "\n")
                archi1.write(contenido)
                archi1.write("-----------------------------------------------------------------------------------------------------\n")
                #CIERRE DE VENTANA
                ventana.destroy()
                self.TOMADEIDENTIDAD()
                mb.showinfo("EXITO", "BIENVENIDO A ACADEMIA USAC")
            #VERIFICA EN CONSOLA SI LOS DATOS HAN SIDO GUARDADOS
            print("Datos guardados exitosamente en el archivo.")
        except Exception as e:
            print(f"Error al guardar la contraseña en el archivo: {e}")

    #FUNCION QUE TOMA FOTOGRAFIAS DEL ROSTRO DEL ESTUDIANTE
    def TOMADEIDENTIDAD(self):
        
        personName = self.USERR.get()
        #RUTA PARA ALMACENAR LAS FOTOS
        dataPath = 'C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/ROSTROS' 
        personPath = dataPath + '/' + personName

        if not os.path.exists(personPath):
            print('Carpeta creada: ',personPath)
            os.makedirs(personPath)

        cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        #cap = cv2.VideoCapture('Video.mp4')

        faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
        count = 0

        while True:

            ret, frame = cap.read()
            if ret == False: break
            frame =  imutils.resize(frame, width=640)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            auxFrame = frame.copy()

            faces = faceClassif.detectMultiScale(gray,1.3,5)

            for (x,y,w,h) in faces:
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                rostro = auxFrame[y:y+h,x:x+w]
                rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
                cv2.imwrite(personPath + '/face_{}.jpg'.format(count),rostro)
                count = count + 1
            cv2.imshow('frame',frame)

            k =  cv2.waitKey(1)
            if k == 27 or count >= 200:
                break

        cap.release()
        cv2.destroyAllWindows()
        self.ALMACENARIDENTIDAD()

    #FUNCION QUE ALMACENA LAS FOTOGRAFIAS EN UN .xml
    def ALMACENARIDENTIDAD(self):

        nombre = self.USERR.get()
        dataPath = 'C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/ROSTROS/' 
        peopleList = os.listdir(dataPath)
        print('Lista de personas: ', peopleList)

        labels = []
        facesData = []
        label = 0

        for nameDir in peopleList:
            personPath = os.path.join(dataPath, nameDir)  # Usa os.path.join para construir rutas de forma segura
            print('Leyendo las imágenes')

            if os.path.isdir(personPath):  # Verificar si es una carpeta
                for fileName in os.listdir(personPath):
                    print('Rostros: ', nameDir + '/' + fileName)
                    labels.append(label)
                    facesData.append(cv2.imread(os.path.join(personPath, fileName), 0))
            else:
                print(f'{personPath} no es una carpeta, se omitirá.')
            label = label + 1

        face_recognizer = cv2.face.LBPHFaceRecognizer.create()

        print("Entrenando...")
        face_recognizer.train(facesData, np.array(labels))

        ruta = 'C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/ROSTROS/'
        nombreEST = nombre + '.xml' 

        if not os.path.exists(ruta):
            os.makedirs(ruta)

        face_recognizer.write(os.path.join(ruta, nombreEST))
        print("Modelo almacenado...")

        carpeta_a_borrar = 'C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/ROSTROS/' + nombre

        try:
            shutil.rmtree(carpeta_a_borrar)
            print(f'Se ha borrado la carpeta y su contenido: {carpeta_a_borrar}')
            self.CORREOBIENVENIDA()
        except OSError as e:
            print(f'No se pudo borrar la carpeta: {carpeta_a_borrar}')
            print(e)

    #CORREO DE BIENVENIDA
    def CORREOBIENVENIDA(self):
        #DIRECCION DE CORREO ELECTRONICO
        CORREO = self.EMAILL.get()
        #INFORMACION PARA EL CORREO ELECTRONICO
        usuario = self.USERR.get()
        #CORREO ELECTRONICO DEL EMISOR
        email_emisor = 'usac66654@gmail.com'
        email_contra = 'yehr mcwg yqss ibsp'
        #CORREO ELECTRONICO DEL RECEPTOR 
        email_receptor2 = CORREO
        #LISTA DE DESTINATARIOS PARA EL CORREO
        destinatarios = [email_receptor2]
        #ASUNTO Y CUERPO DEL CORREO ELECTRONICO
        asunto = 'INFORMACION ACADEMIA USAC'
        cuerpo = """BIENVENIDO A LA ACADEMIA USAC  QUERID@ """ + ( usuario) 
        #ASIGNACIONES DE LA LOCALIDAD EN EL #CORREO ELECTRONICO PARA EL ENVIO
        em=EmailMessage()
        em['from'] = email_emisor
        em['To'] = ", ".join(destinatarios)
        em['Subject'] = asunto
        em.set_content(cuerpo)
        #SEGURIDAD PARA EL ENVIO DE CORREO
        contexto = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as ADVERTENCIA:
            ADVERTENCIA.login(email_emisor,email_contra)
            ADVERTENCIA.sendmail(email_emisor,destinatarios, em.as_string())
        #INFORMACION EN CONSOLA
        print("CORREO ENVIADO")
#----------------------------------------------------------------------------------------------------------#--------------------------------------------------------------      
    #INICIO DE SESION COMO ESTUDIANTE
    def INICIOEST(self):
        #VENTANA
        ventanaAD=tk.Toplevel()
        ventanaAD.title("INICIO DE SESION COMO ESTUDIANTE")
        #FUENTES PARA TEXTOS
        fuente_personalizada = tkFont.Font(family="Arial", size=12, weight="bold")
        fuente_personalizada2 = tkFont.Font(family="Arial", size=10, weight="bold")
        #INFORMACION QUE SE PIDE
        self.INU=tk.Label(ventanaAD, text="INGRESE SU USUARIO", font=fuente_personalizada)
        self.INU.grid(column=0, row=4)
        self.IN2=tk.Label(ventanaAD, text="INGRESE SU CONTRASEÑA", font=fuente_personalizada)
        self.IN2.grid(column=0, row=6)
        #INFORMACION INGRESADA
        self.INU=tk.StringVar()
        Entry=ttk.Entry(ventanaAD, width=50, textvariable=self.INU)
        Entry.grid(column=0, row=5, padx=5, pady=5)
        self.INCON=tk.StringVar()
        Entry1=ttk.Entry(ventanaAD, width=50, textvariable=self.INCON, show="*")
        Entry1.grid(column=0, row=7, padx=5, pady=5)
        #BOTON PARA GUARDAR INFORMACION
        self.Boton=tk.Button(ventanaAD, text="COMENZAR", font=fuente_personalizada2, command=lambda: self.COMPROBAR10(ventanaAD))
        self.Boton.grid(column=0, row=20, padx=5, pady=5)
        #BOTON PARA PEDIR CONTRASEÑA
        self.Boton2=tk.Button(ventanaAD, text="PEDIR CONTRASEÑA", font=fuente_personalizada2, command=lambda: self.PEDIRCONTRA(ventanaAD))
        self.Boton2.grid(column=0, row=21, padx=5, pady=5)
        # CONTADOR DE INTENTOS
        self.intentos = 3

    #COMPROBACION DE DATOS DEL ESTUDIANTE
    def COMPROBAR10(self, ventana):
        #VARIABLE PARA LA COMPROBACION SI EL ESTUDIANTE HA SIDO BLOQUEADO
        BLOCK = "BLOQUEADO"
        #RUTA DEL LOS ARCHIVOS
        rutauser = "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/ESTUDIANTES/"
        #ASIGNACIONES DE VARIABLES INGRESADAS
        usuario = self.INU.get()
        contrasena = self.INCON.get()
        #ENCRIPTACION DE CONTRASEÑA
        Encrip2 = hashlib.sha256(contrasena.encode()).hexdigest()
        #CONTRASEÑA MAESTRA
        Encripmaster = "57d264e19d9846091986a22b3f250ab4c39161fdabb388e42a957d0f460d0231"
        Encripmaster2 ="bc8db39f614342b78a67494dbece216d3726f6924b73563be34fc630ac1db7f5"
        #NOMBRE DEL ARCHIVO A BUSCAR                    
        archiuser = usuario
        #RUTA COMPLETA QUE SE VA A BUSCAR
        ruta_completa = os.path.join(rutauser, archiuser + ".txt")
        
        #ENCONTRAR CORREO Y DESIGNARLE UNA VARIABLE PARA ENVIO DE CORREO SI LA CUENTA ES BLOQUEADA
        try:
            with open(ruta_completa, "r", encoding="utf-8") as archicorreo:
                contenido = archicorreo.read()
                correogmail = re.findall(r'\S+@gmail\.com', contenido)
                CORREO = correogmail[0]
                print(CORREO)
     
            #INTENTO DE RECONOCER AL USUARIO
                if Encrip2 == Encripmaster:
                    with open(ruta_completa, "r", encoding="utf-8") as archi1:
                        lineas = archi1.readlines()
                    with open(ruta_completa, "w", encoding="utf-8") as archi:
                        for linea in lineas:
                            if BLOCK not in linea:
                                nueva_linea = linea.replace(BLOCK, '')
                                archi.write(nueva_linea)
                                print("CUENTA DESBLOQUEDA")
                elif Encrip2 == Encripmaster2:
                        mb.showinfo("INFO", "CUENTA DESBLOQUEDA")
                        self.VENTANAEST()
                        ventana.destroy() 
                else:

                    #COMPROBAR SI EL ESTUDIANTE EXISTE, ABRIR ARCHIVO EN MODO LECTURA
                    with open(ruta_completa, "r", encoding="utf-8") as archi1:
                        contenido = archi1.readlines()  

                        #ALERTA DE QUE LA CUENTA ESTA BLOQUEADA

                        if BLOCK in [line.strip() for line in contenido]:      
                            mb.showerror("ERROR","TU CUENTA ESTA BLOQUEADA")

                        else:  
                            #COMPROBACION DE NOMBRE DE USUARIO     
                            if usuario in [line.strip() for line in contenido]:
                                #COMPROBACION DE CONTRASEÑA INGRESADA
                                if Encrip2 in [line.strip() for line in contenido]:
                                    #CIERRA ARCHIVO Y ABRE LA VENTANA PRINCIPAL DEL ESTUDIANTE
                                    archi1.close()
                                    self.COMPROBARIDENTIDAD()
                                    ventana.destroy()
                                else:
                                    #ALERTA DE CONTRASEÑA INCORRECTA Y CONTEO DE INTENTOS
                                    mb.showerror("ALERTA","CONTRASEÑA INCORRECTA")
                                    self.intentos -= 1
                                    if self.intentos == 0:
                                        #ALERTA FINAL POR INTENTO DE ENTRAR A LA CUENTA
                                        mb.showerror("ALERTA", "TRES INTENTOS FALLIDOS, TE CAERA EL ADMIN >:v")
                                        #CIERRA ARCHIVO DEL ESTUDIANTE QUE ESTA EN MODO LECTURA
                                        archi1.close()
                                        #ABRE ARCHIVO DEL ESTUDIANTE EN MODO AÑADIR
                                        with open(ruta_completa, "a", encoding="utf-8") as archi2:
                                            #ESCRITURA PARA BLOQUEAR USUARIO Y AVISO DEL BLOQUEO AL MISMO
                                            archi2.write("BLOQUEADO")
                                            archi2.close()
                                            self.AVISOADMIN(ventana,CORREO)
                                    else:
                                        #AVISO DE INTENTOS QUE QUEDAN
                                        mb.showinfo("CUIDADO", f"TE QUEDAN {self.intentos} INTENTOS.")
            
        #MENSAJE DE QUE EL USUARIO NO EXISTE
        except FileNotFoundError:
            mb.showinfo("INFO :)","EL USUARIO NO EXISTE")   

    #FUNCION QUE COMPRUEBA SI ES EL ESTUDIANTE REAL.
    def COMPROBARIDENTIDAD(self):
        #RUTA DONDE BUSCARA LOS ROSTROS
        nombre = self.INU.get() 
        dataPath = 'C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/ROSTROS'
        imagePaths = os.listdir(dataPath)
        print('imagePaths=',imagePaths)

        face_recognizer = cv2.face.LBPHFaceRecognizer.create()

        # Leyendo el modelo
        modelPath = os.path.join(dataPath, nombre + '.xml')
        if os.path.isfile(modelPath):
            face_recognizer.read(modelPath)
        else:
            print(f'El archivo {nombre}.xml no existe en la ubicación especificada.')

        cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

        faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        rostro_conocido_detectado = False

        while True:
            ret,frame = cap.read()
            if ret == False: break
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            auxFrame = gray.copy()

            faces = faceClassif.detectMultiScale(gray,1.3,5)

            for (x,y,w,h) in faces:
                rostro = auxFrame[y:y+h,x:x+w]
                rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
                result = face_recognizer.predict(rostro)

                cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
                
                # LBPHFace
                if result[1] < 65:
                    cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                    rostro_conocido_detectado = True
                else:
                    cv2.putText(frame,'TU NO ERES ' + nombre ,(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
                
            cv2.imshow('frame',frame)
            k = cv2.waitKey(1)

            if rostro_conocido_detectado:
                self.VENTANAEST()
                break
                
            if k == 27: 
                break

        cap.release()
        cv2.destroyAllWindows()

    #FUNCION PARA PEDIR CONTRASEÑA
    def PEDIRCONTRA(self, ventana):

        #ASIGNACIONES DE VARIABLES INGRESADAS
        usuario = self.INU.get()
        archiuser = usuario
        #CARACTERES PARA LA CONTRASEÑA
        caracteres = string.ascii_letters + string.digits + string.punctuation
        #CANTIDAD DE DIGITOS
        longitud = 3
        #GENERACION DE UNA CONTRASEÑA RANDOM
        contrasena_aleatoria = ''.join(secrets.choice(caracteres) for _ in range(longitud))
        #ASIGNACION DE CONTRASEÑA A UNA VARIABLE 
        contrasena =  contrasena_aleatoria

        #ENCRIPTACION DE NUEVA CONTRASEÑA
        Encrip2 = hashlib.sha256(contrasena.encode()).hexdigest()

        #RUTA DEL LOS ARCHIVOS
        rutauser = "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/ESTUDIANTES/"
        ruta_completa = os.path.join(rutauser, archiuser + ".txt")

        try:
            with open(ruta_completa, "r", encoding="utf-8") as archicorreo:
                contenido = archicorreo.read()
                correogmail = re.findall(r'\S+@gmail\.com', contenido)
                CORREO = correogmail[0]
                print(CORREO)
                try:
                    nombre_archivo = ruta_completa
                    with open(nombre_archivo, "r") as archivo:
                        lineas = archivo.readlines()
                        lineas[0] = Encrip2
                        with open(nombre_archivo, "w") as archivo:
                            lineas = [line + "\n" for line in lineas]
                            archivo.writelines(lineas)
                        try:
                            #INFORMACION PARA EL CORREO ELECTRONICO
                            usuario = self.INU.get()
                            #CORREO ELECTRONICO DEL EMISOR
                            email_emisor = 'usac66654@gmail.com'
                            email_contra = 'yehr mcwg yqss ibsp'
                            #CORREO ELECTRONICO DEL RECEPTOR 
                            email_receptor2 = CORREO
                            #LISTA DE DESTINATARIOS PARA EL CORREO
                            destinatarios = [email_receptor2]
                            #ASUNTO Y CUERPO DEL CORREO ELECTRONICO
                            asunto = 'SEGURIDAD ACADEMIA USAC'
                            cuerpo = (usuario) + """  SU CONTRASEÑA A CAMBIADO A: \n    """ + ( contrasena ) 
                            #ASIGNACIONES DE LA LOCALIDAD EN EL #CORREO ELECTRONICO PARA EL ENVIO
                            em=EmailMessage()
                            em['from'] = email_emisor
                            em['To'] = ", ".join(destinatarios)
                            em['Subject'] = asunto
                            em.set_content(cuerpo)
                            #SEGURIDAD PARA EL ENVIO DE CORREO
                            contexto = ssl.create_default_context()
                            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as ADVERTENCIA:
                                ADVERTENCIA.login(email_emisor,email_contra)
                                ADVERTENCIA.sendmail(email_emisor,destinatarios, em.as_string())
                            
                            ventana.destroy()
                            #INFORMACION EN CONSOLA
                            mb.showinfo("INFO","CORREO ENVIADO")

                        except Exception:
                            mb.showinfo("INFO","INGRESE EL NOMBRE DE SU USUARIO PARA ENVIARLE EL CORREO")
                except Exception:
                    mb.showerror("ALERTA","PARECE QUE NO SE PUDO ENVIAR EL CORREO")
        except FileNotFoundError:
            mb.showinfo("INFO :)","EL USUARIO NO EXISTE, O NO HA COLOCADO SU NOMBRE DE USUARIO")  
     
    #ENVIO DE CORREO DE SEGURIDAD, ALERTA DE INGRESO
    def AVISOADMIN(self,ventana,CORREO):
        #CIERRE DE VENTANA
        ventana.destroy()
        #INFORMACION PARA EL CORREO ELECTRONICO
        usuario = self.INU.get()
        #CORREO ELECTRONICO DEL EMISOR
        email_emisor = 'usac66654@gmail.com'
        email_contra = 'yehr mcwg yqss ibsp'
        #CORREO ELECTRONICO DEL RECEPTOR (ADMIN)
        email_receptor = 'nswijm@gmail.com'
        email_receptor2 = CORREO
        #LISTA DE DESTINATARIOS PARA EL CORREO
        destinatarios = [email_receptor, email_receptor2]
        #ASUNTO Y CUERPO DEL CORREO ELECTRONICO
        asunto = 'SEGURIDAD ACADEMIA USAC'
        cuerpo = """SE INTENTÓ INGRESAR A LA CUENTA\n ESTA CUENTA SERÁ BLOQUEADA\n CUENTA DEL USUARIO: \n    """ + ( usuario) 
        #ASIGNACIONES DE LA LOCALIDAD EN EL #CORREO ELECTRONICO PARA EL ENVIO
        em=EmailMessage()
        em['from'] = email_emisor
        em['To'] = ", ".join(destinatarios)
        em['Subject'] = asunto
        em.set_content(cuerpo)
        #SEGURIDAD PARA EL ENVIO DE CORREO
        contexto = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as ADVERTENCIA:
            ADVERTENCIA.login(email_emisor,email_contra)
            ADVERTENCIA.sendmail(email_emisor,destinatarios, em.as_string())
        #VENTANA DE BLOQUEO
        self.ventanalocker()
        #INFORMACION EN CONSOLA
        print("CORREO ENVIADO")
#----------------------------------------------------------------------------------------------------------#--------------------------------------------------------------      
    #VENTANA PRINCIPAL ESTUDIANTE
    def VENTANAEST(self):
        #INFO DEL ESTUDIANTE
        usuario = self.INU.get()
        #VENTANA
        ventanaES=tk.Toplevel()
        ventanaES.title("ACADEMIA USAC")
        ventanaES.configure(bg="aquamarine")
        ventanaES.wm_state('zoomed')

        #FUENTES PARA TEXTOS
        fuente_personalizada = tkFont.Font(family="Arial", size=14, weight="bold")

        #BIENVENIDA
        self.etiqueta = tk.Label(ventanaES, text="BIENVENIDO " + usuario, font=fuente_personalizada)
        self.etiqueta.grid(column=10, row=0)

        # MARCO PARA BOTONES
        frameMOSAES = ttk.Frame(ventanaES)
        frameMOSAES.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        #MOSTRAR CURSOS ASIGNADOS
        self.CURSASIGI = tk.Button(ventanaES, text="ASIGNACION DE CURSOS", font=fuente_personalizada, command=lambda: self.CURSASIG(ventanaES), width=26, height=15)
        self.CURSASIGI.grid(column=1, row=1, padx=.5, pady=50)

        #VER MIS CURSOS
        self.CURSVER = tk.Button(ventanaES, text="MIS CURSOS", font=fuente_personalizada, command=lambda: self.MISCURSOS(ventanaES), width=26, height=15)
        self.CURSVER.grid(column=2, row=1, padx=.5, pady=50)

        #VER MIS CURSOS
        self.CURSVER = tk.Button(ventanaES, text="MI INFORMACION", font=fuente_personalizada, command=lambda: self.MIINFO(ventanaES), width=26, height=15)
        self.CURSVER.grid(column=3, row=1, padx=.5, pady=50)

        #UBICACION DE MOSAICOS
        directorio = "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/MOSAICOS/"  
        archivos = os.listdir(directorio)

        #GENERADOR DE BOTONES PARA MOSAICOS
        for i, archivo in enumerate(archivos):
            if os.path.isfile(os.path.join(directorio, archivo)):
                boton = tk.Button(ventanaES, text=archivo, command=lambda a=archivo: self.mostrar_info(os.path.join(directorio, a)),width=15,height=5)
                boton.grid(row=i, column=0, sticky="e")

        #CERRAR SESION
        self.CIERRE_SESION = tk.Button(ventanaES, text="CERRAR SESION", font=fuente_personalizada, command=lambda: self.CIERRESESION(ventanaES), width=26, height=15)
        self.CIERRE_SESION.grid(column=10, row=1, padx=.5, pady=50)
#----------------------------------------------------------------------------------------------------------#--------------------------------------------------------------
    #MOSTRAR INFORMACION DE MOSAICOS
    def mostrar_info(self, archivo):
        try:
            with open(archivo, 'r') as f:
                contenido = f.read()

            ventana_info = tk.Toplevel()
            ventana_info.title("Información del archivo")
            ventana_info.geometry("400x400")

            texto_info = Text(ventana_info)
            texto_info.insert("1.0", contenido)
            texto_info.pack(fill="both", expand=True)

        except Exception as e:
            mb.showerror("Error", f"No se pudo abrir el archivo: {str(e)}")
#----------------------------------------------------------------------------------------------------------#--------------------------------------------------------------
    #FUNCION QUE MOSTRARA UNA VENTANA CON DISTINTAS OPCIONES PARA LOS CURSOS
    def MISCURSOS(self, ventana):

        ventana.destroy()
        
        #VENTANA
        ventanaMC=tk.Toplevel()
        ventanaMC.title("ACADEMIA USAC, MIS CURSOS")
        ventanaMC.configure(bg="palegreen")
        ventanaMC.wm_state('zoomed')

        # MARCO PARA BOTONES
        frameES = ttk.Frame(ventanaMC)
        frameES.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        #VENTANA PARA VER MIS CURSOS
        text_boxTT = ScrolledText(ventanaMC, wrap=tk.WORD, width=80, height=25, state='disabled')
        text_boxTT.grid(row=0, column=3, padx=10, pady=10)
        text_boxTT.config(font=("Helvetica", 14))

        #BUSCAR CURSO
        self.etiqueta2 = tk.Label(ventanaMC, text="INGRESE SU NOMBRE DE USUARIO ")
        self.etiqueta2.grid(column=3, row= 3)

        #INGRESO DEL NOMBRE
        self.VERCURSO=tk.StringVar()
        Entry=ttk.Entry(ventanaMC, width=50, textvariable=self.VERCURSO)
        Entry.grid(column=3, row=4, padx=5, pady=5)

        #BOTON PARA MOSTRAR CURSOS
        mostrar_buttonME = ttk.Button(ventanaMC, text="MOSTRAR CURSOS", command= self.VERCURSOS)
        mostrar_buttonME.grid(row=3, column=1, padx=10, pady=20)

        #SALIR
        mostrar_buttonSE = ttk.Button(ventanaMC, text="SALIR", command=lambda: self.CERRARSES(ventanaMC))
        mostrar_buttonSE.grid(row=7, column=3, columnspan=2, padx=10, pady=10)

        # VARIABLE PARA LECTURA DE ARCHIVOS
        self.archivo_actualEV = None
        self.text_boxTT = text_boxTT
        self.frame = frameES

    #CERRAR VENTANA
    def CERRARSES(self, ventana):
        self.VENTANAEST()
        ventana.destroy()

    #FUNCION QUE GENERA A BOTONES LOS CURSOS
    def VERCURSOS(self):

        directorio = "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/CURSOS ESTUDIANTES/"  
        palabra = self.VERCURSO.get()
        archivos_encontrados = self.buscar_archivos_con_palabra2(directorio, palabra)

        if palabra != "":
            if archivos_encontrados:
                print("Archivos que contienen la palabra:", palabra)
                for archivo in archivos_encontrados:
                    boton = tk.Button(self.frame, text=archivo, command=lambda a=archivo: self.MOSTRARNOTA(a))
                    boton.pack()
            else:
                print(f"No se encontraron archivos que contengan la palabra: {palabra}")
        else:
            mb.showerror("ERROR","INGRESE SU NOMBRE DE USUARIO")

    #FUNCION QUE BUSCARA EL NOMBRE DEL ESTUDIANTE EN LA CARPETA DONDE ESTAN LOS CURSOS
    def buscar_archivos_con_palabra2(self, directorio, palabra_a_buscar):
        archivos_con_palabra = []

        for ruta, _, archivos in os.walk(directorio):
            for archivo in archivos:
                ruta_completa = os.path.join(ruta, archivo)
                try:
                    with open(ruta_completa, 'r', encoding='utf-8') as file:
                        contenido = file.read()
                        if palabra_a_buscar in contenido:
                            archivos_con_palabra.append(archivo)
                except Exception as e:
                    print(f"No se pudo abrir el archivo {archivo}: {e}")

        return archivos_con_palabra

    #FUNCION PARA MOSTRAR CURSO
    def MOSTRARNOTA(self, archivo):
        archi1 = archivo
        ruta = "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/CURSOS ESTUDIANTES/" 
        rutacompleta = os.path.join(ruta, archi1)
        estudiante = self.VERCURSO.get()

        if os.path.exists(rutacompleta):
            with open(rutacompleta, "r", encoding="utf-8") as file:
                lineas = file.readlines()

            nota_encontrada = False
            info = ""

            for linea in lineas:
                partes = linea.strip().split(":")
                if len(partes) == 2:
                    nombre, nota = partes[0], partes[1]
                    if nombre.strip() == estudiante:
                        nota_encontrada = True
                        info += f"{nombre.strip()}:{nota.strip()}\n"
                        nota1 = float(nota.strip())
                        print(nota1)
                        if nota1 > 61:
                            self.GENERARCERTIFICADO(archi1)

            if nota_encontrada:
                self.text_boxTT.configure(state='normal')
                self.text_boxTT.delete("1.0", "end")
                self.text_boxTT.insert("1.0", info)
                self.text_boxTT.configure(state='disabled')
            else:
                print(f"No se encontró la nota para el estudiante: {estudiante}")
        else:
            print(f"El archivo no existe.")
        
    #FUNCION QUE GENERA EL CERTIFICADO
    def GENERARCERTIFICADO(self, archivo):

        nombre = self.VERCURSO.get()
        
        # initializing variables with values
        fileName = 'certificado.pdf'
        documentTitle = 'sample' 
        title = archivo
        subTitle = '¡FELICIDADES POR GANAR ESTE CURSO!'
        textLines = [
            nombre,
            'ID Y ENSEÑAD A TODOS',
        ]
        image = 'C:/Users/Miguel Choc/Desktop/Proyecto USAC/ASDF.png'
        
        # creating a pdf object
        pdf = canvas.Canvas('C:/Users/Miguel Choc/Desktop/' + fileName)
        
        # setting the title of the document
        pdf.setTitle(documentTitle)
        
        # creating the title by setting it's font 
        # and putting it on the canvas
        pdf.setFont('Helvetica',36)
        pdf.drawCentredString(300, 770, title)
        
        #COLOR DE PAGINA
        pdf.setFillColorRGB(0, 0, 255)
        pdf.setFont("Courier-Bold", 24)
        pdf.drawCentredString(290, 720, subTitle)
        
        # drawing a line
        pdf.line(30, 710, 550, 710)
        
        # creating a multiline text using 
        # textline and for loop
        text = pdf.beginText(40, 680)
        text.setFont("Courier", 18)
        text.setFillColor(colors.red)
        for line in textLines:
            text.textLine(line)
        pdf.drawText(text)

        #INSERTAR IMAGEN
        pdf.drawInlineImage(image, 130, 400) 
        
        # saving the pdf
        pdf.save()
        mb.showinfo("FELICIDADES", "CERTIFICADO EN EL ESCRITORIO")
#----------------------------------------------------------------------------------------------------------#--------------------------------------------------------------
    #FUNCION QUE MUESTRA Y PUEDE EDITAR LA INFORMACION DEL ESTUDIANTE
    def MIINFO(self, ventana):
        #CIERRE DE VENTANA ANTERIOR 
        ventana.destroy()

        #FUENTES PARA TEXTOS
        style = ttk.Style()
        style.configure('Custom.TButton', font=('Verdana', 10, 'bold'))
        
       #VENTANA
        ventanaDATOSESTU = tk.Toplevel()
        ventanaDATOSESTU.wm_state('zoomed')
        ventanaDATOSESTU.title("EDICION ESTUDIANTE EN SU BASE DE DATOS.txt")

        #VENTANA PARA EDITAR INFORMACION DE CATEDRATICO
        self.text_box = ScrolledText(ventanaDATOSESTU, wrap=tk.WORD, width=110, height=25)
        self.text_box.grid(row=0, column=1, padx=10, pady=10)

        #BOTON PARA GUARDAR 
        guardar_button = ttk.Button(ventanaDATOSESTU, text="GUARDAR", command=lambda: self.GUARDADATOSESTU(ventanaDATOSESTU), style='Custom.TButton')
        guardar_button.grid(row=1, column=1, padx=10, pady=10)

        #BOTON PARA CANCELAR 
        cancelar_button = ttk.Button(ventanaDATOSESTU, text="CANCELAR / SALIR", command=lambda: self.CIERRADATOSESTU(ventanaDATOSESTU))
        cancelar_button.grid(row=1, column=2, columnspan=2, padx=10, pady=10)

        #BOTON PARA MOSTRAR 
        mostrar_button = ttk.Button(ventanaDATOSESTU, text="MOSTRAR DATOS", command= self.ABREDATOSESTU)
        mostrar_button.grid(row=0, column=3, columnspan=2, padx=10, pady=10)

        #CONTRASEÑA PARA ENCRIPTAR
        etiqueta_contraseña = tk.Label(ventanaDATOSESTU, text='INGRESE LA CONTRASEÑA:')
        etiqueta_contraseña.grid(row=2, column=1, padx=10, pady=10)

        #CELDA PARA INGRESAR CONTRASEÑA
        self.entrada_contraseña = tk.Entry(ventanaDATOSESTU)
        self.entrada_contraseña.grid(row=3, column=1, padx=10, pady=10)

        #BOTON PARA GENERAR CONTRASEÑA ENCRIPTADA
        boton_encriptar = ttk.Button(ventanaDATOSESTU, text='GENERAR CONTRASEÑA ENCRIPTADA', command=self.ENCRIPCONTRADATOSESTU)
        boton_encriptar.grid(row=4, column=1, padx=10, pady=10)

        #CELDA PARA MOSTRAR LA CONTRASEÑA ENCRIPTADA
        self.resultado_text = tk.Text(ventanaDATOSESTU, height=1, width=65)
        self.resultado_text.grid(row=5, column=1, padx=10, pady=10)

        #BOTON PARA COPIAR LA CONTRASEÑA
        boton_copiar = ttk.Button(ventanaDATOSESTU, text='COPIAR CONTRASEÑA ENCRIPTADA', command=lambda: self.COPIACONTRADATOSESTU(ventanaDATOSESTU))
        boton_copiar.grid(row=6, column=1, padx=10, pady=10)

    #FUNCION QUE ABRE Y MUESTRA LA INFORMACION DEL ARCHIVO ELEGIDO
    def ABREDATOSESTU(self):

        #ASIGNACION DE VARIABLE
        usuario = self.INU.get()
        #RUTA COMPLETA QUE SE VA A BUSCAR
        rutauserC= "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/ESTUDIANTES/"
        ruta_completa = os.path.join(rutauserC, usuario + ".txt")
        
        try:
            with open(ruta_completa, "r", encoding="UTF-8") as archivo:
                contenido = archivo.read()
                self.text_box.delete(1.0, tk.END)
                self.text_box.insert(tk.END, contenido)
        except FileNotFoundError:
            print(f"El archivo {ruta_completa} no existe.")

    #FUNCION PARA GUARDAR ARCHIVOS EDITADOS
    def GUARDADATOSESTU(self,ventanaDATOSESTU):

        #ASIGNACION DE VARIABLE
        usuario = self.INU.get()
        #RUTA COMPLETA QUE SE VA A BUSCAR
        rutauserC= "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/CATEDRATICOS/"
        ruta_completa = os.path.join(rutauserC, usuario + ".txt")

        contenido = self.text_box.get(1.0, tk.END)
        with open(ruta_completa, "w") as archivo:
            archivo.write(contenido)
            print("Archivo guardado con éxito.")
            ventanaDATOSESTU.destroy()
            self.VENTANAEST()

    #FUNCION AL CANCELAR EDICION 
    def CIERRADATOSESTU(self, ventanaDATOSESTU):
        ventanaDATOSESTU.destroy()
        self.VENTANAEST()

    #FUNCION PARA HACER UNA NUEVA CONTRASEÑA
    def ENCRIPCONTRADATOSESTU(self):
        contraseña = self.entrada_contraseña.get()
        if contraseña:
            encriptada = hashlib.sha256(contraseña.encode()).hexdigest()
            self.resultado_text.delete("1.0", "end") 
            self.resultado_text.insert("1.0", encriptada) 
        else:
            mb.showinfo("ERROR", "CELDA VACIA")

    #FUNCION PARA COPIAR TEXTO
    def COPIACONTRADATOSESTU(self,ventanaDATOSCATE):
        encriptada = self.resultado_text.get("1.0", "end-1c") 
        ventanaDATOSCATE.clipboard_clear()  
        ventanaDATOSCATE.clipboard_append(encriptada)  
        mb.showinfo("INFO","CONTRASEÑA COPIADA")
        ventanaDATOSCATE.update()

#----------------------------------------------------------------------------------------------------------#--------------------------------------------------------------
    #INICIO PARA LA ASIGNACION DE CURSOS
    def CURSASIG(self, ventana):

        #CERRAR VENTANA
        ventana.destroy()

        #VENTANA
        ventanaCURS=tk.Toplevel()
        ventanaCURS.title("ACADEMIA USAC")
        ventanaCURS.configure(bg="darkcyan")
        ventanaCURS.wm_state('zoomed')

        # MARCO PARA BOTONES
        frameES = ttk.Frame(ventanaCURS)
        frameES.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        #VENTANA PARA VER INFORMACION DE CURSOS
        text_boxCT = ScrolledText(ventanaCURS, wrap=tk.WORD, width=80, height=25, state='disabled')
        text_boxCT.grid(row=0, column=3, padx=10, pady=10)
        text_boxCT.config(font=("Helvetica", 14))

        #NOMBRE
        self.etiqueta2 = tk.Label(ventanaCURS, text="NOMBRE DEL CURSO ")
        self.etiqueta2.place(x=200, y=20)
        #PRECIO 
        self.etiqueta3 = tk.Label(ventanaCURS, text="PRECIO DEL CURSO Q ")
        self.etiqueta3.place(x=200, y=40)
        #CATEDRATICO    
        self.etiqueta4 = tk.Label(ventanaCURS, text="CATEDRATICO DEL CURSO ")
        self.etiqueta4.place(x=200, y=60)
        #CUPOS
        self.etiqueta5 = tk.Label(ventanaCURS, text="CUPOS DEL CURSO  ")
        self.etiqueta5.place(x=200, y=80)
        #CODIGO
        self.etiqueta6 = tk.Label(ventanaCURS, text="CODIGO DEL CURSO  ")
        self.etiqueta6.place(x=200, y=100)
        #FECHA DE INICIO
        self.etiqueta7 = tk.Label(ventanaCURS, text="FECHA DE INICIO ")
        self.etiqueta7.place(x=200, y=120)
        #FECHA DE FINALIZACION
        self.etiqueta8 = tk.Label(ventanaCURS, text="FECHA DE FINALIZACION ")
        self.etiqueta8.place(x=200, y=140)
        #HORA DE INICIO
        self.etiqueta9 = tk.Label(ventanaCURS, text="HORA DE INICIO ")
        self.etiqueta9.place(x=200, y=160)
        #HORA DE FINALIZACION
        self.etiqueta10 = tk.Label(ventanaCURS, text="HORA DE FINALIZACION ")
        self.etiqueta10.place(x=200, y=180)

        
        #ASIGNAR CURSO
        mostrar_buttonAC = ttk.Button(ventanaCURS, text="ASIGNAR CURSO", command=lambda: self.ASIGNARCURS(ventanaCURS))
        mostrar_buttonAC.grid(row=5, column=3, padx=10, pady=10)


        #BOTON DE RELLENO
        RELLENO = ttk.Button(ventanaCURS, text=".")
        RELLENO.grid(row=0, column=2, padx=10, pady=10)
        


        #INGRESE EL NOMBRE DEL CURSO
        self.etiqueta1 = tk.Label(ventanaCURS, text="INGRESE EL NOMBRE DEL CURSO ")
        self.etiqueta1.grid(column=3, row= 2)

        #INGRESO DEL NOMBRE
        self.ICUSAC=tk.StringVar()
        Entry=ttk.Entry(ventanaCURS, width=50, textvariable=self.ICUSAC)
        Entry.grid(column=3, row=4, padx=5, pady=5)

        #DESASIGNAR CURSO
        mostrar_buttonDC = ttk.Button(ventanaCURS, text="DESASIGNAR CURSO", command=lambda: self.DESASIGNARCURSOS(ventanaCURS))
        mostrar_buttonDC.grid(row=6, column=3, padx=10, pady=20)

        #BOTON PARA MOSTRAR CURSOS
        mostrar_buttonMC = ttk.Button(ventanaCURS, text="MOSTRAR CURSOS", command= self.ABRECURSOS)
        mostrar_buttonMC.grid(row=3, column=1, padx=10, pady=20)

        #SALIR
        mostrar_buttonS = ttk.Button(ventanaCURS, text="CANCELAR / SALIR", command=lambda: self.CERRAR(ventanaCURS))
        mostrar_buttonS.grid(row=7, column=3, columnspan=2, padx=10, pady=10)

        # VARIABLE PARA LECTURA DE ARCHIVOS
        self.archivo_actualEV = None
        self.text_box = text_boxCT
        self.frame = frameES

    #CERRAR VENTANA
    def CERRAR(self, ventana):
        self.VENTANAEST()
        ventana.destroy()

    #FUNCION QUE GENERA A BOTONES LOS CURSOS
    def ABRECURSOS(self):
        
        #FUENTES PARA TEXTOS
        style = ttk.Style()
        style.configure('Custom.TButton', font=('Verdana', 10, 'bold'))

        #RUTA DE ARCHIVOS PARA NOMBRAR BOTONES
        ruta_archivos = "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/CURSOS/"  
        archivos = [f for f in os.listdir(ruta_archivos) if f.endswith(".txt")]

        #GENERADOR DE BOTONES PARA CADA CURSO
        for archivo in archivos:
            button = ttk.Button(self.frame, text=archivo, style='Custom.TButton', command=lambda a=archivo: self.MOSTRARCURS(os.path.join(ruta_archivos, a)))
            button.grid(sticky="w")

    #FUNCION PARA MOSTRAR CURSO
    def MOSTRARCURS(self, archivo):
        
        with open(archivo, "r", encoding="utf-8") as file:
            contenido = file.read()
        print("Contenido del archivo:", contenido)
        self.text_box.configure(state='normal')
        self.text_box.delete("1.0", "end")
        self.text_box.insert("1.0", contenido)
        self.text_box.configure(state='disabled')
        
    #FUNCION PARA ASIGNAR CURSO
    def ASIGNARCURS(self, ventana):
        curso = self.ICUSAC.get()
        estudiante = self.INU.get()
        #RUTAS DE ARCHIVOS
        ruta1 = "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/ESTUDIANTES/"
        ruta2 = "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/CURSOS/"
        ruta3 = "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/CURSOS ESTUDIANTES"
        #RUTA COMPLETA
        rutacompleta1 = os.path.join(ruta1, estudiante + ".txt")
        rutacompleta2 = os.path.join(ruta2, curso + ".txt")
        rutacompleta3 = os.path.join(ruta3, curso + ".txt")
        notaz = random.randint(58, 100)

        try: 
            with open (rutacompleta1, "r", encoding="utf-8") as archi:
                contenido = archi.readlines()
                if curso in [line.strip() for line in contenido]:
                    mb.showerror("ESTUDIANTE", "YA ESTAS ASIGNADO EN ESTE CURSO")
                    self.VENTANAEST()
                    ventana.destroy()
                    archi.close()
                else:        
                    with open (rutacompleta2, "r", encoding="utf-8") as archi1:
                        lines = archi1.readlines()
                        archi1.close()
                        if len(lines) > 3:
                            cupos_disponibles = int(lines[3])
                            if cupos_disponibles > 0:
                                #RESTA DE CUPOS
                                cupos_disponibles -= 1
                                    
                                # ACTUALIZAR DATOS
                                lines[3] = str(cupos_disponibles) + "\n"
                                    
                                with open(rutacompleta2, "w", encoding="utf-8") as archi2:
                                    archi2.writelines(lines)
                                    archi2.close()
                                    with open(rutacompleta3, "a", encoding="utf-8") as archies:
                                        archies.write(estudiante + ":" + notaz )
                                        archies.close()
                                        with open (rutacompleta1, "a", encoding="utf-8") as archi3:
                                            archi3.write(curso + "\n")
                                            self.CURSOASIGNADO(ventana)
                            else:
                                mb.showinfo("NOOOOO", "CURSO LLENO")
                                self.VENTANAEST()
                                ventana.destroy()
        except FileNotFoundError:
            mb.showerror("ERROR", "ARCHIVO NO ENCONTRADO")
        except ValueError:
            mb.showerror("ERROR", "ERROR EN EL VALOR DE CUPO")
        except Exception as e:
            mb.showerror("ERROR", "OCURRIO UN ERROR: " + str(e))

    #FUNCION PARA DESASIGNAR CURSO    
    def DESASIGNARCURSOS(self,ventana):
        curso = self.ICUSAC.get()
        estudiante = self.INU.get()
        #RUTAS DE ARCHIVOS
        ruta1 = "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/ESTUDIANTES/"
        ruta2 = "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/CURSOS/"
        #RUTA COMPLETA
        rutacompleta1 = os.path.join(ruta1, estudiante + ".txt")
        rutacompleta2 = os.path.join(ruta2, curso + ".txt")

        try: 
            with open(rutacompleta1, "r", encoding="utf-8") as archi:
                contenido = archi.readlines()
                if curso in [line.strip() for line in contenido]:
                    #ELIMINAR CURSO EN EL ARCHIVO DEL ESTUDIANTE
                    contenido.remove(curso + "\n")
                    with open(rutacompleta1, "w", encoding="utf-8") as archi:
                        archi.writelines(contenido)
                    
                    #RESTAURAR CUPO EN EL CURSO
                    with open(rutacompleta2, "r", encoding="utf-8") as archi1:
                        lines = archi1.readlines()
                        if len(lines) > 3:
                            cupos_disponibles = int(lines[3])
                            cupos_disponibles += 1
                            lines[3] = str(cupos_disponibles) + "\n"
                            with open(rutacompleta2, "w", encoding="utf-8") as archi2:
                                archi2.writelines(lines)
                                self.CURSODESASIGNADO(ventana)
                else:
                    mb.showerror("ERROR", "TU NO ESTAS ASIGNADO")
                    ventana.destroy()
                    self.VENTANAEST()
        except FileNotFoundError:
            mb.showerror("ERROR", "ARCHIVO NO ENCONTRADO")
            ventana.destroy()
            self.VENTANAEST()
        except Exception as e:
            ventana.destroy()
            self.VENTANAEST()
            mb.showerror("ERROR", "OCURRIO UN ERROR: " + str(e))

    #FUNCION QUE ENVIA CORREO POR ASIGNACION
    def CURSOASIGNADO(self, ventana):
        #VARIABLES PARA INFO DEL CORREO
        estudiante = self.INU.get()
        #RUTAS DE ARCHIVOS
        ruta1 = "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/ESTUDIANTES/"
        #RUTA DE ARCHIVO PARA BUSCAR CORREO
        rutacompleta1 = os.path.join(ruta1, estudiante + ".txt")
        

        #ENCONTRAR CORREO Y DESIGNARLE UNA VARIABLE PARA ENVIO DE CORREO
        try:
            with open(rutacompleta1, "r", encoding="utf-8") as archicorreo:
                contenido = archicorreo.read()
                correogmail = re.findall(r'\S+@gmail\.com', contenido)
                CORREO = correogmail[0]
                print(CORREO)
        except Exception:
            mb.showerror("ERROR", "USUARIO NO ENCONTRADO")
        
        
        try:
            #INFORMACION PARA EL CORREO ELECTRONICO
            usuario = self.INU.get()
            #CORREO ELECTRONICO DEL EMISOR
            email_emisor = 'usac66654@gmail.com'
            email_contra = 'yehr mcwg yqss ibsp'
            #CORREO ELECTRONICO DEL RECEPTOR 
            email_receptor2 = CORREO
            #LISTA DE DESTINATARIOS PARA EL CORREO
            destinatarios = [email_receptor2]
            #ASUNTO Y CUERPO DEL CORREO ELECTRONICO
            asunto = 'INFORMACION ACADEMIA USAC'
            cuerpo = (usuario) + """  SU ASIGNACION FUE EXITOSA AL CURSO: \n    """ + ( self.ICUSAC.get() ) 
            #ASIGNACIONES DE LA LOCALIDAD EN EL #CORREO ELECTRONICO PARA EL ENVIO
            em=EmailMessage()
            em['from'] = email_emisor
            em['To'] = ", ".join(destinatarios)
            em['Subject'] = asunto
            em.set_content(cuerpo)
            #SEGURIDAD PARA EL ENVIO DE CORREO
            contexto = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as ADVERTENCIA:
                ADVERTENCIA.login(email_emisor,email_contra)
                ADVERTENCIA.sendmail(email_emisor,destinatarios, em.as_string())
                self.VENTANAEST() 
                ventana.destroy()
                #INFORMACION EN CONSOLA
                mb.showinfo("INFO","CORREO ENVIADO")

        except  Exception:
            mb.showerror("ERROR", "EL CORREO NO SE ENVIO")

    #FUNCION QUE ENVIA CORREO POR DESASIGNACION
    def CURSODESASIGNADO(self, ventana):
        #VARIABLES PARA INFO DEL CORREO
        estudiante = self.INU.get()
        #RUTAS DE ARCHIVOS
        ruta1 = "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/ESTUDIANTES/"
        #RUTA DE ARCHIVO PARA BUSCAR CORREO
        rutacompleta1 = os.path.join(ruta1, estudiante + ".txt")
        

        #ENCONTRAR CORREO Y DESIGNARLE UNA VARIABLE PARA ENVIO DE CORREO 
        try:
            with open(rutacompleta1, "r", encoding="utf-8") as archicorreo:
                contenido = archicorreo.read()
                correogmail = re.findall(r'\S+@gmail\.com', contenido)
                CORREO = correogmail[0]
                print(CORREO)
        except Exception:
            mb.showerror("ERROR", "USUARIO NO ENCONTRADO")
        
        
        try:
            #INFORMACION PARA EL CORREO ELECTRONICO
            usuario = self.INU.get()
            #CORREO ELECTRONICO DEL EMISOR
            email_emisor = 'usac66654@gmail.com'
            email_contra = 'yehr mcwg yqss ibsp'
            #CORREO ELECTRONICO DEL RECEPTOR 
            email_receptor2 = CORREO
            #LISTA DE DESTINATARIOS PARA EL CORREO
            destinatarios = [email_receptor2]
            #ASUNTO Y CUERPO DEL CORREO ELECTRONICO
            asunto = 'INFORMACION ACADEMIA USAC'
            cuerpo = (usuario) + """  SU DESASIGNACION FUE EXITOSA AL CURSO: \n    """ + ( self.ICUSAC.get() ) 
            #ASIGNACIONES DE LA LOCALIDAD EN EL #CORREO ELECTRONICO PARA EL ENVIO
            em=EmailMessage()
            em['from'] = email_emisor
            em['To'] = ", ".join(destinatarios)
            em['Subject'] = asunto
            em.set_content(cuerpo)
            #SEGURIDAD PARA EL ENVIO DE CORREO
            contexto = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as ADVERTENCIA:
                ADVERTENCIA.login(email_emisor,email_contra)
                ADVERTENCIA.sendmail(email_emisor,destinatarios, em.as_string())
                self.VENTANAEST() 
                ventana.destroy()
                #INFORMACION EN CONSOLA
                mb.showinfo("INFO","CORREO ENVIADO")

        except  Exception:
            mb.showerror("ERROR", "EL CORREO NO SE ENVIO")
#----------------------------------------------------------------------------------------------------------#--------------------------------------------------------------    
    #INICIO COMO CATEDRATICO
    def CatedraticoUSAC(self):
        #VENTANA
        ventana=tk.Toplevel()
        ventana.title("INICIO DE SESION COMO CATEDRATICO")
        #FUENTES PARA TEXTOS
        fuente_personalizada = tkFont.Font(family="Arial", size=12, weight="bold")
        fuente_personalizada2 = tkFont.Font(family="Arial", size=10, weight="bold")
        #INFORMACION QUE SE PIDE
        self.CA=tk.Label(ventana, text="INGRESE SU USUARIO", font=fuente_personalizada)
        self.CA.grid(column=0, row=4)
        self.CAT=tk.Label(ventana, text="INGRESE SU CONTRASEÑA", font=fuente_personalizada)
        self.CAT.grid(column=0, row=6)
        #INFORMACION INGRESADA
        self.CAU=tk.StringVar()
        Entry=ttk.Entry(ventana, width=50, textvariable=self.CAU)
        Entry.grid(column=0, row=5, padx=5, pady=5)
        self.CACON=tk.StringVar()
        Entry1=ttk.Entry(ventana, width=50, textvariable=self.CACON, show="*")
        Entry1.grid(column=0, row=7, padx=5, pady=5)
        #BOTON PARA GUARDAR INFORMACION
        self.BotonADM=tk.Button(ventana, text="INICIAR", font=fuente_personalizada2, command=lambda: self.COMPROBARCATE(ventana))
        self.BotonADM.grid(column=0, row=20, padx=5, pady=5)
        # CONTADOR DE INTENTOS
        self.intentos = 3
    
    #COMPROBACION DE LA INFORMACION INGRESADA
    def COMPROBARCATE(self, ventana):
        #VARIABLE PARA LA COMPROBACION SI EL ESTUDIANTE HA SIDO BLOQUEADO
        BLOCK = "BLOQUEADO"
        #RUTA DEL LOS ARCHIVOS
        rutauserca = "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/CATEDRATICOS/"
        #ASIGNACIONES DE VARIABLES INGRESADAS
        usuario = self.CAU.get()
        contrasena = self.CACON.get()  
        #ENCRIPTACION DE CONTRASEÑA
        Encrip2 = hashlib.sha256(contrasena.encode()).hexdigest()
        #NOMBRE DEL ARCHIVO A BUSCAR                    
        archiuser = usuario    
        #RUTA COMPLETA QUE SE VA A BUSCAR
        ruta_completa = os.path.join(rutauserca, archiuser + ".txt")     
        #CONTRASEÑA MAESTRA
        Encripmaster = "57d264e19d9846091986a22b3f250ab4c39161fdabb388e42a957d0f460d0231"    
        Encripmaster2 ="bc8db39f614342b78a67494dbece216d3726f6924b73563be34fc630ac1db7f5"
         
        try:
            if usuario != "" and contrasena !="":
                if Encrip2 == Encripmaster:
                    with open(ruta_completa, "r", encoding="utf-8") as archi1:
                        lineas = archi1.readlines()
                    with open(ruta_completa, "w", encoding="utf-8") as archi:
                        for linea in lineas:
                            if BLOCK not in linea:
                                nueva_linea = linea.replace(BLOCK, '')
                                archi.write(nueva_linea)
                elif Encrip2 == Encripmaster2:
                    mb.showinfo("INFO", "CUENTA DESBLOQUEDA")
                    self.VENTANACATE()
                    ventana.destroy() 
                else:
                    #COMPROBAR SI EL CATEDRATICO EXISTE, ABRIR ARCHIVO EN MODO LECTURA
                    with open(ruta_completa, "r", encoding="utf-8") as archi1:
                        contenido = archi1.readlines()  
                        
                        #ALERTA DE QUE LA CUENTA ESTA BLOQUEADA
                        if BLOCK in [line.strip() for line in contenido]:      
                            mb.showerror("ERROR","TU CUENTA ESTA BLOQUEADA")

                        else:
                            #COMPROBACION DE NOMBRE DE USUARIO     
                            if usuario in [line.strip() for line in contenido]:
                                #COMPROBACION DE CONTRASEÑA INGRESADA
                                if Encrip2 in [line.strip() for line in contenido]:
                                    print(Encrip2)
                                    #CIERRA ARCHIVO Y ABRE LA VENTANA PRINCIPAL DEL CATEDRATICO
                                    archi1.close()
                                    self.VENTANACATE()
                                    ventana.destroy()
                                else:
                                    #ALERTA DE CONTRASEÑA INCORRECTA Y CONTEO DE INTENTOS
                                    mb.showerror("ALERTA","CONTRASEÑA INCORRECTA")
                                    self.intentos -= 1
                                    if self.intentos == 0:
                                        #ALERTA FINAL POR INTENTO DE ENTRAR A LA CUENTA
                                        mb.showerror("ALERTA", "TRES INTENTOS FALLIDOS, TE CAERA EL ADMIN >:v")
                                        #CIERRA ARCHIVO DEL CATEDRATICO QUE ESTA EN MODO LECTURA
                                        archi1.close()
                                        #ABRE ARCHIVO DEL CATEDRATICO EN MODO AÑADIR
                                        with open(ruta_completa, "a", encoding="utf-8") as archi2:
                                            #ESCRITURA PARA BLOQUEAR USUARIO Y AVISO DEL BLOQUEO AL MISMO
                                            archi2.write("BLOQUEADO")
                                            archi2.close()
                                            self.AVISOADMIN2(ventana) 
                                    else:
                                        #AVISO DE INTENTOS QUE QUEDAN
                                        mb.showinfo("CUIDADO", f"TE QUEDAN {self.intentos} INTENTOS.")
            else: 
                mb.showerror("ALERTA", "CELDA/S VACIAS")
        #MENSAJE DE QUE EL USUARIO NO EXISTE
        except FileNotFoundError:
            mb.showinfo("INFO :)","EL USUARIO NO EXISTE") 

    #ENVIO DE CORREO AL ADMIN
    def AVISOADMIN2(self, ventana):
        #CIERRE DE VENTANA
        ventana.destroy()
        #INFORMACION DEL CORREO ELECTRONICO
        usuario = self.CAU.get()
        #CORREO ELECTRONICO DEL EMISOR
        email_emisor = 'usac66654@gmail.com'
        email_contra = 'yehr mcwg yqss ibsp'
        #CORREO ELECTRONICO DEL RECEPTOR (ADMIN)
        email_receptor = 'nswijm@gmail.com'
        #LISTA DE DESTINATARIOS PARA EL CORREO
        destinatarios = [email_receptor]
        #ASUNTO Y CUERPO DEL CORREO ELECTRONICO
        asunto = 'SEGURIDAD ACADEMIA USAC'
        cuerpo = """SE INTENTÓ INGRESAR A LA CUENTA\n ESTA CUENTA SERÁ BLOQUEADA\n CUENTA DEL CATEDRATICO: \n    """ + ( usuario) 
        #ASIGNACIONES DE LA LOCALIDAD EN EL #CORREO ELECTRONICO PARA EL ENVIO
        em=EmailMessage()
        em['from'] = email_emisor
        em['To'] = ", ".join(destinatarios)
        em['Subject'] = asunto
        em.set_content(cuerpo)
        #SEGURIDAD PARA EL ENVIO DE CORREO
        contexto = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as ADVERTENCIA:
            ADVERTENCIA.login(email_emisor,email_contra)
            ADVERTENCIA.sendmail(email_emisor,destinatarios, em.as_string())
        #VENTANA DE BLOQUEO
        self.ventanalocker()
        #INFORMACION EN CONSOLA
        print("CORREO ENVIADO")
#----------------------------------------------------------------------------------------------------------#--------------------------------------------------------------      
    #VENTANA PRINCIPAL DEL CATEDRATICO
    def VENTANACATE(self):

        #INFO DE VENTANA ADMIN
        ventanaCatedra= tk.Toplevel()
        ventanaCatedra.title("BIENVENIDO " + self.CAU.get())
        ventanaCatedra.configure(bg="aqua")
        ventanaCatedra.wm_state('zoomed')
        #FUENTES PARA TEXTOS
        fuente_personalizada = tkFont.Font(family="Verdana Bold", size=15)
        #BOTONES PARA LAS ACCIONES COMO CATEDRATICO   
        #AÑADIR CURSO
        self.AÑADIRCURSOCA = tk.Button(ventanaCatedra, text="AÑADIR CURSO", font=fuente_personalizada, command=lambda: self.AÑADIRCURS1(ventanaCatedra), width=26, height=15)
        self.AÑADIRCURSOCA.grid(column=0, row=0, padx=5, pady=5)
        #VER ESTUDIANTES
        self.ESTUDIANTES = tk.Button(ventanaCatedra, text="ESTUDIANTES", font=fuente_personalizada, command=lambda: self.ESTUDIANTESNOTES(ventanaCatedra), width=26, height=15)
        self.ESTUDIANTES.grid(column=1, row=0, padx=.5, pady=5)
        #EDICION DE DATOS PERSONALES
        self.DATPER = tk.Button(ventanaCatedra, text="DATOS PERSONALES", font=fuente_personalizada, command=lambda: self.DATOSCATE(ventanaCatedra), width=26, height=15)
        self.DATPER.grid(column=2, row=0, padx=.5, pady=5)
        #EDICION DE DATOS PERSONALES
        self.DATPER = tk.Button(ventanaCatedra, text="MODIFICAR CURSOS", font=fuente_personalizada, command=lambda: self.MODCURSCATE(ventanaCatedra), width=26, height=15)
        self.DATPER.grid(column=3, row=0, padx=.5, pady=5)
        #CERRAR SESION
        self.CIERRE_SESION = tk.Button(ventanaCatedra, text="CERRAR SESION", font=fuente_personalizada, command=lambda: self.CIERRESESION(ventanaCatedra), width=26, height=15)
        self.CIERRE_SESION.grid(column=3, row=1, padx=.5, pady=50)
#----------------------------------------------------------------------------------------------------------#--------------------------------------------------------------
    #FUNCION QUE ABRE UNA VENTANA PARA INGRESO DE LOS DATOS DEL CURSO
    def AÑADIRCURS1(self,ventana):
        
        #CIERRA VENTANA ANTERIOR
        
        ventana.destroy()
        
        #VENTANA
        
        ventanacates = tk.Toplevel()
        
        #TITULO E INFORMACIÓN DE LA VENTANA
        
        ventanacates.title("AÑADIR CURSO")
        color_rgb = (103, 99, 202 ) 
        ventanacates.configure(bg="#%02x%02x%02x" % color_rgb)  
        
        ventanacates.wm_state('zoomed')
        
        #FUENTES PARA LOS TEXTOS

        fuente_titulo = tkFont.Font(family="Arial", size=14, weight="bold")
        fuente_personalizada = tkFont.Font(family="Arial", size=10, weight="bold")
        
        #INGRESO DE INFORMACION DEL CURSO
        #NOMBRE DEL CURSO
        
        self.NameCurs=tk.Label(ventanacates, text="INGRESE EL NOMBRE DEL CURSO",font=fuente_personalizada)
        self.NameCurs.grid(column=0, row=0, padx=0, pady=10)
        
        #NOMBRE DEL CURSO INGRESADO
        
        self.NameCursIC=tk.StringVar()
        NameCursP=ttk.Entry(ventanacates, width=50, textvariable=self.NameCursIC)
        NameCursP.grid(column=1, row=0, padx=0, pady=10)
        
        #PRECIO DEL CURSO
        
        self.precurs=tk.Label(ventanacates, text="INGRESE EL PRECIO DEL CURSO EN Q.",font=fuente_personalizada)
        self.precurs.grid(column=0, row=1, padx=0, pady=10)
        
        #PRECIO DEL CURSO INGRESADO
        
        self.precursIC=tk.StringVar()
        precursP=ttk.Entry(ventanacates, width=50, textvariable=self.precursIC)
        precursP.grid(column=1, row=1, padx=0, pady=10)
        
        #CATEDRATICO QUE IMPARTIRA EL CURSO
        
        self.catecurs=tk.Label(ventanacates, text="INGRESE EL NOMBRE DEL CATEDRATICO",font=fuente_personalizada)
        self.catecurs.grid(column=0, row=2, padx=0, pady=10)
        
        #CATEDRATICO DEL CURSO INGRESADO
        
        self.catecursIC=tk.StringVar()
        catecursP=ttk.Entry(ventanacates, width=50, textvariable=self.catecursIC)
        catecursP.grid(column=1, row=2, padx=0, pady=10)
        
        #CUPOS DEL CURSO
        
        self.cupocurs=tk.Label(ventanacates, text="INGRESE LA CANTIDAD DE CUPOS DEL CURSO",font=fuente_personalizada)
        self.cupocurs.grid(column=0, row=3, padx=0, pady=10)
        
        #CUPOS DEL CURSO INGRESADO
        
        self.cupocursIC=tk.StringVar()
        cupocursP=ttk.Entry(ventanacates, width=50, textvariable=self.cupocursIC)
        cupocursP.grid(column=1, row=3, padx=0, pady=10)
        
        #########################################
        #FECHA Y HORARIO DEL CURSO
        
        self.horcurs=tk.Label(ventanacates, text="INGRESE LOS SIGUIENTES DATOS DEL CURSO",font=fuente_titulo)
        self.horcurs.grid(column=1, row=4, columnspan=2, padx=0, pady=20)

        #FECHA DE INICIO

        self.FIcurs=tk.Label(ventanacates, text="INGRESE LA FECHA DE INICIO DEL CURSO DEL CURSO\n INGRESAR COMO ## / ## / ####",font=fuente_personalizada)
        self.FIcurs.grid(column=0, row=5, padx=10, pady=10)
        
        #FECHA DE INICIO DEL CURSO INGRESADO
        
        self.horcursFeInC=tk.StringVar()
        horcursFI=ttk.Entry(ventanacates, width=50, textvariable=self.horcursFeInC)
        horcursFI.grid(column=0, row=6, padx=10, pady=10)

        #FECHA DE FINALIZACION

        self.FFcurs=tk.Label(ventanacates, text="INGRESE LA FECHA DE FINALIZACION DEL CURSO\n INGRESAR COMO ## / ## / ####",font=fuente_personalizada)
        self.FFcurs.grid(column=1, row=5, padx=10, pady=10)

        #FECHA DE FINALIZACION DEL CURSO INGRESADO
        
        self.horcursFeFinC=tk.StringVar()
        horcursFF=ttk.Entry(ventanacates, width=50, textvariable=self.horcursFeFinC)
        horcursFF.grid(column=1, row=6, padx=10, pady=10)

        #HORA DE INICIO

        self.FFcurs=tk.Label(ventanacates, text="INGRESE LA HORA DE INICIO DEL CURSO\n INGRESAR COMO ## : ##",font=fuente_personalizada)
        self.FFcurs.grid(column=2, row=5, padx=10, pady=10)

        #HORA DE INICIO DEL CURSO INGRESADO

        self.horcursHorInC=tk.StringVar()
        horcursHP=ttk.Entry(ventanacates, width=50, textvariable=self.horcursHorInC)
        horcursHP.grid(column=2, row=6, padx=10, pady=10)

        #HORA DE FINALIZACION

        self.FFcurs=tk.Label(ventanacates, text="INGRESE LA HORA QUE FINALIZA EL CURSO\n INGRESAR COMO ## : ##",font=fuente_personalizada)
        self.FFcurs.grid(column=3, row=5, padx=10, pady=10)

        #HORA DE FINALIZACION DEL CURSO INGRESADO

        self.horcursHorFinC=tk.StringVar()
        horcursFP=ttk.Entry(ventanacates, width=50, textvariable=self.horcursHorFinC)
        horcursFP.grid(column=3, row=6, padx=10, pady=10)
        
        #########################################

        #CODIGO DEL CURSO
        
        self.codecurs=tk.Label(ventanacates, text="INGRESE EL CODIGO DEL CURSO",font=fuente_personalizada)
        self.codecurs.grid(column=0, row=7, padx=0, pady=10)
        
        #CODIGO DEL CURSO INGRESADO
        
        self.codecursIC=tk.StringVar()
        codecursP=ttk.Entry(ventanacates, width=50, textvariable=self.codecursIC)
        codecursP.grid(column=1, row=7, padx=0, pady=10)

        # BOTON PARA GUARDAR CURSO
        
        self.Boton4=tk.Button(ventanacates, text="GUARDAR CURSO", font=fuente_titulo, command=lambda: self.COMPROBARCURSO2(ventanacates))
        self.Boton4.grid(column=1, row=9, padx=5, pady=20, columnspan=2)
        

        #BOTON DE CANCELAR

        self.BotonCursCan = tk.Button(ventanacates, text="CANCELAR CURSO", font=fuente_titulo, command=lambda: (self.VENTANACATE(), ventanacates.destroy()))
        self.BotonCursCan.grid(column=0, row=10, padx=5, pady=5)
        self.ventana1.mainloop()

    #FUNCION QUE COMPROBARA ALGUNOS DE LOS DATOS INGRESADOS DEL CURSO
    def COMPROBARCURSO2(self, ventana):

        #ASIGNACION DE VARIABLES: 

        nombrecurso = self.NameCursIC.get()
        preciocurso = self.precursIC.get()
        catedraticocurso = self.catecursIC.get()
        cuposcurso = self.cupocursIC.get()
        codigocurso = self.codecursIC.get()
        FeIn = self.horcursFeInC.get()
        FeFin = self.horcursFeFinC.get()
        HorIn = self.horcursHorInC.get()
        HorFin = self.horcursHorFinC.get()

        #RUTA DEL LOS ARCHIVOS

        rutauser = "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/CATEDRATICOS/"

        #NOMBRE DEL ARCHIVO A BUSCAR                    

        archiuser = catedraticocurso

        #RUTA COMPLETA QUE SE VA A BUSCAR

        ruta_completa = os.path.join(rutauser, archiuser + ".txt")

        
        try:
            #COMPROBACION DE DATOS EN LAS CELDAS

            if nombrecurso != "" and preciocurso != "" and catedraticocurso != "" and cuposcurso != "" and FeIn != "" and FeFin != "" and HorIn != "" and HorFin != "" and codigocurso != "":
           
            #DETERMINAR SI EL CATEDRATICO EXISTE    
           
                with open(ruta_completa, "r", encoding="utf-8") as archi1:
                    contenido = archi1.readlines()
           
                    #ABRIR ARCHIVO SI ES QUE EXISTE
           
                    with open(ruta_completa, "r", encoding="utf-8") as archi1:
                        contenido = archi1.read()
                        if not re.match(r'^\d+$', preciocurso):
                            mb.showerror("ALERTA", "EL PRECIO NO DEBE LLEVAR LETRAS")
                        else:
           
                            #INDICAR SI EL CATEDRATICO TIENE SUS DATOS
           
                            if contenido.strip() != "":
           
                                #CODIGO DEL CURSO #### SOLO NUMEROS
           
                                if not re.match(r'^\d+$', codigocurso):
                                    mb.showerror("ALERTA", "EL CODIGO NO DEBE LLEVAR LETRAS")
                                elif len(codigocurso) < 4 or len(codigocurso) > 4:
                                    mb.showerror("ALERTA","EL CODIGO NO DEBE SER MAYOR O MENOR 4 NUMEROS")
                                else:
           
                                    #CUPOS DEL CURSO SOLO NUMEROS
           
                                    if not re.match(r'^\d+$', cuposcurso):
                                        mb.showerror("ALERTA", "EL CUPO NO DEBE LLEVAR LETRAS")
                                    else:
    
                                        #LLAMA A LA FUNCION QUE COMPROBARA LA FECHA Y EL HORARIO INGRESADO

                                        self.COMPROBACIONFECHAYHORARIO2(ventana)
           
                            #INDICARA QUE NO HAY INFORMACION DEL CATEDRATICO
           
                            else:
                                mb.showerror("ALERTA", "QUERIDO ADMIN EL CATEDRATICO INGRESADO NO EXISTE")
            else: 
                mb.showerror("ALERTA","QUERIDO ADMIN, FALTAN DATOS")
        except FileNotFoundError:
                if catedraticocurso:
                    mb.showerror("ALERTA", "EL CATEDRATICO NO EXISTE")
            
    #FUNCION QUE COMPROBARA LA FECHA Y EL HORARIO INGRESADO
    def COMPROBACIONFECHAYHORARIO2(self,ventana):

        #ASIGNACION DE VARIABLES

        FeIn = self.horcursFeInC.get()
        FeFin = self.horcursFeFinC.get()
        HorIn = self.horcursHorInC.get()
        HorFin = self.horcursHorFinC.get()

        #EXPRESIONES PARA EL FORMATO DE FECHA Y HORA

        fecha_regex = r'\d{2}/\d{2}/\d{4}'
        hora_regex = r'\d{2}:\d{2}'
        hora_invalida = re.match(hora_regex, HorIn)
        hora_fin_invalida = re.match(hora_regex, HorFin)

        #COMPROBACION DE QUE EL FORMATO DE LAS FECHAS INGRESADAS SEA CORRECTO

        if re.match(fecha_regex, FeIn) and re.match(fecha_regex, FeFin):
            

            #COMPROBACION DE QUE EL FORMATO DE LA HORA INGRESADA SEA CORRECTO

            if hora_invalida and hora_fin_invalida:
                # Validación adicional para las horas
                horas_in, minutos_in = map(int, HorIn.split(':'))
                horas_fin, minutos_fin = map(int, HorFin.split(':'))
                
                if 0 <= horas_in <= 24 and 0 <= minutos_in <= 59 and 0 <= horas_fin <= 24 and 0 <= minutos_fin <= 59:
                    self.GUARDARCURSO2(ventana)
                
                #ALERTA DEL FORMATO DE HORAS Y MINUTOS

                else:
                    mb.showerror("ALERTA","LA HORA ES INCORRECTO ADMIN, DEBE IR COMO HORA/MINUTOS")
       
            #ALERTA DE FORMATO DE HORA MAL INGRESADA

            else:
                mb.showerror("ALERTA", "LA HORA ES INCORRECTA ADMNIN, DEBE IR COMO ##/##")
       
        #ALERTA DE FECHA MAL INGRESADA
        
        else:
            mb.showerror("ALERTA","LA FECHA ESTA INCORRECTA ADMIN, DEBE IR COMO ##/##/####")

    #FUNCION QUE GUARDARA LOS DATOS YA COMPROBADOS
    def GUARDARCURSO2(self, ventana):

        #ASIGNACION DE VARIABLES PARA LA ESCRITURA DEL CURSO

        preciocurso = self.precursIC.get()
        catedraticocurso = self.catecursIC.get()
        cuposcurso = self.cupocursIC.get()
        codigocurso = self.codecursIC.get()
        FeIn = self.horcursFeInC.get()
        FeFin = self.horcursFeFinC.get()
        HorIn = self.horcursHorInC.get()
        HorFin = self.horcursHorFinC.get()
        
        #NOMBRE DEL ARCHIVO.txt

        curso = self.NameCursIC.get()
        
        #RUTA DEL LOS ARCHIVOS

        rutaCURSO = "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/CURSOS/"

        #VARIABLE DEL ARCHIVO .TXT

        nuevo = os.path.join(rutaCURSO, curso + ".txt")

        #INTENTO DE GUARDADO DE DATOS INGRESADOS

        try:
            #ESCRITURA DE VARIABLES EN EL ARCHIVO
            with open(nuevo, "w", encoding="utf-8") as archi1:
                archi1.write(curso + "\n")
                archi1.write(preciocurso + "\n")
                archi1.write(catedraticocurso + "\n")
                archi1.write(cuposcurso + "\n")
                archi1.write(codigocurso + "\n")
                archi1.write(FeIn + "\n")
                archi1.write(FeFin + "\n")
                archi1.write(HorIn + "\n")
                archi1.write(HorFin + "\n")
                mb.showinfo("CURSO","CURSO GUARDADO")
                self.VENTANACATE()
                ventana.destroy()
        #INDICACION DE ERROR AL GUARDAR LOS DATOS                   
        except Exception:
            print("NO SE GUARDARON LOS DATOS")
#----------------------------------------------------------------------------------------------------------#--------------------------------------------------------------
    #BOTONES, VENTANA Y CELDAS PARA MODIFICAR INFORMACION DEL CATEDRATICO DESDE SU PERFIL
    def DATOSCATE(self, ventana):
        #CIERRE DE VENTANA ANTERIOR 
        ventana.destroy()

        #FUENTES PARA TEXTOS
        style = ttk.Style()
        style.configure('Custom.TButton', font=('Verdana', 10, 'bold'))
        
       #VENTANA
        ventanaDATOSCATE = tk.Toplevel()
        ventanaDATOSCATE.wm_state('zoomed')
        ventanaDATOSCATE.title("EDICION CATEDRATICOS EN SU BASE DE DATOS.txt")

        #VENTANA PARA EDITAR INFORMACION DE CATEDRATICO
        self.text_box = ScrolledText(ventanaDATOSCATE, wrap=tk.WORD, width=110, height=25)
        self.text_box.grid(row=0, column=1, padx=10, pady=10)

        #BOTON PARA GUARDAR 
        guardar_button = ttk.Button(ventanaDATOSCATE, text="GUARDAR", command=lambda: self.GUARDADATOSCATE(ventanaDATOSCATE), style='Custom.TButton')
        guardar_button.grid(row=1, column=1, padx=10, pady=10)

        #BOTON PARA CANCELAR 
        cancelar_button = ttk.Button(ventanaDATOSCATE, text="CANCELAR / SALIR", command=lambda: self.CIERRADATOSCATE(ventanaDATOSCATE))
        cancelar_button.grid(row=1, column=2, columnspan=2, padx=10, pady=10)

        #BOTON PARA MOSTRAR 
        mostrar_button = ttk.Button(ventanaDATOSCATE, text="MOSTRAR DATOS", command= self.ABREDATOSCATE)
        mostrar_button.grid(row=0, column=3, columnspan=2, padx=10, pady=10)

        #CONTRASEÑA PARA ENCRIPTAR
        etiqueta_contraseña = tk.Label(ventanaDATOSCATE, text='INGRESE LA CONTRASEÑA:')
        etiqueta_contraseña.grid(row=2, column=1, padx=10, pady=10)

        #CELDA PARA INGRESAR CONTRASEÑA
        self.entrada_contraseña = tk.Entry(ventanaDATOSCATE)
        self.entrada_contraseña.grid(row=3, column=1, padx=10, pady=10)

        #BOTON PARA GENERAR CONTRASEÑA ENCRIPTADA
        boton_encriptar = ttk.Button(ventanaDATOSCATE, text='GENERAR CONTRASEÑA ENCRIPTADA', command=self.ENCRIPCONTRADATOSCATE)
        boton_encriptar.grid(row=4, column=1, padx=10, pady=10)

        #CELDA PARA MOSTRAR LA CONTRASEÑA ENCRIPTADA
        self.resultado_text = tk.Text(ventanaDATOSCATE, height=1, width=65)
        self.resultado_text.grid(row=5, column=1, padx=10, pady=10)

        #BOTON PARA COPIAR LA CONTRASEÑA
        boton_copiar = ttk.Button(ventanaDATOSCATE, text='COPIAR CONTRASEÑA ENCRIPTADA', command=lambda: self.COPIACONTRADATOSCATE(ventanaDATOSCATE))
        boton_copiar.grid(row=6, column=1, padx=10, pady=10)

    #FUNCION QUE ABRE Y MUESTRA LA INFORMACION DEL ARCHIVO ELEGIDO
    def ABREDATOSCATE(self):

        #ASIGNACION DE VARIABLE
        usuario = self.CAU.get()
        #RUTA COMPLETA QUE SE VA A BUSCAR
        rutauserC= "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/CATEDRATICOS/"
        ruta_completa = os.path.join(rutauserC, usuario + ".txt")
        
        try:
            with open(ruta_completa, "r", encoding="UTF-8") as archivo:
                contenido = archivo.read()
                self.text_box.delete(1.0, tk.END)
                self.text_box.insert(tk.END, contenido)
        except FileNotFoundError:
            print(f"El archivo {ruta_completa} no existe.")

    #FUNCION PARA GUARDAR ARCHIVOS EDITADOS
    def GUARDADATOSCATE(self,ventanaDATOSCATE):

        #ASIGNACION DE VARIABLE
        usuario = self.CAU.get()
        #RUTA COMPLETA QUE SE VA A BUSCAR
        rutauserC= "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/CATEDRATICOS/"
        ruta_completa = os.path.join(rutauserC, usuario + ".txt")

        contenido = self.text_box.get(1.0, tk.END)
        with open(ruta_completa, "w") as archivo:
            archivo.write(contenido)
            print("Archivo guardado con éxito.")
            ventanaDATOSCATE.destroy()
            self.VENTANACATE()

    #FUNCION AL CANCELAR EDICION 
    def CIERRADATOSCATE(self, ventanaDATOSCATE):
        ventanaDATOSCATE.destroy()
        self.VENTANACATE()

    #FUNCION PARA HACER UNA NUEVA CONTRASEÑA
    def ENCRIPCONTRADATOSCATE(self):
        contraseña = self.entrada_contraseña.get()
        if contraseña:
            encriptada = hashlib.sha256(contraseña.encode()).hexdigest()
            self.resultado_text.delete("1.0", "end") 
            self.resultado_text.insert("1.0", encriptada) 
        else:
            mb.showinfo("ERROR", "CELDA VACIA")

    #FUNCION PARA COPIAR TEXTO
    def COPIACONTRADATOSCATE(self,ventanaDATOSCATE):
        encriptada = self.resultado_text.get("1.0", "end-1c") 
        ventanaDATOSCATE.clipboard_clear()  
        ventanaDATOSCATE.clipboard_append(encriptada)  
        mb.showinfo("INFO","CONTRASEÑA COPIADA")
        ventanaDATOSCATE.update()  
#----------------------------------------------------------------------------------------------------------#--------------------------------------------------------------
    #FUNCION QUE MODIFICARA LOS CURSOS
    def MODCURSCATE(self,ventana):

        #CIERRE DE VENTANA ANTERIOR 
        ventana.destroy()

        #FUENTES PARA TEXTOS
        style = ttk.Style()
        style.configure('Custom.TButton', font=('Verdana', 15, 'bold'))
        
        #VENTANA
        ventanaMODCURSCATE = tk.Toplevel()
        ventanaMODCURSCATE.wm_state('zoomed')
        ventanaMODCURSCATE.title("EDICION DE MOSAICOS EN SU BASE DE DATOS.txt")

        # MARCO PARA BOTONES
        frameCURSCATE = ttk.Frame(ventanaMODCURSCATE)
        frameCURSCATE.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        #BOTON PARA ACTUALIZAR 
        cargar_buttonCT = ttk.Button(ventanaMODCURSCATE, text="CARGAR CURSOS", command=self.CARGACURSCATE, style='Custom.TButton')
        cargar_buttonCT.grid(row=1, column=0, padx=10, pady=10)

        #VENTANA PARA EDITAR INFORMACION DE CATEDRATICOS
        text_boxCT = ScrolledText(ventanaMODCURSCATE, wrap=tk.WORD, width=100, height=25)
        text_boxCT.grid(row=0, column=1, padx=10, pady=10)

        #BOTON PARA GUARDAR ARCHIVOS
        guardar_buttonCT = ttk.Button(ventanaMODCURSCATE, text="GUARDAR", command=lambda: self.GUARDACURSCATE(ventanaMODCURSCATE), style='Custom.TButton')
        guardar_buttonCT.grid(row=1, column=1, padx=10, pady=10)

        #BOTON PARA CANCELAR ARCHIVOS
        cancelar_buttonCT = ttk.Button(ventanaMODCURSCATE, text="CANCELAR / SALIR", command=lambda: self.CIERRACURSCATE(ventanaMODCURSCATE), style='Custom.TButton')
        cancelar_buttonCT.grid(row=1, column=2, columnspan=2, padx=10, pady=10)

        # VARIABLE PARA EDICION Y LECTURA DE ARCHIVOS
        self.archivo_actualCT = None
        self.text_box = text_boxCT
        self.frame = frameCURSCATE

    #FUNCION QUE ABRE Y MUESTRA LA INFORMACION DEL ARCHIVO/CURSO ELEGIDO
    def ABRECURSCATE(self, archivo):
        global archivo_actualCT
        archivo_actualCT = archivo
        with open(archivo, "r", encoding="utf-8") as file:
            contenido = file.read()
        self.text_box.delete("1.0", "end")
        self.text_box.insert("1.0", contenido)

    #FUNCION PARA GUARDAR ARCHIVOS EDITADOS
    def GUARDACURSCATE(self, ventana):
        if archivo_actualCT:
            contenido = self.text_box.get("1.0", "end")
            with open(archivo_actualCT, "w", encoding="utf-8") as file:
                file.write(contenido)
                ventana.destroy()
                self.VENTANACATE()

    #FUNCION PARA ENCONTRAR Y MOSTRAR ARCHIVOS DE CURSOS
    def CARGACURSCATE(self):
        #FUENTES PARA TEXTOS
        style = ttk.Style()
        style.configure('Custom.TButton', font=('Verdana', 10, 'bold'))

        #RUTA DE ARCHIVOS PARA NOMBRAR BOTONES
        ruta_archivos = "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/CURSOS/"  
        archivos = [f for f in os.listdir(ruta_archivos) if f.endswith(".txt")]

        #GENERADOR DE BOTONES PARA CADA CURSO
        for archivo in archivos:
            button = ttk.Button(self.frame, text=archivo, style='Custom.TButton', command=lambda a=archivo: self.ABRECURSCATE(os.path.join(ruta_archivos, a)))
            button.grid(sticky="w")

    #FUNCION AL CANCELAR EDICION 
    def CIERRACURSCATE(self, ventana):
        ventana.destroy()
        self.VENTANACATE()
#----------------------------------------------------------------------------------------------------------#--------------------------------------------------------------
    #FUNCION PARA VER ESTUDIANTES ASIGNADOS
    def ESTUDIANTESNOTES(self, ventana):
        #CERRAR VENTANA
        ventana.destroy()

        #VENTANA
        ventanaESTCURS=tk.Toplevel()
        ventanaESTCURS.title("ACADEMIA USAC")
        ventanaESTCURS.configure(bg="teal")
        ventanaESTCURS.wm_state('zoomed')

        # MARCO PARA BOTONES
        frameES = ttk.Frame(ventanaESTCURS)
        frameES.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        #VENTANA PARA VER INFORMACION DE CURSOS
        text_boxTT = ScrolledText(ventanaESTCURS, wrap=tk.WORD, width=80, height=25, state='disabled')
        text_boxTT.grid(row=0, column=3, padx=10, pady=10)
        text_boxTT.config(font=("Helvetica", 14))


        #CURSO DEL CUAL BUSCAR ESTUDIANTES
        self.etiqueta2 = tk.Label(ventanaESTCURS, text="INGRESE EL NOMBRE DEL CURSO PARA MOSTRAR ESTUDIANTES ")
        self.etiqueta2.grid(column=3, row= 3)

        #INGRESO DEL NOMBRE
        self.VERESTU=tk.StringVar()
        Entry=ttk.Entry(ventanaESTCURS, width=50, textvariable=self.VERESTU)
        Entry.grid(column=3, row=4, padx=5, pady=5)

        #BOTON PARA MOSTRAR ESTUDIANTES
        mostrar_buttonME = ttk.Button(ventanaESTCURS, text="MOSTRAR ESTUDIANTES", command= self.VEREST)
        mostrar_buttonME.grid(row=3, column=1, padx=10, pady=20)

        #SALIR
        mostrar_buttonSE = ttk.Button(ventanaESTCURS, text="SALIR", command=lambda: self.CERRARSE(ventanaESTCURS))
        mostrar_buttonSE.grid(row=7, column=3, columnspan=2, padx=10, pady=10)

        # VARIABLE PARA LECTURA DE ARCHIVOS
        self.archivo_actualEV = None
        self.text_box = text_boxTT
        self.frame = frameES

    #CERRAR VENTANA
    def CERRARSE(self, ventana):
        self.VENTANACATE()
        ventana.destroy()

    #FUNCION QUE GENERA A BOTONES LOS CURSOS
    def VEREST(self):

        directorio = "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/CURSOS ESTUDIANTES/"  
        palabra = self.VERESTU.get() 
        archivos_encontrados = self.buscar_archivos_con_palabra(directorio, palabra)

        if palabra != "":
            if archivos_encontrados:
                print("Archivos que contienen la palabra:", palabra)
                for archivo in archivos_encontrados:
                    nombre_archivo = os.path.basename(archivo)
                    boton = tk.Button(self.frame, text=nombre_archivo , command=lambda a=archivo: self.MOSTRAREST(a))
                    boton.pack()
            else:
                print(f"No se encontraron archivos que contengan la palabra: {palabra}")
        else:
            mb.showerror("ERROR","INGRESE EL NOMBRE DEL CURSO")

    #FUNCION QUE BUSCARA EL NOMBRE DEL CURSO EN LOS ARCHIVOS DE LOS ESTUDIANTES
    def buscar_archivos_con_palabra(self, directorio, palabra):
            archivos_encontrados = []
            for root, dirs, files in os.walk(directorio):
                for archivo in files:
                    if palabra in archivo:
                        archivos_encontrados.append(os.path.join(root, archivo))
            return archivos_encontrados

    #FUNCION PARA MOSTRAR CURSO
    def MOSTRAREST(self, archivo):
        estudiante = archivo
        ruta = "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/CURSOS ESTUDIANTES/" 
        rutacompleta = os.path.join(ruta, estudiante)
        if os.path.exists(rutacompleta):
            with open(rutacompleta, "r", encoding="utf-8") as file:
                contenido = file.read()
            print("Contenido del archivo:", contenido)
            self.text_box.configure(state='normal')
            self.text_box.delete("1.0", "end")
            self.text_box.insert("1.0", contenido)
            self.text_box.configure(state='disabled')
        else:
            print(f"El archivo no existe.")
        
#----------------------------------------------------------------------------------------------------------#--------------------------------------------------------------    
    #INICIO DEL ADMINISTRADOR
    def AdminUSAC(self):
        #VENTANA
        ventanaAD=tk.Toplevel()
        ventanaAD.title("INICIO DE SESION COMO ADMIN")
        #FUENTES PARA TEXTOS
        fuente_personalizada = tkFont.Font(family="Arial", size=12, weight="bold")
        fuente_personalizada2 = tkFont.Font(family="Arial", size=10, weight="bold")
        #INFORMACION QUE SE PIDE
        self.AD=tk.Label(ventanaAD, text="INGRESE SU USUARIO ADMIN", font=fuente_personalizada)
        self.AD.grid(column=0, row=4)
        self.ADM=tk.Label(ventanaAD, text="INGRESE SU CONTRASEÑA ADMIN", font=fuente_personalizada)
        self.ADM.grid(column=0, row=6)
        #INFORMACION INGRESADA
        self.ADMU=tk.StringVar()
        Entry=ttk.Entry(ventanaAD, width=50, textvariable=self.ADMU)
        Entry.grid(column=0, row=5, padx=5, pady=5)
        self.ADMCON=tk.StringVar()
        Entry1=ttk.Entry(ventanaAD, width=50, textvariable=self.ADMCON, show="*")
        Entry1.grid(column=0, row=7, padx=5, pady=5)
        #BOTON PARA GUARDAR INFORMACION
        self.BotonADM=tk.Button(ventanaAD, text="COMENZAR", font=fuente_personalizada2, command=lambda: self.COMPROBARADMIN(ventanaAD))
        self.BotonADM.grid(column=0, row=20, padx=5, pady=5)  
        #CONTEO DE INTENTOS
        self.intentos = 3

    #COMPROBACION DE LA INFORMACION INGRESADA
    def COMPROBARADMIN(self, ventana):
        #ASIGNACION DE VARIABLES
        ADMUS = self.ADMU.get()
        ADMCON = self.ADMCON.get()
        USERADMIN = "USAC"
        CONTRAADMIN = "373"
        #DECLARACION DE QUE EL USUARIO Y CONTRASEÑA SEAN CORRECTOS
        if ADMUS == USERADMIN and ADMCON == CONTRAADMIN:
            ventana.destroy() 
            self.ADMIN()
        else:
            #CUENTA DE INTENTOS
            self.intentos -= 1
            #ALERTA DE DATOS ERRONEOS
            if self.intentos > 0:
                mb.showerror("ALERTA", f"DATOS INVALIDOS. TE QUEDAN {self.intentos} INTENTOS.")
            #ALERTA FINAL Y AVISO AL ADMIN
            else:
                mb.showerror("ALERTA", "HAS ALCANZADO EL LIMITE DE INTENTOS. EL ADMIN TE CASTIGARA >:v")
                ventana.destroy() 
                self.AVISOADMIN3()
                
    #ENVIO DE CORREO AL ADMIN OFICIAL
    def AVISOADMIN3(self):
        #CORREO ELECTRONICO DEL EMISOR
        email_emisor = 'usac66654@gmail.com'
        email_contra = 'yehr mcwg yqss ibsp'
        #CORREO ELECTRONICO DEL RECEPTOR (ADMIN)
        email_receptor = 'nswijm@gmail.com'
        #ASUNTO Y CUERPO DEL CORREO ELECTRONICO
        asunto = 'SEGURIDAD ACADEMIA USAC'
        cuerpo = """ESTAN INTENTANTO INGRESAR A SU USARIO QUERIDO ADMIN""" 
        #ASIGNACIONES DE LA LOCALIDAD EN EL #CORREO ELECTRONICO PARA EL ENVIO
        em=EmailMessage()
        em['from'] = email_emisor
        em['To'] = email_receptor
        em['Subject'] = asunto
        em.set_content(cuerpo)
        #SEGURIDAD PARA EL ENVIO DE CORREO
        contexto = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as ADVERTENCIA:
            ADVERTENCIA.login(email_emisor,email_contra)
            ADVERTENCIA.sendmail(email_emisor,email_receptor, em.as_string())
        #INFORMACION EN CONSOLA
        self.ventanalocker()
        print("CORREO ENVIADO")
#----------------------------------------------------------------------------------------------------------#--------------------------------------------------------------      
    #VENTANA DE BLOQUEO AL INFLITRANTE
    def ventanalocker(self):
        #VENTANA
        ventana = tk.Toplevel()
        #FUENTES PARA TEXTOS
        fuente_personalizada = tkFont.Font(family="Arial", size=17, weight="bold")
        #ABRE LA VENTANA EN TAMAÑO COMPLETO DE LA PANTALLA
        ventana.attributes('-fullscreen', True)  
        #QUITA LOS BOTONES DE CERRAR Y MINIMIZAR
        ventana.overrideredirect(True)  
        ventana.title("TE CAERA LA JUSTICIA")
        #INGRESO DE CONTRASEÑA PRINCIPAL
        AD = tk.Label(ventana, text="INGRESE LA CONTRASEÑA ADMIN DE VERDAD :'(", font=fuente_personalizada)
        AD.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        #CELDA DE INGRESO DE DATOS
        self.CON = tk.StringVar()
        Entry1 = ttk.Entry(ventana, width=50, textvariable=self.CON, show="*")
        Entry1.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        #BOTON DE CONFIRMACION
        boton = tk.Button(ventana, text="SOY EL ADMIN", command=lambda: self.verificar_contraseña(ventana),font=fuente_personalizada)
        boton.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        #CENTRARA ELEMENTOS
        ventana.grid_rowconfigure(0, weight=1)
        ventana.grid_rowconfigure(1, weight=1)
        ventana.grid_rowconfigure(2, weight=1)
        ventana.grid_columnconfigure(0, weight=1)
        ventana.grid_columnconfigure(1, weight=1)
        ventana.mainloop()
    
    #INGRESO DE CONTRASEÑA POR EL ADMIN
    def verificar_contraseña(self, ventana):
        contraadmin = self.CON.get()
        contraseña_correcta = "737"
        if contraadmin == contraseña_correcta:
            ventana.destroy()
#----------------------------------------------------------------------------------------------------------#--------------------------------------------------------------      
    #VENTANA PRINCIPAL DEL ADMINISTRADOR
    def ADMIN(self):
        #INFO DE VENTANA ADMIN
        ventanaAdmin= tk.Toplevel()
        ventanaAdmin.title("BIENVENIDO ADMIN")
        ventanaAdmin.configure(bg="gray")
        ventanaAdmin.wm_state('zoomed')
        #FUENTES PARA TEXTOS
        fuente_personalizada = tkFont.Font(family="Verdana Bold", size=15)
        #BOTONES PARA LAS ACCIONES COMO ADMIN    
        #AÑADIR CURSO
        self.AÑADIRCURSO = tk.Button(ventanaAdmin, text="AÑADIR CURSO", font=fuente_personalizada, command=lambda: self.AÑADIRCURS(ventanaAdmin), width=26, height=15)
        self.AÑADIRCURSO.grid(column=0, row=0, padx=5, pady=5)
        #AÑADIR MOSAICOS   
        self.CREAMOSAICOS = tk.Button(ventanaAdmin, text="CREAR MOSAICO", font=fuente_personalizada, command=lambda: self.CREARMOSA(ventanaAdmin), width=26, height=15)
        self.CREAMOSAICOS.grid(column=1, row=0, padx=5, pady=5)
        #MODIFICARMOSAICOS
        self.MODIFICARMOSAICOS = tk.Button(ventanaAdmin, text="MODIFICAR MOSAICOS", font=fuente_personalizada, command=lambda: self.MODMOSA(ventanaAdmin), width=26, height=15)
        self.MODIFICARMOSAICOS.grid(column=2, row=0, padx=5, pady=5)
        #AÑADIR CATEDRATICO
        self.AÑADIRCATEDRATICO = tk.Button(ventanaAdmin, text="AÑADIR CATEDRÁTICO", font=fuente_personalizada, command=lambda: self.AÑADIRCATE(ventanaAdmin), width=26, height=15)
        self.AÑADIRCATEDRATICO.grid(column=3, row=0, padx=5, pady=5)
        #VER CATEDRATICOS
        self.CATEDRATICOS = tk.Button(ventanaAdmin, text="CATEDRÁTICOS", font=fuente_personalizada, command=lambda: self.CATEDRATIC(ventanaAdmin), width=26, height=15)
        self.CATEDRATICOS.grid(column=4, row=0, padx=.5, pady=5)
        #VER CATEDRATICOS
        self.MODCURS = tk.Button(ventanaAdmin, text="MODIFICAR CURSOS", font=fuente_personalizada, command=lambda: self.MODCURSS(ventanaAdmin), width=26, height=15)
        self.MODCURS.grid(column=0, row=1, padx=.5, pady=5)
        #CERRAR SESION
        self.CIERRE_SESION = tk.Button(ventanaAdmin, text="CERRAR SESION", font=fuente_personalizada, command=lambda: self.CIERRESESION(ventanaAdmin), width=26, height=15)
        self.CIERRE_SESION.grid(column=1, row=1, padx=.5, pady=50)
#----------------------------------------------------------------------------------------------------------#--------------------------------------------------------------
    def CIERRESESION(self, ventana): 
        mb.showinfo("ADIOS","REGRESE PRONTO")
        ventana.destroy()
#----------------------------------------------------------------------------------------------------------#--------------------------------------------------------------  
    #FUNCION PARA CREAR MOSAICOS
    def CREARMOSA(self,ventana):
        
        #CIERRA VENTANA ANTERIOR
        
        ventana.destroy()
        
        #VENTANA
        
        ventanaM = tk.Toplevel()
        
        #TITULO E INFORMACIÓN DE LA VENTANA
        
        ventanaM.title("CREAR CATEDRATICO")
        color_rgb = (253, 178, 1) 
        ventanaM.configure(bg="#%02x%02x%02x" % color_rgb) 
        
        #FUENTES PARA LOS TEXTOS

        fuente_titulo = tkFont.Font(family="Arial", size=14, weight="bold")
        fuente_personalizada = tkFont.Font(family="Arial", size=10, weight="bold")

        #INGRESO DE NOMBRE DEL MOSAICO
        
        self.NameMos=tk.Label(ventanaM, text="INGRESE EL NOMBRE DEL MOSAICO",font=fuente_personalizada)
        self.NameMos.grid(column=0, row=0, padx=0, pady=10, columnspan=10)

        #NOMBRE DEL MOSAICO INGRESADO
        
        self.NameMosI=tk.StringVar()
        NameMosP=ttk.Entry(ventanaM, width=50, textvariable=self.NameMosI)
        NameMosP.grid(column=0, row=1, padx=0, pady=10, columnspan=10)

        #INGRESO DE INFORMACION DEL MOSAICO
        
        self.NameInMos=tk.Label(ventanaM, text="INGRESE INFORMACION PARA EL MOSAICO",font=fuente_personalizada)
        self.NameInMos.grid(column=0, row=2, padx=0, pady=10, columnspan=10)

        #INFORMACION DEL MOSAICO INGRESADA
        
        self.InMosI = tk.StringVar()
        self.InMosP = tk.Text(ventanaM, width=50, height=4)
        self.InMosP.grid(column=0, row=3, padx=0, pady=10, columnspan=10)

        #BOTON DE GUARDADO MOSAICOS

        self.BotonMos=tk.Button(ventanaM, text="GUARDAR MOSAICO", font=fuente_titulo, command=lambda: self.GUARDARMOSAICO(ventanaM))
        self.BotonMos.grid(column=0, row=4, padx=5, pady=20, columnspan=10)

        #BOTON DE CANCELAR

        self.BotonMosCan = tk.Button(ventanaM, text="CANCELAR MOSAICO", font=fuente_titulo, command=lambda: (self.ADMIN(), ventanaM.destroy()))
        self.BotonMosCan.grid(column=0, row=5, padx=5, pady=20, columnspan=10)
#----------------------------------------------------------------------------------------------------------#--------------------------------------------------------------
    #FUNCION QUE GUARDA LA INFORMACION DEL MOSAICO
    def GUARDARMOSAICO(self, ventana):  
        
        #ASIGNACION DE VARIABLES

        NameMos = self.NameMosI.get()
        InfoMos = self.InMosP.get("1.0", "end-1c")

        #NOMBRE DEL ARCHIVO DEL MOSAICO

        Namearchi = NameMos

        #RUTA DEL LOS ARCHIVOS

        rutaMosaicos = "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/MOSAICOS/"

        #VARIABLE DEL ARCHIVO .TXT

        nuevoMos = os.path.join(rutaMosaicos, Namearchi + ".txt")

        #COMPROBACION DE CELDAS LLENAS

        if NameMos != "" and InfoMos != "":

            #INTENTO DE GUARDADO DE DATOS INGRESADOS
            
            try: 
                with open(nuevoMos, "w", encoding="utf-8") as archi1:
                    archi1.write(NameMos + "\n")
                    archi1.write(InfoMos)
                    mb.showinfo("MOSAICO","MOSAICO GUARDADO")
                    self.ADMIN()
                    ventana.destroy()
            
            #ALERTA SI NO GUARDA LA INFORMACION        
            
            except Exception:
                mb.showerror("ALERTA","NO SE GUARDO EL ARCHIVO, LLAMAR AL TECNICO")
        
        #ALERTA DE CELDAS VACIAS
        
        else:
            mb.showerror("ALERTA","QUERIDO ADMIN, FALTAN DATOS")    
#----------------------------------------------------------------------------------------------------------#--------------------------------------------------------------
    #FUNCION QUE ABRE UNA VENTANA PARA INGRESO DE LOS DATOS DEL CURSO
    def AÑADIRCURS(self,ventana):
        
        #CIERRA VENTANA ANTERIOR
        
        ventana.destroy()
        
        #VENTANA
        
        ventana1 = tk.Toplevel()
        
        #TITULO E INFORMACIÓN DE LA VENTANA
        
        ventana1.title("AÑADIR CURSO")
        color_rgb = (253, 178, 1) 
        ventana1.configure(bg="#%02x%02x%02x" % color_rgb)  
        
        ventana1.wm_state('zoomed')
        
        #FUENTES PARA LOS TEXTOS

        fuente_titulo = tkFont.Font(family="Arial", size=14, weight="bold")
        fuente_personalizada = tkFont.Font(family="Arial", size=10, weight="bold")
        
        #INGRESO DE INFORMACION DEL CURSO
        #NOMBRE DEL CURSO
        
        self.NameCurs=tk.Label(ventana1, text="INGRESE EL NOMBRE DEL CURSO",font=fuente_personalizada)
        self.NameCurs.grid(column=0, row=0, padx=0, pady=10)
        
        #NOMBRE DEL CURSO INGRESADO
        
        self.NameCursI=tk.StringVar()
        NameCursP=ttk.Entry(ventana1, width=50, textvariable=self.NameCursI)
        NameCursP.grid(column=1, row=0, padx=0, pady=10)
        
        #PRECIO DEL CURSO
        
        self.precurs=tk.Label(ventana1, text="INGRESE EL PRECIO DEL CURSO EN Q.",font=fuente_personalizada)
        self.precurs.grid(column=0, row=1, padx=0, pady=10)
        
        #PRECIO DEL CURSO INGRESADO
        
        self.precursI=tk.StringVar()
        precursP=ttk.Entry(ventana1, width=50, textvariable=self.precursI)
        precursP.grid(column=1, row=1, padx=0, pady=10)
        
        #CATEDRATICO QUE IMPARTIRA EL CURSO
        
        self.catecurs=tk.Label(ventana1, text="INGRESE EL NOMBRE DEL CATEDRATICO",font=fuente_personalizada)
        self.catecurs.grid(column=0, row=2, padx=0, pady=10)
        
        #CATEDRATICO DEL CURSO INGRESADO
        
        self.catecursI=tk.StringVar()
        catecursP=ttk.Entry(ventana1, width=50, textvariable=self.catecursI)
        catecursP.grid(column=1, row=2, padx=0, pady=10)
        
        #CUPOS DEL CURSO
        
        self.cupocurs=tk.Label(ventana1, text="INGRESE LA CANTIDAD DE CUPOS DEL CURSO",font=fuente_personalizada)
        self.cupocurs.grid(column=0, row=3, padx=0, pady=10)
        
        #CUPOS DEL CURSO INGRESADO
        
        self.cupocursI=tk.StringVar()
        cupocursP=ttk.Entry(ventana1, width=50, textvariable=self.cupocursI)
        cupocursP.grid(column=1, row=3, padx=0, pady=10)
        
        #########################################
        #FECHA Y HORARIO DEL CURSO
        
        self.horcurs=tk.Label(ventana1, text="INGRESE LOS SIGUIENTES DATOS DEL CURSO",font=fuente_titulo)
        self.horcurs.grid(column=1, row=4, columnspan=2, padx=0, pady=20)

        #FECHA DE INICIO

        self.FIcurs=tk.Label(ventana1, text="INGRESE LA FECHA DE INICIO DEL CURSO DEL CURSO\n INGRESAR COMO ## / ## / ####",font=fuente_personalizada)
        self.FIcurs.grid(column=0, row=5, padx=10, pady=10)
        
        #FECHA DE INICIO DEL CURSO INGRESADO
        
        self.horcursFeIn=tk.StringVar()
        horcursFI=ttk.Entry(ventana1, width=50, textvariable=self.horcursFeIn)
        horcursFI.grid(column=0, row=6, padx=10, pady=10)

        #FECHA DE FINALIZACION

        self.FFcurs=tk.Label(ventana1, text="INGRESE LA FECHA DE FINALIZACION DEL CURSO\n INGRESAR COMO ## / ## / ####",font=fuente_personalizada)
        self.FFcurs.grid(column=1, row=5, padx=10, pady=10)

        #FECHA DE FINALIZACION DEL CURSO INGRESADO
        
        self.horcursFeFin=tk.StringVar()
        horcursFF=ttk.Entry(ventana1, width=50, textvariable=self.horcursFeFin)
        horcursFF.grid(column=1, row=6, padx=10, pady=10)

        #HORA DE INICIO

        self.FFcurs=tk.Label(ventana1, text="INGRESE LA HORA DE INICIO DEL CURSO\n INGRESAR COMO ## : ##",font=fuente_personalizada)
        self.FFcurs.grid(column=2, row=5, padx=10, pady=10)

        #HORA DE INICIO DEL CURSO INGRESADO

        self.horcursHorIn=tk.StringVar()
        horcursHP=ttk.Entry(ventana1, width=50, textvariable=self.horcursHorIn)
        horcursHP.grid(column=2, row=6, padx=10, pady=10)

        #HORA DE FINALIZACION

        self.FFcurs=tk.Label(ventana1, text="INGRESE LA HORA QUE FINALIZA EL CURSO\n INGRESAR COMO ## : ##",font=fuente_personalizada)
        self.FFcurs.grid(column=3, row=5, padx=10, pady=10)

        #HORA DE FINALIZACION DEL CURSO INGRESADO

        self.horcursHorFin=tk.StringVar()
        horcursFP=ttk.Entry(ventana1, width=50, textvariable=self.horcursHorFin)
        horcursFP.grid(column=3, row=6, padx=10, pady=10)
        
        #########################################

        #CODIGO DEL CURSO
        
        self.codecurs=tk.Label(ventana1, text="INGRESE EL CODIGO DEL CURSO",font=fuente_personalizada)
        self.codecurs.grid(column=0, row=7, padx=0, pady=10)
        
        #CODIGO DEL CURSO INGRESADO
        
        self.codecursI=tk.StringVar()
        codecursP=ttk.Entry(ventana1, width=50, textvariable=self.codecursI)
        codecursP.grid(column=1, row=7, padx=0, pady=10)

        # BOTON PARA GUARDAR CURSO
        
        self.Boton4=tk.Button(ventana1, text="GUARDAR CURSO", font=fuente_titulo, command=lambda: self.COMPROBARCURSO(ventana1))
        self.Boton4.grid(column=1, row=9, padx=5, pady=20, columnspan=2)
        

        #BOTON DE CANCELAR

        self.BotonCursCan = tk.Button(ventana1, text="CANCELAR CURSO", font=fuente_titulo, command=lambda: (self.ADMIN(), ventana1.destroy()))
        self.BotonCursCan.grid(column=0, row=10, padx=5, pady=5)
        self.ventana1.mainloop()

    #FUNCION QUE COMPROBARA ALGUNOS DE LOS DATOS INGRESADOS DEL CURSO
    def COMPROBARCURSO(self, ventana):

        #ASIGNACION DE VARIABLES: 

        nombrecurso = self.NameCursI.get()
        preciocurso = self.precursI.get()
        catedraticocurso = self.catecursI.get()
        cuposcurso = self.cupocursI.get()
        codigocurso = self.codecursI.get()
        FeIn = self.horcursFeIn.get()
        FeFin = self.horcursFeFin.get()
        HorIn = self.horcursHorIn.get()
        HorFin = self.horcursHorFin.get()

        #RUTA DEL LOS ARCHIVOS

        rutauser = "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/CATEDRATICOS/"

        #NOMBRE DEL ARCHIVO A BUSCAR                    

        archiuser = catedraticocurso

        #RUTA COMPLETA QUE SE VA A BUSCAR

        ruta_completa = os.path.join(rutauser, archiuser + ".txt")

        
        try:
            #COMPROBACION DE DATOS EN LAS CELDAS

            if nombrecurso != "" and preciocurso != "" and catedraticocurso != "" and cuposcurso != "" and FeIn != "" and FeFin != "" and HorIn != "" and HorFin != "" and codigocurso != "":
           
            #DETERMINAR SI EL CATEDRATICO EXISTE    
           
                with open(ruta_completa, "r", encoding="utf-8") as archi1:
                    contenido = archi1.readlines()
           
                    #ABRIR ARCHIVO SI ES QUE EXISTE
           
                    with open(ruta_completa, "r", encoding="utf-8") as archi1:
                        contenido = archi1.read()
                        if not re.match(r'^\d+$', preciocurso):
                            mb.showerror("ALERTA", "EL PRECIO NO DEBE LLEVAR LETRAS")
                        else:
           
                            #INDICAR SI EL CATEDRATICO TIENE SUS DATOS
           
                            if contenido.strip() != "":
           
                                #CODIGO DEL CURSO #### SOLO NUMEROS
           
                                if not re.match(r'^\d+$', codigocurso):
                                    mb.showerror("ALERTA", "EL CODIGO NO DEBE LLEVAR LETRAS")
                                elif len(codigocurso) < 4 or len(codigocurso) > 4:
                                    mb.showerror("ALERTA","EL CODIGO NO DEBE SER MAYOR O MENOR 4 NUMEROS")
                                else:
           
                                    #CUPOS DEL CURSO SOLO NUMEROS
           
                                    if not re.match(r'^\d+$', cuposcurso):
                                        mb.showerror("ALERTA", "EL CUPO NO DEBE LLEVAR LETRAS")
                                    else:
    
                                        #LLAMA A LA FUNCION QUE COMPROBARA LA FECHA Y EL HORARIO INGRESADO

                                        self.COMPROBACIONFECHAYHORARIO(ventana)
           
                            #INDICARA QUE NO HAY INFORMACION DEL CATEDRATICO
           
                            else:
                                mb.showerror("ALERTA", "QUERIDO ADMIN EL CATEDRATICO INGRESADO NO EXISTE")
            else: 
                mb.showerror("ALERTA","QUERIDO ADMIN, FALTAN DATOS")
        except FileNotFoundError:
                if catedraticocurso:
                    mb.showerror("ALERTA", "EL CATEDRATICO NO EXISTE")
            
    #FUNCION QUE COMPROBARA LA FECHA Y EL HORARIO INGRESADO
    def COMPROBACIONFECHAYHORARIO(self,ventana):

        #ASIGNACION DE VARIABLES

        FeIn = self.horcursFeIn.get()
        FeFin = self.horcursFeFin.get()
        HorIn = self.horcursHorIn.get()
        HorFin = self.horcursHorFin.get()

        #EXPRESIONES PARA EL FORMATO DE FECHA Y HORA

        fecha_regex = r'\d{2}/\d{2}/\d{4}'
        hora_regex = r'\d{2}:\d{2}'
        hora_invalida = re.match(hora_regex, HorIn)
        hora_fin_invalida = re.match(hora_regex, HorFin)

        #COMPROBACION DE QUE EL FORMATO DE LAS FECHAS INGRESADAS SEA CORRECTO

        if re.match(fecha_regex, FeIn) and re.match(fecha_regex, FeFin):
            

            #COMPROBACION DE QUE EL FORMATO DE LA HORA INGRESADA SEA CORRECTO

            if hora_invalida and hora_fin_invalida:
                # Validación adicional para las horas
                horas_in, minutos_in = map(int, HorIn.split(':'))
                horas_fin, minutos_fin = map(int, HorFin.split(':'))
                
                if 0 <= horas_in <= 24 and 0 <= minutos_in <= 59 and 0 <= horas_fin <= 24 and 0 <= minutos_fin <= 59:
                    self.GUARDARCURSO(ventana)
                
                #ALERTA DEL FORMATO DE HORAS Y MINUTOS

                else:
                    mb.showerror("ALERTA","LA HORA ES INCORRECTO ADMIN, DEBE IR COMO HORA/MINUTOS")
       
            #ALERTA DE FORMATO DE HORA MAL INGRESADA

            else:
                mb.showerror("ALERTA", "LA HORA ES INCORRECTA ADMNIN, DEBE IR COMO ##/##")
       
        #ALERTA DE FECHA MAL INGRESADA
        
        else:
            mb.showerror("ALERTA","LA FECHA ESTA INCORRECTA ADMIN, DEBE IR COMO ##/##/####")

        #HORARIO DEL CURSO EN ##/##/#### AL ##/##/#### DE ##/## AM Ó ##/## PM
        print("HOLA")

    #FUNCION QUE GUARDARA LOS DATOS YA COMPROBADOS
    def GUARDARCURSO(self, ventana):

        #ASIGNACION DE VARIABLES PARA LA ESCRITURA DEL CURSO

        preciocurso = self.precursI.get()
        catedraticocurso = self.catecursI.get()
        cuposcurso = self.cupocursI.get()
        codigocurso = self.codecursI.get()
        FeIn = self.horcursFeIn.get()
        FeFin = self.horcursFeFin.get()
        HorIn = self.horcursHorIn.get()
        HorFin = self.horcursHorFin.get()
        
        #NOMBRE DEL ARCHIVO.txt

        curso = self.NameCursI.get()
        
        #RUTA DEL LOS ARCHIVOS

        rutaCURSO = "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/CURSOS/"

        #VARIABLE DEL ARCHIVO .TXT

        nuevo = os.path.join(rutaCURSO, curso + ".txt")

        #INTENTO DE GUARDADO DE DATOS INGRESADOS

        try:
            #ESCRITURA DE VARIABLES EN EL ARCHIVO
            with open(nuevo, "w", encoding="utf-8") as archi1:
                archi1.write(curso + "\n")
                archi1.write(preciocurso + "\n")
                archi1.write(catedraticocurso + "\n")
                archi1.write(cuposcurso + "\n")
                archi1.write(codigocurso + "\n")
                archi1.write(FeIn + "\n")
                archi1.write(FeFin + "\n")
                archi1.write(HorIn + "\n")
                archi1.write(HorFin + "\n")
                mb.showinfo("CURSO","CURSO GUARDADO")
                self.ADMIN()
                ventana.destroy()
        #INDICACION DE ERROR AL GUARDAR LOS DATOS                   
        except Exception:
            print("NO SE GUARDARON LOS DATOS")
#----------------------------------------------------------------------------------------------------------#--------------------------------------------------------------
    #FUNCION QUE MODIFICARA LOS CURSOS
    def MODCURSS(self,ventana):

        #CIERRE DE VENTANA ANTERIOR 
        ventana.destroy()

        #FUENTES PARA TEXTOS
        style = ttk.Style()
        style.configure('Custom.TButton', font=('Verdana', 15, 'bold'))
        
        #VENTANA
        ventanaMODCURS = tk.Toplevel()
        ventanaMODCURS.wm_state('zoomed')
        ventanaMODCURS.title("EDICION DE MOSAICOS EN SU BASE DE DATOS.txt")

        # MARCO PARA BOTONES
        frameCURSCATE = ttk.Frame(ventanaMODCURS)
        frameCURSCATE.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        #BOTON PARA ACTUALIZAR 
        cargar_buttonCT = ttk.Button(ventanaMODCURS, text="CARGAR CURSOS", command=self.CARGACURS, style='Custom.TButton')
        cargar_buttonCT.grid(row=1, column=0, padx=10, pady=10)

        #VENTANA PARA EDITAR INFORMACION DE CATEDRATICOS
        text_boxCT = ScrolledText(ventanaMODCURS, wrap=tk.WORD, width=100, height=25)
        text_boxCT.grid(row=0, column=1, padx=10, pady=10)

        #BOTON PARA GUARDAR ARCHIVOS
        guardar_buttonCT = ttk.Button(ventanaMODCURS, text="GUARDAR", command=lambda: self.GUARDACURS(ventanaMODCURS), style='Custom.TButton')
        guardar_buttonCT.grid(row=1, column=1, padx=10, pady=10)

        #BOTON PARA CANCELAR ARCHIVOS
        cancelar_buttonCT = ttk.Button(ventanaMODCURS, text="CANCELAR / SALIR", command=lambda: self.CIERRACURS(ventanaMODCURS), style='Custom.TButton')
        cancelar_buttonCT.grid(row=1, column=2, columnspan=2, padx=10, pady=10)

        # VARIABLE PARA EDICION Y LECTURA DE ARCHIVOS
        self.archivo_actualCT = None
        self.text_box = text_boxCT
        self.frame = frameCURSCATE

    #FUNCION QUE ABRE Y MUESTRA LA INFORMACION DEL ARCHIVO/CURSO ELEGIDO
    def ABRECURS(self, archivo):
        global archivo_actualCT
        archivo_actualCT = archivo
        with open(archivo, "r", encoding="utf-8") as file:
            contenido = file.read()
        self.text_box.delete("1.0", "end")
        self.text_box.insert("1.0", contenido)

    #FUNCION PARA GUARDAR ARCHIVOS EDITADOS
    def GUARDACURS(self, ventana):
        if archivo_actualCT:
            contenido = self.text_box.get("1.0", "end")
            with open(archivo_actualCT, "w", encoding="utf-8") as file:
                file.write(contenido)
                ventana.destroy()
                self.ADMIN()

    #FUNCION PARA ENCONTRAR Y MOSTRAR ARCHIVOS DE CURSOS
    def CARGACURS(self):
        #FUENTES PARA TEXTOS
        style = ttk.Style()
        style.configure('Custom.TButton', font=('Verdana', 10, 'bold'))

        #RUTA DE ARCHIVOS PARA NOMBRAR BOTONES
        ruta_archivos = "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/CURSOS/"  
        archivos = [f for f in os.listdir(ruta_archivos) if f.endswith(".txt")]

        #GENERADOR DE BOTONES PARA CADA CURSO
        for archivo in archivos:
            button = ttk.Button(self.frame, text=archivo, style='Custom.TButton', command=lambda a=archivo: self.ABRECURS(os.path.join(ruta_archivos, a)))
            button.grid(sticky="w")

    #FUNCION AL CANCELAR EDICION 
    def CIERRACURS(self, ventana):
        ventana.destroy()
        self.ADMIN()
#----------------------------------------------------------------------------------------------------------#--------------------------------------------------------------
    #FUNCION QUE MODIFICARA LOS MOSAICOS
    def MODMOSA(self,ventana):

        #CIERRE DE VENTANA ANTERIOR 
        ventana.destroy()

        #FUENTES PARA TEXTOS
        style = ttk.Style()
        style.configure('Custom.TButton', font=('Verdana', 15, 'bold'))
        
       #VENTANA
        ventanaMOSA = tk.Toplevel()
        ventanaMOSA.wm_state('zoomed')
        ventanaMOSA.title("EDICION DE MOSAICOS EN SU BASE DE DATOS.txt")

        # MARCO PARA BOTONES
        frameMOSA = ttk.Frame(ventanaMOSA)
        frameMOSA.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        #BOTON PARA ACTUALIZAR 
        cargar_buttonM = ttk.Button(ventanaMOSA, text="CARGAR ARCHIVOS", command=self.CARGAMOS, style='Custom.TButton')
        cargar_buttonM.grid(row=1, column=0, padx=10, pady=10)

        #VENTANA PARA EDITAR INFORMACION DE CATEDRATICOS
        text_boxM = ScrolledText(ventanaMOSA, wrap=tk.WORD, width=100, height=25)
        text_boxM.grid(row=0, column=1, padx=10, pady=10)

        #BOTON PARA GUARDAR ARCHIVOS
        guardar_buttonM = ttk.Button(ventanaMOSA, text="GUARDAR", command=lambda: self.GUARDAMOS(ventanaMOSA), style='Custom.TButton')
        guardar_buttonM.grid(row=1, column=1, padx=10, pady=10)

        #BOTON PARA CANCELAR ARCHIVOS
        cancelar_buttonM = ttk.Button(ventanaMOSA, text="CANCELAR / SALIR", command=lambda: self.CIERRAMOS(ventanaMOSA), style='Custom.TButton')
        cancelar_buttonM.grid(row=1, column=2, columnspan=2, padx=10, pady=10)

        # VARIABLE PARA EDICION Y LECTURA DE ARCHIVOS
        self.archivo_actual = None
        self.text_box = text_boxM
        self.frame = frameMOSA

    #FUNCION QUE ABRE Y MUESTRA LA INFORMACION DEL ARCHIVO ELEGIDO
    def ABREMOS(self, archivo):
        global archivo_actualMOSA
        archivo_actualMOSA = archivo
        with open(archivo, "r", encoding="utf-8") as file:
            contenido = file.read()
        self.text_box.delete("1.0", "end")
        self.text_box.insert("1.0", contenido)

    #FUNCION PARA GUARDAR ARCHIVOS EDITADOS
    def GUARDAMOS(self,ventanaMOSA):
        if archivo_actualMOSA:
            contenido = self.text_box.get("1.0", "end")
            with open(archivo_actualMOSA, "w", encoding="utf-8") as file:
                file.write(contenido)
                ventanaMOSA.destroy()
                self.ADMIN()

    #FUNCION PARA ENCONTRAR Y MOSTRAR ARCHIVOS
    def CARGAMOS(self):
         #FUENTES PARA TEXTOS
        style = ttk.Style()
        style.configure('Custom.TButton', font=('Verdana', 10, 'bold'))

        #RUTA DE ARCHIVOS PARA NOMBRAR BOTONES
        ruta_archivos = "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/MOSAICOS/"  
        archivos = [f for f in os.listdir(ruta_archivos) if f.endswith(".txt")]

        #GENERADOR DE BOTONES PARA CADA MOSAICO
        for archivo in archivos:
            button = ttk.Button(self.frame, text=archivo, style='Custom.TButton', command=lambda a=archivo: self.ABRE(os.path.join(ruta_archivos, a)))
            button.grid(sticky="w")

    #FUNCION AL CANCELAR EDICION 
    def CIERRAMOS(self, ventana):
        ventana.destroy()
        self.ADMIN()
#----------------------------------------------------------------------------------------------------------#--------------------------------------------------------------
    #FUNCION QUE  PIDE LOS DATOS PARA AÑADIR CATEDRATICO
    def AÑADIRCATE(self,ventana):

        #CIERRA VENTANA ANTERIOR
        
        ventana.destroy()
        
        #VENTANA
        
        ventanaCATE = tk.Toplevel()
        
        #TITULO E INFORMACIÓN DE LA VENTANA
        
        ventanaCATE.title("AÑADIR CATEDRATICO")
        color_rgb = (1, 16, 253 ) 
        ventanaCATE.configure(bg="#%02x%02x%02x" % color_rgb)  
        ventanaCATE.wm_state('zoomed')
        
        #FUENTES PARA LOS TEXTOS

        fuente_titulo = tkFont.Font(family="Arial", size=14, weight="bold")
        fuente_personalizada = tkFont.Font(family="Arial", size=10, weight="bold")
        
        #INGRESO DE INFORMACION DEL CATEDRATICO
        #NOMBRE DEL CATEDRATICO
        
        self.NameCa=tk.Label(ventanaCATE, text="INGRESE EL NOMBRE DEL CATEDRATICO",font=fuente_personalizada)
        self.NameCa.grid(column=0, row=0, padx=0, pady=10)
        
        #NOMBRE DEL CATEDRATICO INGRESADO
        
        self.NameCaI=tk.StringVar()
        NameCaP=ttk.Entry(ventanaCATE, width=50, textvariable=self.NameCaI)
        NameCaP.grid(column=0, row=1, padx=0, pady=10)
        
        #APELLIDO DEL CATEDRATICO
        
        self.ApeCA=tk.Label(ventanaCATE, text="INGRESE EL APELLIDO DEL CATEDRATICO",font=fuente_personalizada)
        self.ApeCA.grid(column=0, row=2, padx=0, pady=10)
        
        #APELLIDO DEL CATEDRATICO INGRESADO
        
        self.ApeCAI=tk.StringVar()
        ApeCAP=ttk.Entry(ventanaCATE, width=50, textvariable=self.ApeCAI)
        ApeCAP.grid(column=0, row=3, padx=0, pady=10)
        
        #DPI DEL CATEDRATICO 
        
        self.DPICA=tk.Label(ventanaCATE, text="INGRESE EL DPI DEL CATEDRATICO",font=fuente_personalizada)
        self.DPICA.grid(column=0, row=4, padx=0, pady=10)
        
        #DPI DEL CATEDRATICO INGRESADO
        
        self.DPICAI=tk.StringVar()
        DPICAP=ttk.Entry(ventanaCATE, width=50, textvariable=self.DPICAI)
        DPICAP.grid(column=0, row=5, padx=0, pady=10)

        #CURSO QUE IMPARTIRA EL CATEDRATICO 
        
        self.CURSCA=tk.Label(ventanaCATE, text="INGRESE EL CURSO QUE IMPARTIRA EL CATEDRATICO",font=fuente_personalizada)
        self.CURSCA.grid(column=0, row=6, padx=0, pady=10)
        
        #CURSO QUE IMPARTIRA EL CATEDRATICO INGRESADO
        
        self.CURSCAI=tk.StringVar()
        CURSCAP=ttk.Entry(ventanaCATE, width=50, textvariable=self.CURSCAI)
        CURSCAP.grid(column=0, row=7, padx=0, pady=10)
        
        #CONTRASEÑA DEL CATEDRATICO
        
        self.CONTRACATE=tk.Label(ventanaCATE, text="INGRESE LA CONTRASEÑA DEL CATEDRATICO",font=fuente_personalizada)
        self.CONTRACATE.grid(column=0, row=8, padx=0, pady=10)
        
        #CONTRASEÑA DEL CATEDRATICO INGRESADA
        
        self.CONTRACATEI=tk.StringVar()
        CONTRACATEP=ttk.Entry(ventanaCATE, width=50, textvariable=self.CONTRACATEI, show="*")
        CONTRACATEP.grid(column=0, row=9, padx=0, pady=10)
        
        #CONFIRME SU CONTRASEÑA
        
        self.CONCONTRACATE=tk.Label(ventanaCATE, text="CONFIRME LA CONTRASEÑA DEL CATEDRATICO",font=fuente_titulo)
        self.CONCONTRACATE.grid(column=0, row=10, columnspan=2, padx=0, pady=20)
        
        #CONTRASEÑA DE CONFIRMACION INGRESADA
        
        self.CONCONTRACATEI=tk.StringVar()
        CONCONTRACATEP=ttk.Entry(ventanaCATE, width=50, textvariable=self.CONCONTRACATEI, show="*")
        CONCONTRACATEP.grid(column=0, row=11, padx=10, pady=10)

        #BOTON DE GUARDADO 

        self.BotonCATE=tk.Button(ventanaCATE, text="GUARDAR CATEDRATICO", font=fuente_titulo, command=lambda: self.GUARDARCATEDRATICO(ventanaCATE))
        self.BotonCATE.grid(column=1, row=12, padx=5, pady=20, columnspan=10)

        #BOTON DE CANCELAR

        self.BotonCATECan = tk.Button(ventanaCATE, text="CANCELAR REGISTRO", font=fuente_titulo, command=lambda: (self.ADMIN(), ventanaCATE.destroy()))
        self.BotonCATECan.grid(column=0, row=12, padx=5, pady=20)

    #FUNCION QUE COMPRUEBA LOS DATOS REGISTRADOS
    def GUARDARCATEDRATICO(self, ventana):

        #ASIGNACION DE VARIABLES A LOS DATOS REGISTRADOS

        NameCate = self.NameCaI.get()
        ApelliCate = self.ApeCAI.get()
        DPICate = self.DPICAI.get()
        CursoCate = self.CURSCAI.get()
        ContraCate = self.CONTRACATEI.get()
        ContraCateCon = self.CONCONTRACATEI.get()

        #NOMBRE DEL ARCHIVO.txt

        catedratico = self.NameCaI.get()
        
        #RUTA DEL LOS ARCHIVOS

        rutaCATE = "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/CATEDRATICOS/"

        #VARIABLE DEL ARCHIVO .TXT

        nuevo = os.path.join(rutaCATE, catedratico + ".txt")

        #INTENTO Y COMPROBACION PARA EL GUARDADO DE DATOS INGRESADOS
        
        try: 

            #COMPROBACION DE QUE LAS CELDAS NO ESTEN VACIAS

            if NameCate != "" and ApelliCate != "" and DPICate != "" and ContraCate and ContraCateCon != "" :
                
                # ABRIR ARCHIVO, SI ES QUE ESTE EXISTE
                try:
                    with open(nuevo, "r", encoding="utf-8") as archi1:
                       
                        #ASIGNACION DE LA INFORMACION DEL ARCHIVO A VARIABLE

                        contenido = archi1.read()

                        #DETERMINAR SI EL ARCHIVO CONTIENE INFORMACION

                        if contenido.strip() != "":
                            
                            #ALERTA DE QUE EL CATEDRATICO EXISTE
                            
                            mb.showerror("USUARIO EN USO", "CATEDRATICO EXISTENTE")

                except Exception:

                            #COMPROBACION DE DPI POR SI TIENE LETRAS O MAS DIGITOS 

                            if not re.match(r'^\d+$', DPICate):
                                mb.showerror("ALERTA", "El NUMERO DE DPI NO LLEVA LETRAS")
                            elif len(DPICate) < 13 or len(DPICate) > 13:
                                mb.showerror("ALERTA", "EL NUMERO DPI SOLO LLEVA 13 DIGITOS")
                            else:

                                #COMPROBACION DE QUE LAS CONTRASEÑAS SEAN IGUALES

                                if ContraCate == ContraCateCon:

                                    #VALIDAR FORMATO DE CONTRASEÑA

                                    if self.validar_contrasena2(ContraCate):

                                        #CREACION DEL ARCHIVO PARA ESCRITURA DE DATOS

                                        with open(nuevo, "w", encoding="utf-8") as archi2:

                                            #ENCRIPTACION DE LA CONTRASEÑA    

                                            Encrip = hashlib.sha256(ContraCateCon.encode()).hexdigest()

                                            #ESCRITURA DE DATOS EN EL ARCHIVO

                                            archi2.write(NameCate + "\n")
                                            archi2.write(ApelliCate + "\n")
                                            archi2.write(DPICate + "\n")
                                            archi2.write(CursoCate + "\n")
                                            archi2.write(Encrip + "\n")

                                            #DATOS GUARDADOS CON EXITO

                                            mb.showinfo("EXITO","DATOS DEL CATEDRATICO ALMECENADOS")

                                            #LLAMA A LA FUNCION ADMIN Y CIERRA LA VENTANA

                                            self.ADMIN()
                                            ventana.destroy()
                                    else:
                                        mb.showerror("ALERTA", "LA CONTRASEÑA DEBE TENER NUMEROS, LETRAS Y UN CARACTER")

                                #ALERTA DE CONTRASEÑAS AL NO SER IGUALES        

                                else:
                                    mb.showerror("ALERTA","CONTRASEÑAS NO SON IGUALES")

            #ALERTA DE CELDAS VACIAS

            else:
                mb.showerror("ALERTA","FALTAN DATOS ADMIN")
        
        #ALERTO POR SI NO GUARDA LA INFO DEL CATEDRATICO
        
        except Exception:
            mb.showerror("ALERTA","NO FUE GUARDADO EL CATEDRATICO")

    #FUNCION PARA COMPROBAR FORMATO DE CONTRASEÑAS
    def validar_contrasena2(self, ContraCateCon):
        # Utiliza una expresión regular para verificar la contraseña
        patron = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@#$%^&+=]).{8}$")
        return patron.match(ContraCateCon) is not None
#----------------------------------------------------------------------------------------------------------#--------------------------------------------------------------
    #VENTANA DONDE MUESTRA LOS CATEDRATICOS, SUS DATOS, Y SU RESPECTIVA MODIFICACION O ELIMINACION 
    def CATEDRATIC(self,ventana):
        #CIERRE DE VENTANA ANTERIOR 
        ventana.destroy()

        #FUENTES PARA TEXTOS
        style = ttk.Style()
        style.configure('Custom.TButton', font=('Verdana', 10, 'bold'))
        
       #VENTANA
        ventanaCATE = tk.Toplevel()
        ventanaCATE.wm_state('zoomed')
        ventanaCATE.title("EDICION CATEDRATICOS EN SU BASE DE DATOS.txt")

        # MARCO PARA BOTONES
        frame = ttk.Frame(ventanaCATE)
        frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        #BOTON PARA ACTUALIZAR 
        cargar_button = ttk.Button(ventanaCATE, text="CARGAR ARCHIVOS", command=self.CARGA, style='Custom.TButton')
        cargar_button.grid(row=1, column=0, padx=10, pady=10)

        #VENTANA PARA EDITAR INFORMACION DE CATEDRATICOS
        text_box = ScrolledText(ventanaCATE, wrap=tk.WORD, width=100, height=25)
        text_box.grid(row=0, column=1, padx=10, pady=10)

        #BOTON PARA GUARDAR ARCHIVOS
        guardar_button = ttk.Button(ventanaCATE, text="GUARDAR", command=lambda: self.GUARDA(ventanaCATE), style='Custom.TButton')
        guardar_button.grid(row=1, column=1, padx=10, pady=10)

        #BOTON PARA CANCELAR 
        cancelar_button = ttk.Button(ventanaCATE, text="CANCELAR / SALIR", command=lambda: self.CIERRA(ventanaCATE))
        cancelar_button.grid(row=1, column=2, columnspan=2, padx=10, pady=10)

        #CONTRASEÑA PARA ENCRIPTAR
        etiqueta_contraseña = tk.Label(ventanaCATE, text='INGRESE LA CONTRASEÑA:')
        etiqueta_contraseña.grid(row=2, column=1, padx=10, pady=10)

        #CELDA PARA INGRESAR CONTRASEÑA
        self.entrada_contraseña = tk.Entry(ventanaCATE)
        self.entrada_contraseña.grid(row=3, column=1, padx=10, pady=10)

        #BOTON PARA GENERAR CONTRASEÑA ENCRIPTADA
        boton_encriptar = ttk.Button(ventanaCATE, text='GENERAR CONTRASEÑA ENCRIPTADA', command=self.ENCRIPCONTRA)
        boton_encriptar.grid(row=4, column=1, padx=10, pady=10)

        #CELDA PARA MOSTRAR LA CONTRASEÑA ENCRIPTADA
        self.resultado_text = tk.Text(ventanaCATE, height=1, width=65)
        self.resultado_text.grid(row=5, column=1, padx=10, pady=10)

        #BOTON PARA COPIAR LA CONTRASEÑA
        boton_copiar = ttk.Button(ventanaCATE, text='COPIAR CONTRASEÑA ENCRIPTADA', command=lambda: self.COPIACONTRA(ventanaCATE))
        boton_copiar.grid(row=6, column=1, padx=10, pady=10)


    # VARIABLE PARA EDICION Y LECTURA DE ARCHIVOS
        self.archivo_actual = None
        self.text_box = text_box
        self.frame = frame

    #FUNCION QUE ABRE Y MUESTRA LA INFORMACION DEL ARCHIVO ELEGIDO
    def ABRE(self, archivo):
        global archivo_actual
        archivo_actual = archivo
        with open(archivo, "r", encoding="utf-8") as file:
            contenido = file.read()
        self.text_box.delete("1.0", "end")
        self.text_box.insert("1.0", contenido)

    #FUNCION PARA GUARDAR ARCHIVOS EDITADOS
    def GUARDA(self,ventanaCATE):
        if archivo_actual:
            contenido = self.text_box.get("1.0", "end")
            with open(archivo_actual, "w", encoding="utf-8") as file:
                file.write(contenido)
                ventanaCATE.destroy()
                self.ADMIN()

    #FUNCION PARA ENCONTRAR Y MOSTRAR ARCHIVOS
    def CARGA(self):
         #FUENTES PARA TEXTOS
        style = ttk.Style()
        style.configure('Custom.TButton', font=('Verdana', 10, 'bold'))

        #RUTA DE ARCHIVOS PARA NOMBRAR BOTONES
        ruta_archivos = "C:/Users/Miguel Choc/Desktop/Proyecto USAC/REGISTROS DE LA ACADEMIA/CATEDRATICOS/"  
        archivos = [f for f in os.listdir(ruta_archivos) if f.endswith(".txt")]

        #GENERADOR DE BOTONES PARA CADA CATEDRATICO
        for archivo in archivos:
            button = ttk.Button(self.frame, text=archivo, style='Custom.TButton', command=lambda a=archivo: self.ABRE(os.path.join(ruta_archivos, a)))
            button.grid(sticky="w")

    #FUNCION AL CANCELAR EDICION 
    def CIERRA(self, ventanaCATE):
        ventanaCATE.destroy()
        self.ADMIN()

    #FUNCION PARA HACER UNA NUEVA CONTRASEÑA
    def ENCRIPCONTRA(self):
        contraseña = self.entrada_contraseña.get()
        if contraseña:
            encriptada = hashlib.sha256(contraseña.encode()).hexdigest()
            self.resultado_text.delete("1.0", "end") 
            self.resultado_text.insert("1.0", encriptada) 
        else:
            mb.showinfo("ERROR", "CELDA VACIA")

    #FUNCION PARA COPIAR TEXTO
    def COPIACONTRA(self,ventanaCATE):
        encriptada = self.resultado_text.get("1.0", "end-1c") 
        ventanaCATE.clipboard_clear()  
        ventanaCATE.clipboard_append(encriptada)  
        mb.showinfo("INFO","CONTRASEÑA COPIADA")
        ventanaCATE.update()  
#----------------------------------------------------------------------------------------------------------#--------------------------------------------------------------

#BLOQUE MADRE
ACADEMIAUSAC =ACADEMIA()