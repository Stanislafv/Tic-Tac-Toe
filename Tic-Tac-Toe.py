import tkinter as tk
import time
import random
root = tk.Tk()
root.title("Крестики-нолики")
root.geometry("257x370")

player_1_1 = "ㅤ"
player_1_2 = "ㅤ"
player_1_3 = "ㅤ"

player_2_1 = "ㅤ"
player_2_2 = "ㅤ"
player_2_3 = "ㅤ"

player_3_1 = "ㅤ"
player_3_2 = "ㅤ"
player_3_3 = "ㅤ"

label = tk.Label(root, text="", font=("Courier New", 24, "bold"))
label.grid(row=3, column=0, columnspan=19)

win = 0

#1_x

def click_1_1():
    global player_1_1
    if player_1_1 == "ㅤ":
        player_1_1 = "o"
        button_1_1.config(text="o", state="disabled")
        root.update()
        bot()

button_1_1 = tk.Button(root, text=player_1_1, command=click_1_1, width=4, height=2, font=("Arial", 24, "bold"))
button_1_1.grid(row=0, column=0)

def click_1_2():
    global player_1_2
    if player_1_2 == "ㅤ":
        player_1_2 = "o"
        button_1_2.config(text="o", state="disabled")
        root.update()
        bot()

button_1_2 = tk.Button(root, text=player_1_2, command=click_1_2, width=4, height=2, font=("Arial", 24, "bold"))
button_1_2.grid(row=0, column=1)

def click_1_3():
    global player_1_3
    if player_1_3 == "ㅤ":
        player_1_3 = "o"
        button_1_3.config(text="o", state="disabled")
        root.update()
        bot()

button_1_3 = tk.Button(root, text=player_1_3, command=click_1_3, width=4, height=2, font=("Arial", 24, "bold"))
button_1_3.grid(row=0, column=2)

#2_x

def click_2_1():
    global player_2_1
    if player_2_1 == "ㅤ":
        player_2_1 = "o"
        button_2_1.config(text="o", state="disabled")
        root.update()
        bot()

button_2_1 = tk.Button(root, text=player_2_1, command=click_2_1, width=4, height=2, font=("Arial", 24, "bold"))
button_2_1.grid(row=1, column=0)

def click_2_2():
    global player_2_2
    if player_2_2 == "ㅤ":
        player_2_2 = "o"
        button_2_2.config(text="o", state="disabled")
        root.update()
        bot()

button_2_2 = tk.Button(root, text=player_2_2, command=click_2_2, width=4, height=2, font=("Arial", 24, "bold"))
button_2_2.grid(row=1, column=1)

def click_2_3():
    global player_2_3
    if player_2_3 == "ㅤ":
        player_2_3 = "o"
        button_2_3.config(text="o", state="disabled")
        root.update()
        bot()

button_2_3 = tk.Button(root, text=player_2_3, command=click_2_3, width=4, height=2, font=("Arial", 24, "bold"))
button_2_3.grid(row=1, column=2)

#3_x

def click_3_1():
    global player_3_1
    if player_3_1 == "ㅤ":
        player_3_1 = "o"
        button_3_1.config(text="o", state="disabled")
        root.update()
        bot()

button_3_1 = tk.Button(root, text=player_3_1, command=click_3_1, width=4, height=2, font=("Arial", 24, "bold"))
button_3_1.grid(row=2, column=0)

def click_3_2():
    global player_3_2
    if player_3_2 == "ㅤ":
        player_3_2 = "o"
        button_3_2.config(text="o", state="disabled")
        root.update()
        bot()

button_3_2 = tk.Button(root, text=player_3_2, command=click_3_2, width=4, height=2, font=("Arial", 24, "bold"))
button_3_2.grid(row=2, column=1)

def click_3_3():
    global player_3_3
    if player_3_3 == "ㅤ":
        player_3_3 = "o"
        button_3_3.config(text="o", state="disabled")
        root.update()
        bot()

button_3_3 = tk.Button(root, text=player_3_3, command=click_3_3, width=4, height=2, font=("Arial", 24, "bold"))
button_3_3.grid(row=2, column=2)

#БОТ

