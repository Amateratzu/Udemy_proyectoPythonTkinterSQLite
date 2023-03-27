import tkinter as tk
from client.gui_app import Frame, barra_menu

def main():
    root = tk.Tk()
    root.title('Catálogo de películas')
    root.iconbitmap('img/cp-logo.ico')
    root.resizable(0,0) #Para habilitar y deshabilitar el maximizar y minimizar la ventana
    barra_menu(root)

    app = Frame(root=root)
    
    app.mainloop()

if __name__ == '__main__':
    main()