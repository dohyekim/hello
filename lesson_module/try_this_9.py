import os

def clear_screen():
    if os.name == "nt": #"nt" = window
        os.system('cls')
    else: 
        os.system("clear")
