from tkinter import *   #knihovna pro GUI


def encode(msg, div):
    n = len(div) - 1
    code = '0'.zfill(n)
    out = msg
    msg = msg + code

    # konverze na list kvuli jednoduchosti
    msg = list(msg)
    div = list(div)

    for i in range(len(msg)-n):
        #pokud je msg bit 1 -> vykonej modulo 2...
        if msg[i] == '1':
            for j in range(len(div)):
                msg[i+j] = str((int(msg[i+j])+int(div[j]))%2)

    out += ''.join(msg[-len(code):])
    return out 

def check(msg, div):
    n = len(div) - 1 
    # konverze na list kvuli jednoduchosti
    msg = list(msg)
    div = list(div)

    for i in range(len(msg)-n):
        if msg[i] == '1':
            for j in range(len(div)):
                msg[i+j] = str((int(msg[i+j])+int(div[j]))%2)

    return int(''.join(msg[-n:])) == 0

#___________________________funkce pro encode a check button______________

def encode_print():
    msg = inputmsg.get("1.0","end-1c")
    key = inputkey.get("1.0","end-1c")
    if all(c in msg for c in "01") & all(c in key for c in "01"):   #validuje vstupy
        outmsg.set(encode(msg,key))
    else:
        outmsg.set("Chyba! Vlozte polynom jen ve forme 10010")

def check_print():
    msg = inputmsg.get("1.0","end-1c")
    key = inputkey.get("1.0","end-1c")
    if all(c in msg for c in "01") & all(c in key for c in "01"):    
        if(check(inputmsg.get("1.0","end-1c"),inputkey.get("1.0","end-1c"))):
            outmsg.set("True")
        else:
            outmsg.set("False")
    else:
            outmsg.set("Chyba! Vlozte polynom jen ve forme 10010")

#__________________________________GUI_________________________________
top = Tk(className=' CRC python')
var = StringVar()
inputtxt = Label(top, textvariable=var)
var.set("Vstupni polynom ve forme 11010011101100")
inputtxt.pack()

top.geometry("500x400")
inputmsg = Text(top,
                   height = 1,
                   width = 50)
inputmsg.pack()

var = StringVar()
inputtxt = Label(top, textvariable=var)
var.set("Generujici polynom ve forme 1011")
inputtxt.pack()

inputkey = Text(top,
                   height = 1,
                   width = 30)
inputkey.pack()

m= Label(top, textvariable="") #pouzito jako prazdny prostor
m.pack()

encode_button = Button(top,text="Encode", command=encode_print)
encode_button.pack()

check_button = Button(top,text="Check", command=check_print)
check_button.pack()

outmsg = StringVar()
encodedmsg = Label(top, textvariable=outmsg)
encodedmsg.pack()


autor = StringVar()
autor.set("Autor: Olda Tihelka")
autor= Label(top, textvariable=autor)
autor.pack()

top.mainloop()  #nekonecny loop GUI
#___________________________konec GUI______________________________________________