#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# -*- coding: utf-8 -*-

import os
import json
import urllib

print("***********************************************")
print(" ****** Bienvenido al instalador de MAC ****** ")
print("***********************************************")

name    = ''
email   = ''
options = {
    'developer':    '',
    'android':      '',
    'ios':          '',
    'designer':     '',
    'sublime':      '',
    'zsh':          '',
    'animations':   '',
    'show_files':   '',
    'autoupdate':   ''
}

# Información Básica
# - Nombre
# - Correo electronico
while name == '':
    name = input("Cual es tu nombre?\n> ").strip()

count = 0
while email == '' or '@' not in email:
    if count == 0:
        email = input("Cual es tu email?\n").strip()
    elif count > 0:
        email = input("Cual es tu email? (escribe un email valido)\n").strip()
    count = count + 1

# Opciones de instalación
while options['developer'] not in ['y', 'n']:
  options['developer'] = input("Quieres instalar los Developer Tools? (%s)  " % '|'.join(['y','n']))

# Herramientas para developers
if options['developer'] == 'y':
    # Developer tools para Android
    while options['android'] not in ['y', 'n']:
        options['android'] = input("Quieres instalar Android Tools? (%s)  " % '|'.join(['y','n']))
    # Developer tools para Ios
    while options['ios'] not in ['y', 'n']:
        options['ios'] = input("Quieres instalar los IOS Tools? (%s)  " % '|'.join(['y','n']))

# Herramientas para diseñador
while options['designer'] not in ['y', 'n']:
    options['designer'] = input("Quieres instalar las herramientas para diseño? (%s)  " % '|'.join(['y','n']))

# Sublime Text 3
while options['sublime'] not in ['y', 'n']:
    options['sublime'] = input("Quieres instalar Sublime Text 3 con algunos plugins? (%s)  " % '|'.join(['y','n']))

# Oh My ZSH
while options['zsh'] not in ['y', 'n']:
    options['zsh'] = input("Quieres insalar Oh My Zsh? (%s)  " % '|'.join(['y','n']))

# Animaciones de OSX
while options['animations'] not in ['y', 'n']:
    options['animations'] = input("Quieres acelerar las animaciones en OSX? (%s)  " % '|'.join(['y','n']))

# Mostrar los archivos ocultos en el finder
while options['show_files'] not in ['y', 'n']:
    options['show_files'] = input("Quieres que se muestren los archivos ocultos? (%s)  " % '|'.join(['y','n']))

# Auto-Update (opción recomendada)
while options['autoupdate'] not in ['y', 'n']:
    options['autoupdate'] = input("Necesitas que el Sistema Operativo se actualice automáticamente? (Recomendado) (%s)  " % '|'.join(['y','n']))

print("\n\n")
print("***********************************************************")
print("Hola, %s!" % name)
print("***********************************************************")
print("En este proceso te preguntaremos la contraseña varias veces")
print("***********************************************************")
print("Iniciaremos el proceso de instalación :)...")
print("***********************************************************")

# Crearemos un private key
if not os.path.isfile(os.path.expanduser("~") + '/.ssh/id_rsa.pub'):
    print("Estamos creando una llave privada con el correo proporcionado")
    print("*************************************************************")
    os.system('ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N "" -C "%s"' % email)

# Colocando el nombre como el hostname en la PC (esto lo puedes hacer via System Preferences -> Sharing)
os.system('sudo scutil --set ComputerName "%s"' % name)
os.system('sudo scutil --set HostName "%s"' % name)
os.system('sudo scutil --set LocalHostName "%s"' % name)
os.system('sudo defaults write /Library/Preferences/SystemConfiguration/com.apple.smb.server NetBIOSName -string "%s"' % name)


# Check if Xcode Command Line Tools are installed
if os.system('xcode-select -p') != 0:
    print("Instalando Xcode Tools")
    os.system('xcode-select --install')
    print("******************************")
    print("Reinicia tu MAC para continuar")
    print("******************************")
    exit()