from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import winsound
import random

root = Tk()
root.title("Bataille navale")
root.geometry("700x500")
root.iconbitmap('icon.ico')
main = Frame(root)


def main_f(): #Create menu
    main.pack(fill="both", expand=1)
    main_canvas=Canvas(main,width=710,height=510, bg="white")
    main_canvas.place(x=350,y=250,anchor="center")
    bg_open = Image.open("images/background.jpeg")
    bg = bg_open.resize((710,510))
    main_canvas.map = ImageTk.PhotoImage(bg)
    main_canvas.create_image(0,0,anchor="nw", image=main_canvas.map)
    Label(main, text="Bataille navale",relief=SOLID, font=("Arial", 25)).place(relx=0.5,rely=0.05,anchor="center")
    Button(main, text="Jouer", font=("Arial", 18), borderwidth=10, command=toplevel).place(relx=0.5,rely=0.4,anchor="center")
    Button(main, text="Règles", font=("Arial", 18), borderwidth=5, command=rules).place(relx=0.5,rely=0.6,anchor="center")

def rules():
    xx = Toplevel(main)
    xx.title("Règles")
    text = Text(xx)
    text.pack()
    text.insert(END, 
    """Au début du jeu, chaque joueur place à sa guise tous les bateaux sur sa grille de façon stratégique. 
Le but étant de compliquer au maximum la tache de son adversaire, c’est-à-dire détruire tous vos navires. 
Bien entendu, le joueur ne voit pas la grille de son adversaire.
Une fois tous les bateaux en jeu, la partie peut commencer.. Un à un, les joueurs se tire dessus pour détruire les navires ennemis.
Une partie de bataille navale se termine lorsque l’un des joueurs n’a plus de navires.
    """)
    text.configure(state=DISABLED)

def toplevel():
    global x #create another window
    x = Toplevel(main, bg="lightblue")
    x.title("Joueur vs Ordinateur")
    x.geometry("1300x700")
    game()