def bot():
    global player_1_1
    global player_1_2
    global player_1_3
    global player_2_1
    global player_2_2
    global player_2_3
    global player_3_1
    global player_3_2
    global player_3_3
    global label

    global win

    if player_1_1 == "o" and player_1_2 == "o" and player_1_3 == "o":
        print("Вы выйграли!")
        win = 1
    elif player_2_1 == "o" and player_2_2 == "o" and player_2_3 == "o":
        print("Вы выйграли!")
        win = 1
    elif player_3_1 == "o" and player_3_2 == "o" and player_3_3 == "o":
        print("Вы выйграли!")
        win = 1
    elif player_1_1 == "o" and player_2_1 == "o" and player_3_1 == "o":
        print("Вы выйграли!")
        win = 1
    elif player_1_2 == "o" and player_2_2 == "o" and player_3_2 == "o":
        print("Вы выйграли!")
        win = 1
    elif player_1_3 == "o" and player_2_3 == "o" and player_3_3 == "o":
        print("Вы выйграли!")
        win = 1
    elif player_1_1 == "o" and player_2_2 == "o" and player_3_3 == "o":
        print("Вы выйграли!")
        win = 1
    elif player_1_3 == "o" and player_2_2 == "o" and player_3_1 == "o":
        print("Вы выйграли!")
        win = 1

    if player_1_1 != "ㅤ" and player_1_2 != "ㅤ" and player_1_3 != "ㅤ" and player_2_1 != "ㅤ" and player_2_2 != "ㅤ" and player_2_3 != "ㅤ" and player_3_1 != "ㅤ" and player_3_2 != "ㅤ" and player_3_3 != "ㅤ":
        win = 3

    elif  player_1_1 == "x" and player_1_2 == "x" and player_1_3 == "ㅤ":
        player_1_3 = "x"
        button_1_3.config(text="x")
        print("Вы проиграли!")
        win = 2
    elif player_1_1 == "x" and player_1_3 == "x" and player_1_2 == "ㅤ":
        player_1_2 = "x"
        button_1_2.config(text="x")
        print("Вы проиграли!")
        win = 2
    elif player_1_2 == "x" and player_1_3 == "x" and player_1_1 == "ㅤ":
        player_1_1 = "x"
        button_1_1.config(text="x")
        print("Вы проиграли!")
        win = 2
    
    elif  player_2_1 == "x" and player_2_2 == "x" and player_2_3 == "ㅤ":
        player_2_3 = "x"
        button_2_3.config(text="x")
        print("Вы проиграли!")
        win = 2
    elif player_2_1 == "x" and player_2_3 == "x" and player_2_2 == "ㅤ":
        player_2_2 = "x"
        button_2_2.config(text="x")
        print("Вы проиграли!")
        win = 2
    elif player_2_2 == "x" and player_2_3 == "x" and player_2_1 == "ㅤ":
        player_2_1 = "x"
        button_2_1.config(text="x")
        print("Вы проиграли!")
        win = 2

    elif  player_3_1 == "x" and player_3_2 == "x" and player_3_3 == "ㅤ":
        player_3_3 = "x"
        button_3_3.config(text="x")
        print("Вы проиграли!")
        win = 2
    elif player_3_1 == "x" and player_3_3 == "x" and player_3_2 == "ㅤ":
        player_3_2 = "x"
        button_3_2.config(text="x")
        print("Вы проиграли!")
        win = 2
    elif player_3_2 == "x" and player_3_3 == "x" and player_3_1 == "ㅤ":
        player_3_1 = "x"
        button_3_1.config(text="x")
        print("Вы проиграли!")
        win = 2

    
    elif player_1_1 == "x" and player_2_1 == "x" and player_3_1 == "ㅤ":
        player_3_1 = "x"
        button_3_1.config(text="x")
        print("Вы проиграли!")
        win = 2
    elif player_2_1 == "x" and player_3_1 == "x" and player_1_1 == "ㅤ":
        player_1_1 = "x"
        button_1_1.config(text="x")
        print("Вы проиграли!")
        win = 2
    elif player_1_1 == "x" and player_3_1 == "x" and player_2_1 == "ㅤ":
        player_2_1 = "x" 
        button_2_1.config(text="x") 
        print("Вы проиграли!")
        win = 2

    elif player_1_2 == "x" and player_2_2 == "x" and player_3_2 == "ㅤ":
        player_3_2 = "x"
        button_3_2.config(text="x")
        print("Вы проиграли!")
        win = 2
    elif player_2_2 == "x" and player_3_2 == "x" and player_1_2 == "ㅤ":
        player_1_2 = "x"
        button_1_2.config(text="x")
        print("Вы проиграли!")
        win = 2
    elif player_1_2 == "x" and player_3_2 == "x" and player_2_2 == "ㅤ":
        player_2_2 = "x" 
        button_2_2.config(text="x")
        print("Вы проиграли!")
        win = 2   

    elif player_1_3 == "x" and player_2_3 == "x" and player_3_3 == "ㅤ":
        player_3_3 = "x"
        button_3_3.config(text="x")
        print("Вы проиграли!")
        win = 2
    elif player_2_3 == "x" and player_3_3 == "x" and player_1_3 == "ㅤ":
        player_1_3 = "x"
        button_1_3.config(text="x")
        print("Вы проиграли!")
        win = 2
    elif player_1_3 == "x" and player_3_3 == "x" and player_2_3 == "ㅤ":
        player_2_3 = "x" 
        button_2_3.config(text="x")
        print("Вы проиграли!")
        win = 2 

    elif player_1_1 == "x" and player_2_2 == "x" and player_3_3 == "ㅤ":
        player_3_3 = "x"
        button_3_3.config(text="x")
        print("Вы проиграли!")
        win = 2
    elif player_2_2 == "x" and player_3_3 == "x" and player_1_1 == "ㅤ":
        player_1_1 = "x"
        button_1_1.config(text="x")
        print("Вы проиграли!")
        win = 2
    elif player_3_3 == "x" and player_1_1 == "x" and player_2_2 == "ㅤ":
        player_2_2 = "x"
        button_2_2.config(text="x")
        print("Вы проиграли!")
        win = 2

    elif player_1_3 == "x" and player_2_2 == "x" and player_3_1 == "ㅤ":
        player_3_1 = "x"
        button_3_1.config(text="x")
        print("Вы проиграли!")
        win = 2
    elif player_2_2 == "x" and player_3_1 == "x" and player_1_3 == "ㅤ":
        player_1_3 = "x"
        button_1_3.config(text="x")
        print("Вы проиграли!")
        win = 2
    elif player_3_1 == "x" and player_1_3 == "x" and player_2_2 == "ㅤ":
        player_2_2 = "x"
        button_2_2.config(text="x")
        print("Вы проиграли!")
        win = 2

    

    if  player_1_1 == "o" and player_1_2 == "o" and player_1_3 == "ㅤ":
        player_1_3 = "x"
        button_1_3.config(text="x")
    elif player_1_1 == "o" and player_1_3 == "o" and player_1_2 == "ㅤ":
        player_1_2 = "x"
        button_1_2.config(text="x")
    elif player_1_2 == "o" and player_1_3 == "o" and player_1_1 == "ㅤ":
        player_1_1 = "x"
        button_1_1.config(text="x")
    
    elif  player_2_1 == "o" and player_2_2 == "o" and player_2_3 == "ㅤ":
        player_2_3 = "x"
        button_2_3.config(text="x")
    elif player_2_1 == "o" and player_2_3 == "o" and player_2_2 == "ㅤ":
        player_2_2 = "x"
        button_2_2.config(text="x")
    elif player_2_2 == "o" and player_2_3 == "o" and player_2_1 == "ㅤ":
        player_2_1 = "x"
        button_2_1.config(text="x")

    elif  player_3_1 == "o" and player_3_2 == "o" and player_3_3 == "ㅤ":
        player_3_3 = "x"
        button_3_3.config(text="x")
    elif player_3_1 == "o" and player_3_3 == "o" and player_3_2 == "ㅤ":
        player_3_2 = "x"
        button_3_2.config(text="x")
    elif player_3_2 == "o" and player_3_3 == "o" and player_3_1 == "ㅤ":
        player_3_1 = "x"
        button_3_1.config(text="x")

    
    elif player_1_1 == "o" and player_2_1 == "o" and player_3_1 == "ㅤ":
        player_3_1 = "x"
        button_3_1.config(text="x")
    elif player_2_1 == "o" and player_3_1 == "o" and player_1_1 == "ㅤ":
        player_1_1 = "x"
        button_1_1.config(text="x")
    elif player_1_1 == "o" and player_3_1 == "o" and player_2_1 == "ㅤ":
        player_2_1 = "x"  
        button_2_1.config(text="x")  

    elif player_1_2 == "o" and player_2_2 == "o" and player_3_2 == "ㅤ":
        player_3_2 = "x"
        button_3_2.config(text="x")
    elif player_2_2 == "o" and player_3_2 == "o" and player_1_2 == "ㅤ":
        player_1_2 = "x"
        button_1_2.config(text="x")
    elif player_1_2 == "o" and player_3_2 == "o" and player_2_2 == "ㅤ":
        player_2_2 = "x"    
        button_2_2.config(text="x")

    elif player_1_3 == "o" and player_2_3 == "o" and player_3_3 == "ㅤ":
        player_3_3 = "x"
        button_3_3.config(text="x")
    elif player_2_3 == "o" and player_3_3 == "o" and player_1_3 == "ㅤ":
        player_1_3 = "x"
        button_1_3.config(text="x")
    elif player_1_3 == "o" and player_3_3 == "o" and player_2_3 == "ㅤ":
        player_2_3 = "x"  
        button_2_3.config(text="x")

    elif player_1_1 == "o" and player_2_2 == "o" and player_3_3 == "ㅤ":
        player_3_3 = "x"
        button_3_3.config(text="x")
    elif player_2_2 == "o" and player_3_3 == "o" and player_1_1 == "ㅤ":
        player_1_1 = "x"
        button_1_1.config(text="x")
    elif player_3_3 == "o" and player_1_1 == "o" and player_2_2 == "ㅤ":
        player_2_2 = "x"
        button_2_2.config(text="x")

    elif player_1_3 == "o" and player_2_2 == "o" and player_3_1 == "ㅤ":
        player_3_1 = "x"
        button_3_1.config(text="x")
    elif player_2_2 == "o" and player_3_1 == "o" and player_1_3 == "ㅤ":
        player_1_3 = "x"
        button_1_3.config(text="x")
    elif player_3_1 == "o" and player_1_3 == "o" and player_2_2 == "ㅤ":
        player_2_2 = "x"
        button_2_2.config(text="x")

    elif player_2_2 == "ㅤ":
        player_2_2 = "x"
        button_2_2.config(text="x")
    elif player_2_2 != "ㅤ":
        while win == 0:
            rand = random.randint(1,8)
            if rand == 1 and player_1_1 == "ㅤ":
                player_1_1 = "x"
                button_1_1.config(text="x")
                break
            if rand == 2 and player_1_2 == "ㅤ":
                player_1_2 = "x"
                button_1_2.config(text="x")
                break
            if rand == 3 and player_1_3 == "ㅤ":
                player_1_3 = "x"
                button_1_3.config(text="x")
                break
            if rand == 4 and player_2_1 == "ㅤ":
                player_2_1 = "x" 
                button_2_1.config(text="x")  
                break
            if rand == 5 and player_2_3 == "ㅤ":
                player_2_3 = "x" 
                button_2_3.config(text="x")
                break
            if rand == 6 and player_3_1 == "ㅤ":
                player_3_1 = "x" 
                button_3_1.config(text="x")
                break
            if rand == 7 and player_3_2 == "ㅤ":
                player_3_2 = "x" 
                button_3_2.config(text="x")
                break
            if rand == 8 and player_3_3 == "ㅤ":
                player_3_3 = "x"  
                button_3_3.config(text="x")
                break   
            else:
                continue

    if win == 1:
        label.config(text="Вы выйграли!", font=("Courier New", 24, "bold"))
        root.after(1000, restart)
    elif win == 2:
        label.config(text="Вы проиграли!", font=("Courier New", 24, "bold"))
        root.after(1000, restart)
    elif win == 3:
        label.config(text="Ничья!", font=("Courier New", 24, "bold"))
        root.after(1000, restart)
    root.update()

