def saludo(nombre):  #defino la funcion del saludo
    print(f"hola " + nombre)
import time  #importo libreria tiempo

nombre = input("ingrese su nombre: ")  #programa principal
time.sleep(1)

saludo(nombre)  #llamo a la funcion luego de solicitar el nombre al usuario