#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------------
# Licencia
#-----------------------------------------------------------------------------------
#
# script.py - v 1.0.0
#
# Este script está bajo licencia GPL v3 (http://www.gnu.org/licenses/gpl-3.0.html)
#
# Desarrollado por Fabio Escudero
# Fecha: 21-02-2017
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
    Uso: %s valor1 valor2
    
    Ejemplo: 
        %s 2 5
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
        parser.add_argument (dest="param1", nargs='?')
        parser.add_argument (dest="param2", nargs='?')

        args = parser.parse_args()

        param1 = float (args.param1)
        param2 = float (args.param2)


        #--------------------------------------------------
        # Código principal
        print "Resultado: %s" % str (sumar (param1, param2))


    except:
        ayuda_uso()
        exit (1)


if __name__ == "__main__":
    main ()