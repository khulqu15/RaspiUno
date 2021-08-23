import time
import tkinter
import serial

def ButtonMenu(value):
    global MenuValue
    global statusLamp
    MenuValue = int(value)
    print(MenuValue)
    exceptionText.set('')
    if(input1.get() == ''):
        inpt1 = int(0)
    else:
        inpt1 = int(input1.get())
    if(input2.get() == ''):
        inpt2 = int(0)
    else:
        inpt2 = int(input2.get())
    print(inpt1)
    print(inpt2)
    values = bytearray([inpt1, inpt2, MenuValue])
    ser.write(values)
    ReadSerial()

def ButtonQuit():
    global tkTop
    ser.write(bytes('L', 'UTF-8'))
    tkTop.destroy()

def ValidationInteger(value):
    if not value:
        return True
    try: 
        float(value)
        return True
    except ValueError:
        return False

def ButtonReset():
    input1.delete(0, 'end')
    input2.delete(0, 'end')

def ToggleLamp():
    global statusLamp
    print(statusLamp)
    if statusLamp == 0:
        statusLamp = 1
    else :
        statusLamp = 0
    ButtonSending()

def ButtonSending():
    global statusLamp
    global MenuValue
    if input1.get() == "":
        input1.insert(0, 0)
    if input2.get() == "":
        input2.insert(0, 0)    
    exceptionText.set('')
    values = str(statusLamp)+","+str(input1.get())+","+str(input2.get())+","+str(MenuValue)+","+str(statusLamp)
    ser.write(values.encode('utf-8'))
    print(values)
    print(values.encode)
    ReadSerial()

ser = serial.Serial('COM3', 115200)
print('Menunggu Perangkat')
time.sleep(2)
print(ser.name)
print(ser.in_waiting)

tkTop = tkinter.Tk()
screen_width = tkTop.winfo_screenwidth()
screen_height = tkTop.winfo_screenheight()
height = 300
width = 600
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
# tkTop.geometry('600x300')
tkTop.geometry('%dx%d+%d+%d' % (width, height, x, y))
tkTop.positionfrom
tkTop.title('Arduino Control')
tkTop.rowconfigure(0, minsize=300, weight=1)
tkTop.columnconfigure(1, minsize=600, weight=1)

frameMenu = tkinter.Frame(tkTop)

statusLamp = 0
MenuValue = 0

ClickMenu = tkTop.register(ButtonMenu)

button1 = tkinter.Button(frameMenu, text='Toggle Lamp', command=ToggleLamp)
button1.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
button1 = tkinter.Button(frameMenu, text='Button A', command=(ClickMenu, 1))
button1.grid(row=1, column=0, sticky='ew', padx=5, pady=5)
button2 = tkinter.Button(frameMenu, text='Button B', command=(ClickMenu, 2))
button2.grid(row=2, column=0, sticky='ew', padx=5, pady=5)
button3 = tkinter.Button(frameMenu, text='Button C', command=(ClickMenu, 3))
button3.grid(row=3, column=0, sticky='ew', padx=5, pady=5)
button4 = tkinter.Button(frameMenu, text='Button D', command=(ClickMenu, 4))
button4.grid(row=4, column=0, sticky='ew', padx=5, pady=5)

buttonQuit = tkinter.Button(frameMenu, text='Quit', command=ButtonQuit)
buttonQuit.grid(row=5, column=0, sticky='ew', padx=5, pady=5)

validation = tkTop.register(ValidationInteger)
sending = tkTop.register(ButtonSending)
frameMain = tkinter.Frame(tkTop)

label1 = tkinter.Label(frameMain, text="Integer 1")
label1.grid(row=0, column=0, sticky="sw", padx=5, pady=0)
input1 = tkinter.Entry(frameMain, validate="key", validatecommand=(validation, "%P"))
input1.grid(row=1, column=0, sticky="ew", padx=5, pady=0)

label2 = tkinter.Label(frameMain, text="Integer 2")
label2.grid(row=0, column=1, sticky="sw", padx=5, pady=0)
input2 = tkinter.Entry(frameMain, validate="key", validatecommand=(validation, "%P"))
input2.grid(row=1, column=1, sticky="ew", padx=5, pady=0)

ButtonReset = tkinter.Button(frameMain, text='Reset', command=ButtonReset)
ButtonReset.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

ButtonSend = tkinter.Button(frameMain, text="Send", bg="blue", fg="white", command=(ButtonSending))
ButtonSend.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

exceptionText = tkinter.IntVar()
exceptionLabel = tkinter.Label(frameMain, textvariable=exceptionText, fg="red")
exceptionText.set('')
exceptionLabel.grid(row=3, column=0, columnspan=3, sticky="ew", padx=5, pady=5)

labelResult = tkinter.Label(frameMain, text="Output")
labelResult.grid(row=0, column=3, sticky="sw", padx=5, pady=5)
dataCanvas = tkinter.Canvas(frameMain, width=240, height=260, bg="white")
dataCanvas.grid(row=1, column=3, rowspan=100)
scroll = tkinter.Scrollbar(frameMain, orient="vertical", command=dataCanvas.yview)
scroll.grid(row=1, column=4, rowspan=100, sticky="ns")
dataCanvas.config(yscrollcommand = scroll.set)

canvasFrame = tkinter.Frame(dataCanvas, bg="white")
dataCanvas.create_window((10, 0), window=canvasFrame, anchor='nw')

frameMenu.grid(row=0, column=0, sticky='ns')
frameMain.grid(row=0, column=1, sticky='nsew')

def ReadSerial():
    global statusLamp
    if ser.isOpen():
        print('Test1')
        # recentPack = ser.read()
        # print(recentPack)
        # recentPackString = recentPack.decode('utf').rstrip('\n')
        menuval = ''
        if input1.get() == "":
            input1.insert(0, "0")
        if input2.get() == "":
            input2.insert(0, "0")
        if MenuValue == 0:
            menuval = 'Belum pernah di klik'
        if MenuValue == 1:
            menuval = 'A'
        if MenuValue == 2:
            menuval = 'B'
        if MenuValue == 3:
            menuval = 'C'
        if MenuValue == 4:
            menuval = 'D'
        tkinter.Label(canvasFrame, 
            text="Input1 :"+ str(input1.get()) + "\n Input2 :"+ str(input2.get()) + "\n Menu Click : " + str(menuval) + "\n Status Lampu : " + str(statusLamp), 
            font=('Calibri', '8'), bg='white').pack()

# tkinter.mainloop()
while True:
    tkTop.update()
    dataCanvas.config(scrollregion=dataCanvas.bbox("all"))