root.grid_columnconfigure(0, weight=0, uniform="col")
root.grid_columnconfigure(1, weight=0, uniform="col")
root.grid_columnconfigure(2, weight=0, uniform="col")

def restart():
    global player_1_1
    global player_1_2
    global player_1_3
    global player_2_1
    global player_2_2
    global player_2_3
    global player_3_1
    global player_3_2
    global player_3_3
    global win
    global label

    player_1_1 = "ㅤ"
    player_1_2 = "ㅤ"
    player_1_3 = "ㅤ"

    player_2_1 = "ㅤ"
    player_2_2 = "ㅤ"
    player_2_3 = "ㅤ"

    player_3_1 = "ㅤ"
    player_3_2 = "ㅤ"
    player_3_3 = "ㅤ"

    win = 0

    label.config(text="", font=("Courier New", 24, "bold"))

    button_1_1.config(text="ㅤ", state="active")
    button_1_2.config(text="ㅤ", state="active")
    button_1_3.config(text="ㅤ", state="active")

    button_2_1.config(text="ㅤ", state="active")
    button_2_2.config(text="ㅤ", state="active")
    button_2_3.config(text="ㅤ", state="active")

    button_3_1.config(text="ㅤ", state="active")
    button_3_2.config(text="ㅤ", state="active")
    button_3_3.config(text="ㅤ", state="active")

    

root.mainloop()