"""
Made By Rayr
      ___           ___           ___           ___     
     /\  \         /\  \         |\__\         /\  \    
    /::\  \       /::\  \        |:|  |       /::\  \   
   /:/\:\  \     /:/\:\  \       |:|  |      /:/\:\  \  
  /::\~\:\  \   /::\~\:\  \      |:|__|__   /::\~\:\  \ 
 /:/\:\ \:\__\ /:/\:\ \:\__\     /::::\__\ /:/\:\ \:\__\
 \/_|::\/:/  / \/__\:\/:/  /    /:/~~/~    \/_|::\/:/  /
    |:|::/  /       \::/  /    /:/  /         |:|::/  / 
    |:|\/__/        /:/  /     \/__/          |:|\/__/  
    |:|  |         /:/  /                     |:|  |    
     \|__|         \/__/                       \|__|    
"""
import os
import time
import termcolor
import colorama
colorama.init()
from win32gui import GetWindowText, GetForegroundWindow
print('Waiting... 5 seconds ', end='')
print(termcolor.colored('Please click on Discord', 'green',))
time.sleep(5)
os.system('cls')
print(' ')
print(' ')
print('Focused Window:')
print(' ')
x = (GetWindowText(GetForegroundWindow()))
print('          ' + termcolor.colored(x, 'grey', 'on_white'))
print(' ')
print('     ' + termcolor.colored('↑ Paste this if the script asks for the window name ↑', 'blue',))
