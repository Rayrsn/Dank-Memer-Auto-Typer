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
#from win32gui import GetWindowText, GetForegroundWindow
#linux dependencies
import gi
gi.require_version("Wnck", "3.0")
from gi.repository import Wnck

print('Waiting... 5 seconds ', end='')
print(termcolor.colored('Please click on Discord', 'green',))
time.sleep(5)
os.system('clear')
print(' ')
print(' ')
print('Focused Window:')
print(' ')
#x = (GetWindowText(GetForegroundWindow()))
scr = Wnck.Screen.get_default()
scr.force_update()
x = (scr.get_active_window().get_name())
print('          ' + termcolor.colored(x, 'grey', 'on_white'))
print(' ')
print('     ' + termcolor.colored('↑ Paste this if the script asks for the window name ↑', 'blue',))
