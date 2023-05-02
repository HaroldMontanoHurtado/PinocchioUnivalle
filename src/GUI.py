import customtkinter as ctk

root = ctk.CTk() # se crea la ventana raiz

# variables creadas para centrar la ventana al iniciar el programa
wtotal = root.winfo_screenwidth()
htotal = root.winfo_screenheight()
wventana = 680
hventana = 600
pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)
root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight-50))

root.title('Pinocchio - Artificial intelligence')
root.resizable(0,0)

""" ------------------------- MAIN FRAME -------------------------
En este frame se trabajará todo los componentes que se van a agregar para la app.
"""
main_frame = ctk.CTkFrame(master=root, width=wventana, height=hventana)
main_frame.place(x=0,y=0)

# - Labels -
label = ctk.CTkLabel(master=main_frame, text="Maps", fg_color="transparent",
                     width=80, height=30, font=('Comic Sans MS', 23))
label.place(x=40,y=455)

# Llamado de las clases que implementan cada algoritmo
def funcion_button_BFS():
    print("button BFS pressed")

def funcion_button_UCS():
    print("button UCS pressed")

def funcion_button_IDFS():
    print("button IDFS pressed")

# - Botones -
disHorinzButt = 20

buttonBFS = ctk.CTkButton(master=main_frame, text="BFS", command=funcion_button_BFS,
                       width=120, height=50, border_width=0, state='enable',
                       corner_radius=8, font=('Comic Sans MS', 23))
buttonBFS.place(x=disHorinzButt, y=75)

buttonBFS = ctk.CTkButton(master=main_frame, text="UCS", command=funcion_button_UCS,
                       width=120, height=50, border_width=0, state='disabled',
                       corner_radius=8, font=('Comic Sans MS', 23))
buttonBFS.place(x=disHorinzButt, y=155)

buttonBFS = ctk.CTkButton(master=main_frame, text="IDFS", command=funcion_button_IDFS,
                       width=120, height=50, border_width=0, state='enable',
                       corner_radius=8, font=('Comic Sans MS', 23))
buttonBFS.place(x=disHorinzButt, y=235)

# - Switch -
def switch_event():
    print("switch toggled, current value:", switch_var.get()) 
    # imprime lo que haya en la variable switch_var

switch_var = ctk.StringVar(value="on") # se inicializa su valor en 'on'
switch = ctk.CTkSwitch(master=main_frame, text="Evitar\nDevolverse",
                       command=switch_event, variable=switch_var,
                       onvalue="Con farmac-On", offvalue="Sin farmacon",
                       width=120,height=50, font=('Comic Sans MS', 18))
# Se obtienen dos resultados, cuando se activa y cuando se desactiva
switch.place(x=disHorinzButt, y=375)

# - Option Menu -
def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

optionmenu = ctk.CTkOptionMenu(master=main_frame,
                               values=["map 1", "map 2", "custom"],
                               command=optionmenu_callback,
                               width=120,height=50)
optionmenu.set("Maps")
optionmenu.place(x=disHorinzButt, y=495)

# - TabView -
tabView = ctk.CTkTabview(master=main_frame, width=500, height=530)
tabView.place(x=160,y=50)


tabView.add('Game')
tabView.add('Map')


root.mainloop()