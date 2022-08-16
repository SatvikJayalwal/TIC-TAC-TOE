from tkinter import*
from tkinter import messagebox
import tkinter as tk

root=Tk()
root.title("TIC TAC TOE")
clicked=True
count=0

def result():
    global winner
    winner=False
    #check for X
    if btn1["text"]=="X" and btn2["text"]=="X" and btn3["text"]=="X" :
        btn1.config(bg="gold")
        btn2.config(bg="gold")
        btn3.config(bg="gold")
        winner=True
        messagebox.showinfo("TIC TAC TOE","X WON THE GAME!")
        launch()
    
    elif btn4["text"]=="X" and btn5["text"]=="X" and btn6["text"]=="X" :
        btn4.config(bg="gold")
        btn5.config(bg="gold")
        btn6.config(bg="gold")
        winner=True
        messagebox.showinfo("TIC TAC TOE","X WON THE GAME!")
        launch()

    elif btn7["text"]=="X" and btn8["text"]=="X" and btn9["text"]=="X" :
        btn7.config(bg="gold")
        btn8.config(bg="gold")
        btn9.config(bg="gold")
        winner=True
        messagebox.showinfo("TIC TAC TOE","X WON THE GAME!")
        launch()
    
    elif btn1["text"]=="X" and btn4["text"]=="X" and btn7["text"]=="X" :
        btn1.config(bg="gold")
        btn4.config(bg="gold")
        btn7.config(bg="gold")
        winner=True
        messagebox.showinfo("TIC TAC TOE","X WON THE GAME!")
        launch()

    elif btn2["text"]=="X" and btn5["text"]=="X" and btn8["text"]=="X" :
        btn2.config(bg="gold")
        btn5.config(bg="gold")
        btn8.config(bg="gold")
        winner=True
        messagebox.showinfo("TIC TAC TOE","X WON THE GAME!")
        launch()
    
    elif btn3["text"]=="X" and btn6["text"]=="X" and btn9["text"]=="X" :
        btn3.config(bg="gold")
        btn6.config(bg="gold")
        btn9.config(bg="gold")
        winner=True
        messagebox.showinfo("TIC TAC TOE","X WON THE GAME!")
        launch()

    elif btn1["text"]=="X" and btn5["text"]=="X" and btn9["text"]=="X" :
        btn1.config(bg="gold")
        btn5.config(bg="gold")
        btn9.config(bg="gold")
        winner=True
        messagebox.showinfo("TIC TAC TOE","X WON THE GAME!")
        launch()

    elif btn3["text"]=="X" and btn5["text"]=="X" and btn7["text"]=="X" :
        btn3.config(bg="gold")
        btn5.config(bg="gold")
        btn7.config(bg="gold")
        winner=True
        messagebox.showinfo("TIC TAC TOE","X WON THE GAME!")
        launch()
   
    #check for O
    elif btn1["text"]=="O" and btn2["text"]=="O" and btn3["text"]=="O" :
        btn1.config(bg="gold")
        btn2.config(bg="gold")
        btn3.config(bg="gold")
        winner=True
        messagebox.showinfo("TIC TAC TOE","O WON THE GAME!")
        launch()
    
    elif btn4["text"]=="O" and btn5["text"]=="O" and btn6["text"]=="O" :
        btn4.config(bg="gold")
        btn5.config(bg="gold")
        btn6.config(bg="gold")
        winner=True
        messagebox.showinfo("TIC TAC TOE","O WON THE GAME!")
        launch()

    elif btn7["text"]=="O" and btn8["text"]=="O" and btn9["text"]=="O" :
        btn7.config(bg="gold")
        btn8.config(bg="gold")
        btn9.config(bg="gold")
        winner=True
        messagebox.showinfo("TIC TAC TOE","O WON THE GAME!")
        launch()
    
    elif btn1["text"]=="O" and btn4["text"]=="O" and btn7["text"]=="O" :
        btn1.config(bg="gold")
        btn4.config(bg="gold")
        btn7.config(bg="gold")
        winner=True
        messagebox.showinfo("TIC TAC TOE","O WON THE GAME!")
        launch()

    elif btn2["text"]=="O" and btn5["text"]=="O" and btn8["text"]=="O" :
        btn2.config(bg="gold")
        btn5.config(bg="gold")
        btn8.config(bg="gold")
        winner=True
        messagebox.showinfo("TIC TAC TOE","O WON THE GAME!")
        launch()
    
    elif btn3["text"]=="O" and btn6["text"]=="O" and btn9["text"]=="O" :
        btn3.config(bg="gold")
        btn6.config(bg="gold")
        btn9.config(bg="gold")
        winner=True
        messagebox.showinfo("TIC TAC TOE","O WON THE GAME!")
        launch()

    elif btn1["text"]=="O" and btn5["text"]=="O" and btn9["text"]=="O" :
        btn1.config(bg="gold")
        btn5.config(bg="gold")
        btn9.config(bg="gold")
        winner=True
        messagebox.showinfo("TIC TAC TOE","O WON THE GAME!")
        launch()

    elif btn3["text"]=="O" and btn5["text"]=="O" and btn7["text"]=="O" :
        btn3.config(bg="gold")
        btn5.config(bg="gold")
        btn7.config(bg="gold")
        winner=True
        messagebox.showinfo("TIC TAC TOE","O WON THE GAME!")
        launch()

    #check if tie
    if count==9 and winner==False:
        messagebox.showinfo("TIC TAC TOE","OOPS! IT'S A TIE!")
        launch()
    
def btn_click(b):
    global clicked,count

    if b["text"] == " " and clicked == True:
        b["text"]="X"
        b.config(bg="black",fg="white")
        clicked=False
        count+=1
        result()

    elif b["text"]==" " and clicked == False:
        b["text"] = "O"
        b.config(bg="black",fg="red")
        clicked=True
        count+=1
        result()

    else:
        messagebox.showerror("TIC TAC TOE","Oops! Box is already selected\nPick another Box...")

def launch():
    global btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9
    global clicked,count
    clicked=True
    count=0

    btn1=Button(root,text=" ",fg="black",font=("Vernada",20),height=3,width=6,bg="black", command= lambda: btn_click(btn1))
    btn1.grid(row=0,column=0)

    btn2=Button(root,text=" ",font=("Vernada",20),height=3,width=6,bg="black", command= lambda: btn_click(btn2))
    btn2.grid(row=0,column=1)
    btn3=Button(root,text=" ",font=("Vernada",20),height=3,width=6,bg="black", command= lambda: btn_click(btn3))
    btn3.grid(row=0,column=2)

    btn4=Button(root,text=" ",font=("Vernada",20),height=3,width=6,bg="black", command= lambda: btn_click(btn4))
    btn4.grid(row=1,column=0)

    btn5=Button(root,text=" ",font=("Vernada",20),height=3,width=6,bg="black", command= lambda: btn_click(btn5))
    btn5.grid(row=1,column=1)

    btn6=Button(root,text=" ",font=("Vernada",20),height=3,width=6,bg="black", command= lambda: btn_click(btn6))
    btn6.grid(row=1,column=2)

    btn7=Button(root,text=" ",font=("Vernada",20),height=3,width=6,bg="black", command= lambda: btn_click(btn7))
    btn7.grid(row=2,column=0)

    btn8=Button(root,text=" ",font=("Vernada",20),height=3,width=6,bg="black", command= lambda: btn_click(btn8))
    btn8.grid(row=2,column=1)

    btn9=Button(root,text=" ",font=("Vernada",20),height=3,width=6,bg="black", command= lambda: btn_click(btn9))
    btn9.grid(row=2,column=2)

launch()

root.mainloop()