def game():
    global x, player, change_image, conf, boat_1, boat_2, boat_3, constant, constant2,constant3,computer, b1 , b2,b3, a_c # global import constants
    Label(x, text="Joueur", font=("Arial", 18)).place(x=250, y=25,anchor="center")
    Label(x, text="Ordinateur", font=("Arial", 18)).place(x=1000, y=25,anchor="center")

    player = Canvas(x, width=550, height=550, bg="white") #create player field
    player.place(x=300,y=325,anchor="center")
    computer = Canvas(x, width=550, height=550, bg="white") #create computer field
    computer.place(x=1000,y=325,anchor="center")

    map_open = Image.open("images/map.jpg")
    map_resize = map_open.resize((505,505))
    player.map = ImageTk.PhotoImage(map_resize)
    computer.map = ImageTk.PhotoImage(map_resize)
    player.create_image(50,50,anchor="nw",image=player.map)
    computer.create_image(50,50,anchor="nw",image=computer.map)
    
    x_cor, y_cor,x2_cor,y2_cor = 0,0,0,0 #create variables
    while True: #create lines with loop function
        x_cor += 50 
        x2_cor += 50
        y2_cor = 555
        player.create_line(x_cor,y_cor,x2_cor,y2_cor)
        computer.create_line(x_cor,y_cor,x2_cor,y2_cor)
        if x_cor == 500:
            x_cor, y_cor,x2_cor,y2_cor = 0,0,0,0
            break
        
    while True:
        y_cor += 50
        x2_cor = 555
        y2_cor += 50
        player.create_line(x_cor,y_cor,x2_cor,y2_cor)
        computer.create_line(x_cor,y_cor,x2_cor,y2_cor)
        if y_cor == 500:
            x_cor, y_cor,x2_cor,y2_cor = 25,25,0,0
            break
    cor = "ABCDEFGHIJ123456789" 
    
    while True:
        x_cor += 50
        Label(player, text=cor[x2_cor],bg="white",font=("Arial",25)).place(x=x_cor,y=y_cor,anchor="center")
        Label(computer, text=cor[x2_cor],bg="white",font=("Arial",25)).place(x=x_cor,y=y_cor,anchor="center")
        x2_cor += 1
        if x2_cor == 10:
            break
        
    while True:
        x_cor = 25
        y_cor += 50
        Label(player, text=cor[x2_cor],bg="white",font=("Arial",25)).place(x=x_cor,y=y_cor,anchor="center")
        Label(computer, text=cor[x2_cor],bg="white",font=("Arial",25)).place(x=x_cor,y=y_cor,anchor="center")
        x2_cor += 1
        if x2_cor == 19:
            Label(player, text=10,bg="white",font=("Arial",25)).place(x=x_cor,y=y_cor+50,anchor="center")
            Label(computer, text=10,bg="white",font=("Arial",25)).place(x=x_cor,y=y_cor+50,anchor="center")
            break

    b1_open = Image.open("images/boat_1.png") #open ship image
    b1 = b1_open.resize((150,50)) #resize it to an optimal size
    player.background = ImageTk.PhotoImage(b1) #create a reference, otherwise picture wont show
    boat_1 = player.create_image(325,375,anchor="center", image=player.background) #create image in player field
    
    b2_open = Image.open("images/boat_2.png") #same for computer field
    b2 = b2_open.resize((150,50))
    player.background2 = ImageTk.PhotoImage(b2)
    boat_2 = player.create_image(175,375,anchor="center", image=player.background2)

    b3_open = Image.open("images/boat_1.png") #same for computer field
    b3 = b3_open.resize((100,50))
    player.background3 = ImageTk.PhotoImage(b3)
    boat_3 = player.create_image(150,325,anchor="center", image=player.background3)
    
    #Button change
    change_open = Image.open("images/change.png") #create button to rotate ships
    b4 = change_open.resize((50,50)) #resize picture 
    change_image = ImageTk.PhotoImage(b4)

    constant = False #create three constants
    constant2 = False
    constant3 = False
    
    def change(a): #function to rotate ships
        global conf, player, boat_1, boat_2, boat_3, constant, constant2,constant3
        if conf == 0:
            a += 90
            player.background = ImageTk.PhotoImage(b1.rotate(a, expand=True)) #use.rotate(angel) to rotate
            boat_1 = player.create_image(player.coords(boat_1)[0],player.coords(boat_1)[1],anchor="center", image=player.background) #get canvas coords with canvas.coords(canvas_object) to rotate the ship at his current position
            constant = True
            
        if conf == 1:
            a += 90
            player.background2 = ImageTk.PhotoImage(b2.rotate(a, expand=True))
            boat_2 = player.create_image(player.coords(boat_2)[0],player.coords(boat_2)[1],anchor="center", image=player.background2)
            constant2 = True
            constant = True
            
        if conf == 2:
            a += 90
            player.background3 = ImageTk.PhotoImage(b3.rotate(a, expand=True))
            boat_3 = player.create_image(player.coords(boat_3)[0],player.coords(boat_3)[1],anchor="center", image=player.background3)
            constant3 = True



    change_Btn = Button(x,image=change_image, command=lambda:change(a=0)) 
    change_Btn.pack(side=TOP)
    change_Btn.place(x=650,y=225,anchor="center")  
    img_label = Label(image=change_image) #reference
    img_label.image = change_image #reference

    #Button change
    change_open = Image.open("images/change.png") #create another button function to rotate it back
    b4 = change_open.resize((50,50))
    change_image2 = ImageTk.PhotoImage(b4)

    def change2(a):
        global conf, player, boat_1, boat_2, boat_3, new_x, constant, constant2,constant3
        if conf == 0:
            player.background = ImageTk.PhotoImage(b1.rotate(a, expand=True))
            boat_1 = player.create_image(player.coords(boat_1)[0],player.coords(boat_1)[1],anchor="center", image=player.background)
            constant = False
        if conf == 1:
            player.background2 = ImageTk.PhotoImage(b2.rotate(a, expand=True))
            boat_2 = player.create_image(player.coords(boat_2)[0],player.coords(boat_2)[1],anchor="center", image=player.background2)
            constant2 = False
            constant = False
        if conf == 2:
            player.background3 = ImageTk.PhotoImage(b3.rotate(a, expand=True))
            boat_3 = player.create_image(player.coords(boat_3)[0],player.coords(boat_3)[1],anchor="center", image=player.background3)
            constant3 = False

    change_Btn2 = Button(x,image=change_image2, command=lambda:change2(a=0))
    change_Btn2.pack(side=TOP)
    change_Btn2.place(x=650,y=300,anchor="center")  
    img_label2 = Label(image=change_image2)
    img_label2.image = change_image2


    conf = 0
    def move(e): #create function to move
        #get original coords and use % operator to place it optimal in the field
        #when output of % > 25, use loop funtion to add it up till 50, same for <25 and >0
        
        global player, conf, boat_1, boat_2,boat_3, new_x, constant
        if constant == False: #if constat is false, ship remains horizontal
            if conf == 0:
                player.background = ImageTk.PhotoImage(b1)
                boat_1 = player.create_image(e.x,e.y,anchor="center", image=player.background)
            elif conf == 1 and constant2 == False:
                if int(player.coords(boat_1)[0])%50 > 25:
                    new_x = int(player.coords(boat_1)[0])
                    while True:
                        new_x += 1
                        if new_x%50 == 0:
                            break
                        
                    if int(player.coords(boat_1)[1])%50 > 25:
                        new_y = int(player.coords(boat_1)[1])
                        while True:
                            new_y += 1
                            if new_y%50 == 0:
                                player.background = ImageTk.PhotoImage(b1)
                                boat_1 = player.create_image(new_x-25,new_y-25,anchor="center", image=player.background)
                                break
                            
                    if int(player.coords(boat_1)[1])%50 < 25 and int(player.coords(boat_1)[0])%50 > 0:
                        new_y = int(player.coords(boat_1)[1])
                        while True:
                            new_y -= 1
                            if new_y%50 == 0:
                                player.background = ImageTk.PhotoImage(b1)
                                boat_1 = player.create_image(new_x-25,new_y-25,anchor="center", image=player.background)
                                break
                            
                if int(player.coords(boat_1)[0])%50 < 25 and int(player.coords(boat_1)[0])%50 > 0:
                    new_x = int(player.coords(boat_1)[0])
                    while True:
                        new_x -= 1
                        if new_x%50 == 0:
                            break
                        
                    if int(player.coords(boat_1)[1])%50 < 25 and int(player.coords(boat_1)[0])%50 > 0:
                        new_y = int(player.coords(boat_1)[1])
                        while True:
                            new_y -= 1
                            if new_y%50 == 0:
                                player.background = ImageTk.PhotoImage(b1)
                                boat_1 = player.create_image(new_x+25,new_y-25,anchor="center", image=player.background)
                                break
                            
                    if int(player.coords(boat_1)[1])%50 > 25:
                        new_y = int(player.coords(boat_1)[1])
                        while True:
                            new_y += 1
                            if new_y%50 == 0:
                                player.background = ImageTk.PhotoImage(b1)
                                boat_1 = player.create_image(new_x+25,new_y-25,anchor="center", image=player.background)
                                break
                            
                player.background2 = ImageTk.PhotoImage(b2)
                boat_2 = player.create_image(e.x,e.y,anchor="center", image=player.background2)
                
        elif constant == True: #if constat is true, ship remains vertical
            if conf == 0:
                player.background = ImageTk.PhotoImage(b1.rotate(90, expand=True))
                boat_1 = player.create_image(e.x,e.y,anchor="center", image=player.background)
            elif conf == 1 and constant2 == True:
                if int(player.coords(boat_1)[0])%50 > 25:
                    new_x = int(player.coords(boat_1)[0])
                    while True:
                        new_x += 1
                        if new_x%50 == 0:
                            break
                        
                    if int(player.coords(boat_1)[1])%50 > 25:
                        new_y = int(player.coords(boat_1)[1])
                        while True:
                            new_y += 1
                            if new_y%50 == 0:
                                player.background = ImageTk.PhotoImage(b1.rotate(90, expand=True))
                                boat_1 = player.create_image(new_x-25,new_y-25,anchor="center", image=player.background)
                                break
                            
                    if int(player.coords(boat_1)[1])%50 < 25 and int(player.coords(boat_1)[0])%50 > 0:
                        new_y = int(player.coords(boat_1)[1])
                        while True:
                            new_y -= 1
                            if new_y%50 == 0:
                                player.background = ImageTk.PhotoImage(b1.rotate(90, expand=True))
                                boat_1 = player.create_image(new_x-25,new_y-25,anchor="center", image=player.background)
                                break
                            
                if int(player.coords(boat_1)[0])%50 < 25 and int(player.coords(boat_1)[0])%50 > 0:
                    new_x = int(player.coords(boat_1)[0])
                    while True:
                        new_x -= 1
                        if new_x%50 == 0:
                            break
                        
                    if int(player.coords(boat_1)[1])%50 < 25 and int(player.coords(boat_1)[0])%50 > 0:
                        new_y = int(player.coords(boat_1)[1])
                        while True:
                            new_y -= 1
                            if new_y%50 == 0:
                                player.background = ImageTk.PhotoImage(b1.rotate(90, expand=True))
                                boat_1 = player.create_image(new_x+25,new_y-25,anchor="center", image=player.background)
                                break
                            
                    if int(player.coords(boat_1)[1])%50 > 25:
                        new_y = int(player.coords(boat_1)[1])
                        while True:
                            new_y += 1
                            if new_y%50 == 0:
                                player.background = ImageTk.PhotoImage(b1.rotate(90, expand=True))
                                boat_1 = player.create_image(new_x+25,new_y-25,anchor="center", image=player.background)
                                break
                            
                player.background2 = ImageTk.PhotoImage(b2.rotate(90, expand=True))
                boat_2 = player.create_image(e.x,e.y,anchor="center", image=player.background2)
        if conf == 2:
            if constant3 == False:
                player.background3 = ImageTk.PhotoImage(b3)
                boat_3 = player.create_image(e.x,e.y,anchor="center", image=player.background3)
            elif constant3 == True:
                player.background3 = ImageTk.PhotoImage(b3.rotate(90, expand=True))
                boat_3 = player.create_image(e.x,e.y,anchor="center", image=player.background3)
    player.bind("<B1-Motion>", move) #function for moving, when click and drag
    
    def confi(): #function for confirmations
        #if boat 1 is placed, boat 2 will be placed then
        global conf, player, boat_1, boat_2,boat_3, new_x, constant2, constant3
        conf += 1
        constant == False
        
        if conf == 2:
            if constant2 == False: #if constat is false, ship remains horizontal
                if int(player.coords(boat_2)[0])%50 > 25:
                    new_x = int(player.coords(boat_2)[0])
                    while True:
                        new_x += 1
                        if new_x%50 == 0:
                            break
                        
                    if int(player.coords(boat_2)[1])%50 > 25:
                        new_y = int(player.coords(boat_2)[1])
                        while True:
                            new_y += 1
                            if new_y%50 == 0:
                                player.background2 = ImageTk.PhotoImage(b2)
                                boat_2 = player.create_image(new_x-25,new_y-25,anchor="center", image=player.background2)
                                break
                            
                    if int(player.coords(boat_2)[1])%50 < 25 and int(player.coords(boat_2)[0])%50 > 0:
                        new_y = int(player.coords(boat_2)[1])
                        while True:
                            new_y -= 1
                            if new_y%50 == 0:
                                player.background2 = ImageTk.PhotoImage(b2)
                                boat_2 = player.create_image(new_x-25,new_y+25,anchor="center", image=player.background2)
                                break
                            
                if int(player.coords(boat_2)[0])%50 < 25 and int(player.coords(boat_2)[0])%50 > 0:
                    new_x = int(player.coords(boat_2)[0])
                    while True:
                        new_x -= 1
                        if new_x%50 == 0:
                            break
                        
                    if int(player.coords(boat_2)[1])%50 < 25 and int(player.coords(boat_2)[0])%50 > 0:
                        new_y = int(player.coords(boat_2)[1])
                        while True:
                            new_y -= 1
                            if new_y%50 == 0:
                                player.background2 = ImageTk.PhotoImage(b2)
                                boat_2 = player.create_image(new_x+25,new_y+25,anchor="center", image=player.background2)
                                break
                            
                    if int(player.coords(boat_2)[1])%50 > 25:
                        new_y = int(player.coords(boat_2)[1])
                        while True:
                            new_y += 1
                            if new_y%50 == 0:
                                player.background2 = ImageTk.PhotoImage(b2)
                                boat_2 = player.create_image(new_x+25,new_y-25,anchor="center", image=player.background2)
                                break 
                            
            elif constant2 == True: #If its true it remains vertical
                if int(player.coords(boat_2)[0])%50 > 25:
                    new_x = int(player.coords(boat_2)[0])
                    while True:
                        new_x += 1
                        if new_x%50 == 0:
                            break
                        
                    if int(player.coords(boat_2)[1])%50 > 25:
                        new_y = int(player.coords(boat_2)[1])
                        while True:
                            new_y += 1
                            if new_y%50 == 0:
                                player.background2 = ImageTk.PhotoImage(b2.rotate(90, expand=True))
                                boat_2 = player.create_image(new_x-25,new_y-25,anchor="center", image=player.background2)
                                break
                            
                    if int(player.coords(boat_2)[1])%50 < 25 and int(player.coords(boat_2)[0])%50 > 0:
                        new_y = int(player.coords(boat_2)[1])
                        while True:
                            new_y -= 1
                            if new_y%50 == 0:
                                player.background2 = ImageTk.PhotoImage(b2.rotate(90, expand=True))
                                boat_2 = player.create_image(new_x-25,new_y+25,anchor="center", image=player.background2)
                                break
                            
                if int(player.coords(boat_2)[0])%50 < 25 and int(player.coords(boat_2)[0])%50 > 0:
                    new_x = int(player.coords(boat_2)[0])
                    while True:
                        new_x -= 1
                        if new_x%50 == 0:
                            break
                        
                    if int(player.coords(boat_2)[1])%50 < 25 and int(player.coords(boat_2)[0])%50 > 0:
                        new_y = int(player.coords(boat_2)[1])
                        while True:
                            new_y -= 1
                            if new_y%50 == 0:
                                player.background2 = ImageTk.PhotoImage(b2.rotate(90, expand=True))
                                boat_2 = player.create_image(new_x+25,new_y+25,anchor="center", image=player.background2)
                                break
                            
                    if int(player.coords(boat_2)[1])%50 > 25:
                        new_y = int(player.coords(boat_2)[1])
                        while True:
                            new_y += 1
                            if new_y%50 == 0:
                                player.background2 = ImageTk.PhotoImage(b2.rotate(90, expand=True))
                                boat_2 = player.create_image(new_x+25,new_y-25,anchor="center", image=player.background2)
                                break 
        #boat_3
        if conf == 3:
            confirm.config(text="Commencer la partie")
            if constant3 == False: #if constat is false, ship remains horizontal
                if int(player.coords(boat_3)[0])%50 > 25:
                    new_x = int(player.coords(boat_3)[0])
                    while True:
                        new_x += 1
                        if new_x%50 == 0:
                            break

                    if int(player.coords(boat_3)[1])%50 > 25:
                        new_y = int(player.coords(boat_3)[1])
                        while True:
                            new_y += 1
                            if new_y%50 == 0:
                                player.background3 = ImageTk.PhotoImage(b3)
                                boat_3 = player.create_image(new_x,new_y-25,anchor="center", image=player.background3)
                                break
                            
                    if int(player.coords(boat_3)[1])%50 < 25 and int(player.coords(boat_3)[0])%50 > 0:
                        new_y = int(player.coords(boat_3)[1])
                        while True:
                            new_y -= 1
                            if new_y%50 == 0:
                                player.background3 = ImageTk.PhotoImage(b3)
                                boat_3 = player.create_image(new_x,new_y+25,anchor="center", image=player.background3)
                                break
                            
                if int(player.coords(boat_3)[0])%50 < 25 and int(player.coords(boat_3)[0])%50 > 0:
                    new_x = int(player.coords(boat_3)[0])
                    while True:
                        new_x -= 1
                        if new_x%50 == 0:
                            break
                        
                    if int(player.coords(boat_3)[1])%50 < 25 and int(player.coords(boat_3)[0])%50 > 0:
                        new_y = int(player.coords(boat_3)[1])
                        while True:
                            new_y -= 1
                            if new_y%50 == 0:
                                player.background3 = ImageTk.PhotoImage(b3)
                                boat_3 = player.create_image(new_x,new_y+25,anchor="center", image=player.background3)
                                break
                            
                    if int(player.coords(boat_3)[1])%50 > 25:
                        new_y = int(player.coords(boat_3)[1])
                        while True:
                            new_y += 1
                            if new_y%50 == 0:
                                player.background3 = ImageTk.PhotoImage(b3)
                                boat_3 = player.create_image(new_x,new_y-25,anchor="center", image=player.background3)
                                break 
                            
            elif constant3 == True: #If its true it remains vertical
                if int(player.coords(boat_3)[0])%50 > 25:
                    new_x = int(player.coords(boat_3)[0])
                    while True:
                        new_x += 1
                        if new_x%50 == 0:
                            break
                        
                    if int(player.coords(boat_3)[1])%50 > 25:
                        new_y = int(player.coords(boat_3)[1])
                        while True:
                            new_y += 1
                            if new_y%50 == 0:
                                player.background3 = ImageTk.PhotoImage(b3.rotate(90, expand=True))
                                boat_3 = player.create_image(new_x+25,new_y,anchor="center", image=player.background3)
                                break
                            
                    if int(player.coords(boat_3)[1])%50 < 25 and int(player.coords(boat_3)[0])%50 > 0:
                        new_y = int(player.coords(boat_3)[1])
                        while True:
                            new_y -= 1
                            if new_y%50 == 0:
                                player.background3 = ImageTk.PhotoImage(b3.rotate(90, expand=True))
                                boat_3 = player.create_image(new_x-25,new_y,anchor="center", image=player.background3)
                                break
                            
                if int(player.coords(boat_3)[0])%50 < 25 and int(player.coords(boat_3)[0])%50 > 0:
                    new_x = int(player.coords(boat_3)[0])
                    while True:
                        new_x -= 1
                        if new_x%50 == 0:
                            break
                        
                    if int(player.coords(boat_3)[1])%50 < 25 and int(player.coords(boat_3)[0])%50 > 0:
                        new_y = int(player.coords(boat_3)[1])
                        while True:
                            new_y -= 1
                            if new_y%50 == 0:
                                player.background3 = ImageTk.PhotoImage(b3.rotate(90, expand=True))
                                boat_3 = player.create_image(new_x-25,new_y,anchor="center", image=player.background3)
                                break
                            
                    if int(player.coords(boat_3)[1])%50 > 25:
                        new_y = int(player.coords(boat_3)[1])
                        while True:
                            new_y += 1
                            if new_y%50 == 0:
                                player.background3 = ImageTk.PhotoImage(b3.rotate(90, expand=True))
                                boat_3 = player.create_image(new_x+25,new_y,anchor="center", image=player.background3)
                                break 
                            
        if conf == 4:
            confirm.destroy()
            Label(x, text="Cliquer pour attaquer").place(relx=0.25,rely=0.9,anchor="center")
            start()
    confirm = Button(x, text="Confirmation du bateau", command=confi)
    confirm.place(relx=0.25,rely=0.9,anchor="center")
    a_c = 0
    
    
    def start():
        
        #start game function
        def attack(e):
            global nx, ny
            #get coords from the mouse to place the optimal X
            #same princip as previous
            ny = e.y
            nx = e.x
            mx = 0
            my = 0
            if e.x%50 >= 25:
                nx = e.x
                while True:
                    nx += 1
                    if nx%50 == 0:
                        mx = -25
                        break
                    
            if e.x%50 < 25 and e.x%50 >= 0:
                nx = e.x
                while True:
                    nx -= 1
                    if nx%50 == 0:
                        mx = +25
                        break
                    
            if e.y%50 >= 25:
                ny = e.y
                while True:
                    ny += 1
                    if ny%50 == 0:
                        my = -25
                        break
                    
            if e.y%50 >= 0 and e.y%50 < 25:
                ny = e.y
                while True:
                    ny -= 1
                    if ny%50 == 0:
                        my = +25
                        break
                    
            #enemy ship coordinats
            list_a = [175,275,475]
            list_b = [175,225,125]
            
            
            def playsound(): #playsound
                winsound.PlaySound('explosion.wav', winsound.SND_FILENAME)
            playsound()
            
            
            if nx+mx in list_a and ny+my in list_b: #if enemy coordinats hits, hit will be marked
                global a_c
                a_c += 1
                Label(computer,text="X",bg="white",font=("Arial",25),fg="green").place(x=nx+mx,y=ny+my,anchor="center")
                if len(list_a)*len(list_b) == a_c: #list_a * list_b = amount of fields
                    messagebox.showinfo(message="Félicitation vous avez gagné")
            else:
                Label(computer,text="X",bg="white",font=("Arial",25)).place(x=nx+mx,y=ny+my,anchor="center")

            def enemy():
                global nx, ny
                #function to place random X's on player field!
                i_list =[-75,-25,25,75]
                rx = i_list[random.randint(0,3)]
                ry = i_list[random.randint(0,3)]
                if nx+rx < 50:
                    nx += 50
                    if nx+rx <0:
                        nx += 50
                        if nx+rx <-50:
                            nx+=50
                            if nx+rx <-75:
                                nx+=50
                if ny+ry <50:
                    ny += 50
                    if ny<+ry <0:
                        ny += 50
                        if ny+ry <-50:
                            ny+=50
                            if ny+ry <-75:
                                ny+=50
                Label(player,text="X",bg="white",font=("Arial",25)).place(x=nx+rx,y=ny+ry,anchor="center")
            enemy()
        computer.bind("<Button-1>", attack)
        
        
main_f()
root.mainloop()