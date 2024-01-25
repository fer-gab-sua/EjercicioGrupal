""" MODULO ENCARGADO DE LANZAR LA APLICACION
"""

from tkinter import Tk
from vista import VentanaPrincipal

__author__ = "Fernando Suarez, Damian Colomb"
__mainteinter__ = "Fernando Suarez, Damian Colomb"
__email__ = "fer.gab.sua@gmail.com , colomb.damian@gmail.com"
__copyrigth__ = "Copyright 2023"
__version__ = "0.1"

if __name__ == "__main__":
    root_tk = Tk()
    VentanaPrincipal(root_tk)
    root_tk.mainloop()