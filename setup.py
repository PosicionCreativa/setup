#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# -*- coding: utf-8 -*-

import os
import json
import urllib

# Definición de colores
class color:
    purple  = '\033[95m'
    blue    = '\033[94m'
    green   = '\033[92m'
    yellow  = '\033[93m'
    red     = '\033[91m'
    end     = '\033[0m'
    # Efectos en el texto (bold y underline)
    bold    = '\033[1m'
    under   = '\033[4m'

print(color.yellow)
print("***********************************************")
print(" ****** Bienvenido al instalador de MAC ****** ")
print("***********************************************")
print(color.end)

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

# Definición de preguntas
questions = {
    'name': color.green + "Cual es tu nombre?" + color.end + "\n> ",
    'email': {
        'default': color.green + "Cual es tu email? " + color.end + "\n> ",
        'invalid': color.red + "(escribe un email valido) " + color.end + "\n> "
    },
    'developer': {
        'default': color.green + "Quieres instalar los Developer Tools? (%s) " + color.end,
        'android': color.green + "Quieres instalar Android Tools? (%s) " + color.end,
        'ios'    : color.green + "Quieres instalar los IOS Tools? (%s) " + color.end,
    },
    'designer': color.green + "Quieres instalar las herramientas para diseño? (%s) " + color.end,
    'sublime' : color.green + "Quieres instalar Sublime Text 3 con algunos plugins? (%s) " + color.end,
    'zsh': color.green + "Quieres insalar Oh My Zsh? (%s) " + color.end,
    'animations': color.green + "Quieres acelerar las animaciones en OSX? (%s) " + color.end,
    'show_files': color.green + "Quieres que se muestren los archivos ocultos? (%s) " + color.end,
    'autoupdate': color.green + "Necesitas que el Sistema se actualice (%s) " + color.green
}

# Solicitud de Información Básica
# - Nombre
# - Correo electronico
while name == '':
    name = raw_input(questions['name']).strip()

count = 0
while email == '' or '@' not in email:
    if count == 0:
        email = raw_input(questions['email']['default']).strip()
    elif count > 0:
        email = raw_input(questions['email']['invalid']).strip()
    count = count + 1

# Opciones de instalación
while options['developer'] not in ['y', 'n']:
  options['developer'] = raw_input(questions['developer']['default'] % '|'.join(['y','n']))

# Herramientas para developers
if options['developer'] == 'y':
    # Developer tools para Android
    while options['android'] not in ['y', 'n']:
        options['android'] = raw_input(questions['developer']['android'] % '|'.join(['y','n']))
    # Developer tools para Ios
    while options['ios'] not in ['y', 'n']:
        options['ios'] = raw_input(questions['developer']['ios'] % '|'.join(['y','n']))

# Herramientas para diseñador
while options['designer'] not in ['y', 'n']:
    options['designer'] = raw_input(questions['designer'] % '|'.join(['y','n']))

# Sublime Text 3
while options['sublime'] not in ['y', 'n']:
    options['sublime'] = raw_input(questions['sublime'] % '|'.join(['y','n']))

# Oh My ZSH
while options['zsh'] not in ['y', 'n']:
    options['zsh'] = raw_input(questions['zsh'] % '|'.join(['y','n']))

# Animaciones de OSX
while options['animations'] not in ['y', 'n']:
    options['animations'] = raw_input(questions['animations'] % '|'.join(['y','n']))

# Mostrar los archivos ocultos en el finder
while options['show_files'] not in ['y', 'n']:
    options['show_files'] = raw_input(questions['show_files'] % '|'.join(['y','n']))

# Auto-Update (opción recomendada)
while options['autoupdate'] not in ['y', 'n']:
    options['autoupdate'] = raw_input(questions['autoupdate'] % '|'.join(['y','n']))


print("\n\n")
print(color.yellow)
print("***********************************************************")
print("Hola, %s!" % name)
print("***********************************************************")
print("En este proceso te preguntaremos la contraseña varias veces")
print("***********************************************************")
print("Iniciaremos el proceso de instalación :)...")
print("***********************************************************")
print(color.end)

# Crearemos un public key
if not os.path.isfile(os.path.expanduser("~") + '/.ssh/id_rsa.pub'):
    print("*************************************************************")
    print("Estamos creando una llave publica con el correo proporcionado")
    print("*************************************************************")
    os.system('ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N "" -C "%s"' % email)

# Colocando el nombre como el hostname en la PC (esto lo puedes hacer via System Preferences -> Sharing)
os.system('sudo scutil --set ComputerName "%s"' % name)
os.system('sudo scutil --set HostName "%s"' % name)
os.system('sudo scutil --set LocalHostName "%s"' % name)
os.system('sudo defaults write /Library/Preferences/SystemConfiguration/com.apple.smb.server NetBIOSName -string "%s"' % name)


# Verificamos que xcode cli este instalado, sino lo instalamos :)
if os.system('xcode-select -p') != 0:
    print("**********************")
    print("Instalando Xcode Tools")
    print("**********************")
    os.system('xcode-select --install')
    print("******************************")
    print("Reinicia tu MAC para continuar")
    print("******************************")
    exit()

# Instalando Homebrew y Homebrew Cask
print("***********************************")
print("Instalando Homebrew & Homebrew Cask")
print("***********************************")
os.system('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
os.system('brew tap caskroom/cask')
os.system('brew tap homebrew/services')
os.system('brew tap caskroom/versions')
os.system('brew tap caskroom/fonts')
os.system('brew tap homebrew/versions')
os.system('brew update && brew upgrade && brew cleanup && brew cask cleanup')

# Instalamos Git, GitFlow, Nodejs, Python y Ruby (RoR soon)
print("**********************************************")
print("Instalando Git, GitFlow, Nodejs, Python y Ruby")
print("**********************************************")
os.system('brew install git node python python3 ruby')
os.system('brew link --overwrite git node python python3 ruby')
os.system('brew install git-flow')

# Instalamos algunas herramientas cli utiles
print("***************************************")
print("Instalando curl, wget, sqlite y openssl")
print("***************************************")
os.system('brew install graphicsmagick curl wget sqlite libpng libxml2 openssl')

# Instalando los Command Line Tools
print("*********************************")
print("Instalando los Command Line Tools")
print("*********************************")
os.system('npm install -g yo bower gulp grunt grunt-cli node-gyp nvm')