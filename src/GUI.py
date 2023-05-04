from customtkinter import *
from PIL import ImageTk, Image
from numpy import loadtxt
from customtkinter import ctk

class Window(CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # variables creadas para centrar la ventana al iniciar el programa
        self.wtotal = self.winfo_screenwidth()
        self.htotal = self.winfo_screenheight()
        self.wventana = 680
        self.hventana = 600
        self.pwidth = round(self.wtotal/2-self.wventana/2)
        self.pheight = round(self.htotal/2-self.hventana/2)
        self.geometry(
            str(self.wventana)+"x"+str(self.hventana)+
            "+"+str(self.pwidth)+"+"+str(self.pheight-50))
        self.title('Pinocchio - Artificial intelligence')
        self.resizable(0,0)
        # componentes agregados
        self.disHorinzButt = 20
        
        self.tabView()
        self.optionMenus()
        self.labels()
        self.buttons()
        self.switchs()
        #self.images() # será inicializado cuando se elija el mapa

    def labels(self):
        label = CTkLabel(
            master=self, text="Maps", fg_color="transparent",
            width=80, height=30, font=('Comic Sans MS', 20))
        label.place(x=40,y=480)

    def buttons(self):
        def funcion_button_BFS():
            print("button BFS pressed")
        def funcion_button_UCS():
            print("button UCS pressed")
        def funcion_button_IDFS():
            print("button IDFS pressed")
        def funcion_button_steps():
            print("button steps pressed")
        
        global button_BFS, button_IDFS, button_UCS, button_Steps
        # Se crean como globas para hacer alternar el estado del boton
        button_BFS = CTkButton(
            master=self, text="BFS", command=funcion_button_BFS,
            width=120, height=50, border_width=0, state='disabled',
            text_color_disabled='white', corner_radius=8, 
            font=('Comic Sans MS', 23))
        button_BFS.place(x=self.disHorinzButt, y=80)

        button_IDFS = CTkButton(
            master=self, text="IDFS", command=funcion_button_IDFS,
            width=120, height=50, border_width=0, state='disabled',
            text_color_disabled='white', corner_radius=8,
            font=('Comic Sans MS', 23))
        button_IDFS.place(x=self.disHorinzButt, y=160)

        button_UCS = CTkButton(
            master=self, text="UCS", command=funcion_button_UCS,
            width=120, height=50, border_width=0, state='disabled',
            text_color_disabled='white', corner_radius=8, 
            font=('Comic Sans MS', 23))
        button_UCS.place(x=self.disHorinzButt, y=240)

        button_Steps = CTkButton(
            master=self, text="NextStep", command=funcion_button_steps,
            width=120, height=50, border_width=0, state='disabled',
            text_color_disabled='white', corner_radius=8,
            font=('Comic Sans MS', 20))
        button_Steps.place(x=self.disHorinzButt, y=410)

    def switchs(self):
        def switch_event():
            print("switch toggled, current value:", switch_var.get()) 
            # imprime lo que haya en la variable switch_var
        switch_var = StringVar(value="on") # se inicializa su valor en 'on'
        switch = CTkSwitch(
            master=self, text="Evitar\nDevolverse",
            command=switch_event, variable=switch_var,
            onvalue="Con farmac-On!! >:D", offvalue="sin farmacon :c",
            width=120,height=50, font=('Comic Sans MS', 18))
        # Se obtienen dos resultados, cuando se activa y cuando se desactiva
        switch.place(x=self.disHorinzButt, y=330)

    def optionMenus(self):
        global optionmenu
        
        def optionmenu_callback(choice):
            print("optionmenu dropdown clicked:", choice)
            self.reader()
            self.activateButton(button_BFS)
            self.activateButton(button_IDFS)
            self.activateButton(button_UCS)
            self.activateButton(button_Steps)
            
            self.images() # se llama la función que enseña las imagenes (el mapa)

        optionmenu = CTkOptionMenu(
            master=self, values=["map01", "map02", "map03"],
            command=optionmenu_callback, width=120, height=50)
        optionmenu.set("Maps")
        optionmenu.place(x=self.disHorinzButt, y=510)

    def images(self):
        img_mindWall = ImageTk.PhotoImage(
            Image.open('img/MindWall.png'))  # bloqueo-> 0
        img_Smoking = ImageTk.PhotoImage(
            Image.open('img/Smoking.png'))  # cigarrillos-> 2
        img_Fox = ImageTk.PhotoImage(
            Image.open('img/ThiefFox.png'))  # zorro-> 3
        img_Pinocchio = ImageTk.PhotoImage(
            Image.open('img/PinocchioPerdido.png'))  # Pinocchio-> 4
        img_Gepetto = ImageTk.PhotoImage(
            Image.open('img/Gepetto.png'))  # Gepetto-> 5
        
        # Con el bucle organizaremos cada personaje en su sitio, segun la matriz.
        posY = 80 # Las posiciones empiezan inicializadas.
        for filas in map:
            posX = 160 # posX empieza en 160 cada avanza a la siguiente fila.
            for columnas in filas:
                try:
                    if columnas == 0.0:
                        CTkLabel(master=self, text='', image=img_mindWall,).place(x=posX, y=posY)
                    elif columnas == 1.0:
                        None # No se ejecutara nada, porque no es necesaria una imagen.
                    elif columnas == 2.0:
                        CTkLabel(master=self, text='',image=img_Smoking).place(x=posX, y=posY)
                    elif columnas == 3.0:
                        CTkLabel(master=self, text='',image=img_Fox).place(x=posX, y=posY)
                    elif columnas == 4.0:
                        CTkLabel(master=self, text='',image=img_Pinocchio).place(x=posX, y=posY)
                    elif columnas == 5.0:
                        CTkLabel(master=self, text='',image=img_Gepetto).place(x=posX, y=posY)
                    else:
                        print(f"Error en la matriz del {optionmenu.get()}")
                    posX+=100
                except:
                    print(f'Error al crear los labels.image')
            posY+=100

    def reader(self):
        """
        skiprows: Salta a la linea que le indique el argumento (int)
        ingresado. Esto en caso de que el txt tenga encabezado.
        Cada elemento, en la matriz, es de tipo <class 'numpy.float64'>
        """
        global map
        
        try:
            map = loadtxt(f'data/{optionmenu.get()}.txt', skiprows=3)
            #print(f'selecciono el {optionmenu.get()}')
            print(map)
            print('datos tipo:', type(map[0][1]))
        except:
            print('Error en la selección del mapa')

    def activateButton(self, button):
        button._state='enable'
        button._state='normal'
        button._hover=True
        button._text_color='red'

    def tabView(self):
        tab_view = CTkTabview(master=self, width=510, height=545)
        tab_view.add('GAME')
        tab_view.place(x=155, y=40)
        
        img_Scenario = ImageTk.PhotoImage(
            Image.open('img/Scenario.png'))  # casilla-> 1
        CTkLabel(master=self, text='',image=img_Scenario).place(x=160, y=80)

if __name__=="__main__":
    window = Window()
    window.mainloop()
