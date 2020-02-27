import os

hostname="www.itmorelia.edu.mx"

respuesta=os.system("ping -c 1 "+hostname)

if respuesta==0:
    print (hostname+": esta en funcionamiento!")
else:
    print (hostname+": No funciona")

red="200.33.171.0/24"

os.system("nmap -sP "+red)

"""C:\Users\franciscojavier>C:/Users/franciscojavier/AppData/Local/Programs/Python/Python38-32/python.exe "c:/Users/franciscojavier/Downloads/Cuarto Semestre/Topicos Avanzados de Programacion/Codigos/Practica 2.py"
Acceso denegado. La opción -c requiere privilegios administrativos.
www.itmorelia.edu.mx: No funciona"""