#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------------
# Zip Cracker - v 1.0.0
#-----------------------------------------------------------------------------------
#
# Simple script para crackear la contraseña de un archivo .zip con un diccionario
#
# Bajo licencia GPL v3 (http://www.gnu.org/licenses/gpl-3.0.html)
#
# Desarrollado por Fabio Escudero
# Feb 2017
# Última versión en https://github.com/fabioescudero/python
#

#-----------------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------------
from time import time
import zipfile
import argparse
import sys
import os


#-----------------------------------------------------------------------------------
# Ayuda de uso del programa
#-----------------------------------------------------------------------------------
def ayuda_uso():
    prog = os.path.basename (sys.argv[0])

    print u'''
    Uso: {} -a archivo -d diccionario
    
    Ejemplo: 
        {} -a sample.zip -d rockyou.txt
    '''.format (prog, prog)

#-----------------------------------------------------------------------------------
# Definición de funciones
#-----------------------------------------------------------------------------------
def muestra_duracion (inicio, contador):
    duracion = time() - inicio
    print u"\nTiempo empleado: {:0.4f} segundos.".format (duracion)
    print u"Se procesaron {:.0f} claves por segundo".format (contador/(time() - inicio))

#-----------------------------------------------------------------------------------
# Código principal
#-----------------------------------------------------------------------------------
def main():
    #--------------------------------------------------
    # Presentacion
    print u'''
     ___________ _____     _____                _             
    |___  /_   _|  __ \   / ____|              | |            
       / /  | | | |__) | | |     _ __ __ _  ___| | _____ _ __ 
      / /   | | |  ___/  | |    | '__/ _` |/ __| |/ / _ \ '__|
     / /__ _| |_| |      | |____| | | (_| | (__|   <  __/ |   
    /_____|_____|_|       \_____|_|  \__,_|\___|_|\_\___|_|   

    '''

    #--------------------------------------------------
    # Recupera los parametros
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument ("-a", type=str, nargs='?')
    parser.add_argument ("-d", type=str, nargs='?')

    args = parser.parse_args()

    if (args.a is None or args.d is None):
        ayuda_uso()
        exit()

    archivo = args.a
    diccionario = args.d

    try:
        archivo_zip = zipfile.ZipFile (archivo, "r")
    except:
        print u"Error. No se pudo abrir el archivo '{}'".format(archivo)
        exit()

    try:
        lista_pass = open(diccionario, "r").readlines()
    except:
        print u"Error. No se pudo abrir el archivo '{}'".format(diccionario)
        exit()

    #--------------------------------------------------
    # Código principal
    try:
        print u"[+] Se cargaron {:d} contraseñas del diccionario {}".format (len (lista_pass), diccionario)
        print u"[+] Verificando, espere por favor...\n"

        inicio = time()
        contador = 0
        for password in lista_pass:
            try:
                contador += 1
                password = password.replace("\r","").replace("\n","")
                archivo_zip.extractall (pwd=password)
                print u"[+] Password encontrado: {}.".format (password)
                muestra_duracion (inicio, contador)
                exit()

            except Exception, e:
                pass

        print u"[+] No se pudo encontrar el password buscado\n"
        muestra_duracion (inicio, contador)

    except Exception, e:
        print e
        exit()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print u"[+] Búsqueda interrumpida por el usuario..."
    except:
        exit()
