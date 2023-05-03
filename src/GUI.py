from customtkinter import *

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
        
        self.labels()
        self.buttons()
        self.switchs()
        self.optionMenus()
        self.tabviews()
        
    def labels(self):
        label = CTkLabel(
            master=self, text="Maps", fg_color="transparent",
            width=80, height=30, font=('Comic Sans MS', 23))
        label.place(x=40,y=455)
        
    def buttons(self):
        def funcion_button_BFS():
            print("button BFS pressed")

        def funcion_button_UCS():
            print("button UCS pressed")

        def funcion_button_IDFS():
            print("button IDFS pressed")
        
        buttonBFS = CTkButton(
            master=self, text="BFS", command=funcion_button_BFS,
            width=120, height=50, border_width=0, state='enable',
            corner_radius=8, font=('Comic Sans MS', 23))
        buttonBFS.place(x=self.disHorinzButt, y=75)

        buttonBFS = CTkButton(
            master=self, text="UCS", command=funcion_button_UCS,
            width=120, height=50, border_width=0, state='disabled',
            corner_radius=8, font=('Comic Sans MS', 23))
        buttonBFS.place(x=self.disHorinzButt, y=155)

        buttonBFS = CTkButton(
            master=self, text="IDFS", command=funcion_button_IDFS,
            width=120, height=50, border_width=0, state='enable',
            corner_radius=8, font=('Comic Sans MS', 23))
        buttonBFS.place(x=self.disHorinzButt, y=235)

    def switchs(self):
        def switch_event():
            print("switch toggled, current value:", switch_var.get()) 
            # imprime lo que haya en la variable switch_var
        switch_var = StringVar(value="on") # se inicializa su valor en 'on'
        switch = CTkSwitch(
            master=self, text="Evitar\nDevolverse",
            command=switch_event, variable=switch_var,
            onvalue="Con farmac-On", offvalue="Sin farmacon",
            width=120,height=50, font=('Comic Sans MS', 18))
        # Se obtienen dos resultados, cuando se activa y cuando se desactiva
        switch.place(x=self.disHorinzButt, y=375)

    def optionMenus(self):
        def optionmenu_callback(choice):
            print("optionmenu dropdown clicked:", choice)

        optionmenu = CTkOptionMenu(
            master=self, values=["map 1", "map 2", "custom"],
            command=optionmenu_callback, width=120, height=50)
        optionmenu.set("Maps")
        optionmenu.place(x=self.disHorinzButt, y=495)

    def tabviews(self):
        # - TabView -
        tabView = CTkTabview(master=self, width=500, height=530)
        tabView.place(x=160,y=50)

        tabView.add('Game')
        tabView.add('Map')
        # Ensayo para ver si se creaba dentro del tabview (y sí)
        label_tab = CTkLabel(
            master=tabView, text="Prueba label", fg_color="transparent",
            width=80, height=30, font=('Comic Sans MS', 23))
        label_tab.place(x=0,y=0)

if __name__=="__main__":
    window = Window()
    window.mainloop()

""" ------------------------- MAIN FRAME -------------------------
En este frame se trabajará todo los componentes que se van a agregar para la app.

main_frame = ctk.CTkFrame(master=root, width=wventana, height=hventana)
main_frame.place(x=0,y=0)

"""