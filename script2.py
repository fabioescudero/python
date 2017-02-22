#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------------
# Licencia
#-----------------------------------------------------------------------------------
#
# script2.py - v 1.0.0
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
import argparse
import sys
import os


#-----------------------------------------------------------------------------------
# Constantes
#-----------------------------------------------------------------------------------
MD5  = "md5"
SHA1 = "sha1"


#-----------------------------------------------------------------------------------
# Ayuda de uso del programa
#-----------------------------------------------------------------------------------
def ayuda_uso():
    prog = os.path.basename (sys.argv[0])

    print u'''
    Uso: %s -a parámetro1 -b parámetro2
    
    Ejemplo: 
        %s -a 2 -b 5
    ''' % ((prog,) * 2)


#-----------------------------------------------------------------------------------
# Definición de funciones
#-----------------------------------------------------------------------------------
def sumar (valor1, valor2):
    resultado = valor1 + valor2
    return resultado
        

#-----------------------------------------------------------------------------------
# Código principal
#-----------------------------------------------------------------------------------
def main():
    try:
        #--------------------------------------------------
        # Recupera los parametros
        parser = argparse.ArgumentParser()
        parser.add_argument ("-a", nargs='?')
        parser.add_argument ("-b", nargs='?')

        args = parser.parse_args()

        param1 = float (args.a)
        param2 = float (args.b)


        #--------------------------------------------------
        # Código principal
        print "Resultado: %s" % str (sumar (param1, param2))


    except:
        ayuda_uso()
        exit (1)


if __name__ == "__main__":
    main ()