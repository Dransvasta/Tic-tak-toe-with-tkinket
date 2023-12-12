import tkinter as tk
boxes={1:[0,0,100,100],2:[100,0,200,100],3:[200,0,300,100],4:[0,100,100,200],5:[100,100,200,200],6:[200,100,300,200],7:[0,200,100,300],8:[100,200,200,300],9:[200,200,300,300]}
turn=0
tik_buttons_enabled=True
player_places={0:[],1:[]}
custom_font = ("Helvetica", 16, "bold")
label_text="Player 1"
p1=0
p2=0
def update_label2():
    label2.config(text="Player 1: "+str(p1)+"\n"+"Player 2: "+str(p2))
def clear_canvas():
    canvas.delete("all")
def Retry1():
    main1(canvas)
    Retry_button.grid_forget()
def commonwin():
    global tik_buttons_enabled
    tik_buttons_enabled=False
    label.config(text="No One Wins")
    #Retry_button=tk.button(button = tk.Button(root, text="Retry", command=Retry1))
    Retry_button.grid(row=1,column=1)
def gameover():
    global turn 
    global player_places
    global tik_buttons_enabled
    wins=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    #print("---------------------------------------")
    for i in wins:
        #print(i)
        #print(player_places[turn])
        #print(i in player_places[turn])
        c=True
        for j in i:
            if j not in player_places[turn]:
                c=False
                break
        if c:
            tik_buttons_enabled=False
            global p1
            global p2
            if turn==0:
                p1+=1
            else:
                p2+=1
            update_label2()
            label.config(text="**Gameover**\n"+"Player "+str(turn+1)+" Wins!!!!!")
            #Retry_button=tk.button(button = tk.Button(root, text="Retry", command=Retry1))
            Retry_button.grid(row=1,column=1)
            return True
    if len(player_places[turn])+len(player_places[1-turn])==9:
        commonwin()
        return True
    return False
def update_label():
    label.config(text=label_text)

def schedule_update():
    # Schedule the update_label function to be called after 2000 milliseconds
    root.after(2000, update_label)
def draw_tictak(canvas):
    canvas.create_rectangle(100, 0, 101, 300, fill='black')
    canvas.create_rectangle(200, 0, 201, 300, fill='black')
    canvas.create_rectangle(0, 100, 300, 101, fill='black')
    canvas.create_rectangle(0, 200, 300, 201, fill='black')
def on_canvas_click(event):
    global boxes
    global turn
    global label_text
    if tik_buttons_enabled:
        x = canvas.canvasx(event.x)
        y = canvas.canvasy(event.y)
        for i, d1 in boxes.items():
            if (d1[0]<x<d1[2]) and (d1[1]<y<d1[3]):
                if i not in player_places[turn] and i not in player_places[1-turn]:
                    text_x=(d1[0]+d1[2])//2
                    text_y=(d1[1]+d1[3])//2
                    text_content="O" if turn==0 else "X"
                    canvas.create_text(text_x, text_y, text=text_content, font=("Arial", 30))
                    player_places[turn].append(i)
                    print(player_places)
                    if not gameover():
                        turn=1-turn
                        label_text="Player "+str(turn+1)
                        update_label()
                    #gameover()
                    break
                else:
                    label.config(text="Wrong Input")
                    schedule_update()
def main1(canvas):
    clear_canvas()
    global tik_buttons_enabled
    global label_text
    global player_places
    global turn 
    turn=0
    label_text="Player 1"
    update_label()
    player_places={0:[],1:[]}
    tik_buttons_enabled=True
    draw_tictak(canvas)
# Create the main window
root = tk.Tk()
root.title("Canvas Example")
Retry_button=tk.Button(root, text="Play Again", command=Retry1,pady=20,padx=40)
# Create a canvas widget
canvas = tk.Canvas(root, width=300, height=300, bg='white',highlightthickness=2, highlightbackground='black')
canvas.grid(row=0,column=0,rowspan=3,pady=5,padx=5)
canvas.bind("<Button-1>", on_canvas_click)
label = tk.Label(root, text=label_text,font=custom_font,pady=20)
label.grid(row=2,column=1)
label2=tk.Label(root,font=custom_font)
label2.grid(row=0,column=1)
#label.place(x=50, y=30)



main1(canvas)
update_label2()

root.mainloop()