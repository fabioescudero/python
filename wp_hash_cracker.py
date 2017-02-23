#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------------
# WordPress Hash Cracker - v 1.0.0
#-----------------------------------------------------------------------------------
#
# Simple script para crackear un hash de WordPress (utilizado para almacenar las 
# contraseñas) contra un diccionario
# Es necesario tener instalada la libreria passlib (https://pypi.python.org/pypi/passlib)
# En internet hay varios diccionarios para utilizar (https://wiki.skullsecurity.org/Passwords)
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
import argparse
import sys
import os

try:
    from passlib.hash import phpass
except:
    print u"\nPara ejecutar este script se necesita la librería passlib (https://pypi.python.org/pypi/passlib)\n"
    exit()

#-----------------------------------------------------------------------------------
# Ayuda de uso del programa
#-----------------------------------------------------------------------------------
def ayuda_uso():
    prog = os.path.basename (sys.argv[0])

    print u'''
    Uso: {} -h hash -d diccionario
    
    Ejemplo: 
        {} -h '$P$HeH0TFBXisquuirb5dWFx46/EduIeD/' -d rockyou.txt
    '''.format (prog, prog)

#-----------------------------------------------------------------------------------
# Definición de funciones
#-----------------------------------------------------------------------------------
def muestra_duracion (inicio):
    duracion = time() - inicio
    print u"Tiempo empleado: {:0.4f} segundos.".format (duracion)


#-----------------------------------------------------------------------------------
# Código principal
#-----------------------------------------------------------------------------------
def main():
    #--------------------------------------------------
    # Recupera los parametros
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument ("-h", type=str, nargs='?')
    parser.add_argument ("-d", type=str, nargs='?')

    args = parser.parse_args()

    if (args.h is None or args.d is None):
        ayuda_uso()
        exit()

    dicc = args.d
    hash = args.h.replace ("'", "")

    #--------------------------------------------------
    # Presentacion
    print u'''
     _    _           _        _____                _             
    | |  | |         | |      / ____|              | |            
    | |__| | __ _ ___| |__   | |     _ __ __ _  ___| | _____ _ __ 
    |  __  |/ _` / __| '_ \  | |    | '__/ _` |/ __| |/ / _ \ '__|
    | |  | | (_| \__ \ | | | | |____| | | (_| | (__|   <  __/ |   
    |_|  |_|\__,_|___/_| |_|  \_____|_|  \__,_|\___|_|\_\___|_|   
                                                              
    '''

    #--------------------------------------------------
    # Código principal
    try:
        lista_pass = open(dicc).readlines()
        print u"[+] Se cargaron {:d} contraseñas del diccionario {}".format (len (lista_pass), dicc)
        print u"[+] Verificando, espere por favor...\n"

        inicio = time()

        for password in lista_pass:
            if (phpass.verify (password.rstrip(), hash)):
                print u"[+] Password encontrado: {}".format (password)
                muestra_duracion (inicio)
                exit()

        print u"[+] No se pudo encontrar el password buscado\n"
        muestra_duracion (inicio)

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
