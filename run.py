import pandas as pd
import numpy as np
from tkinter import filedialog
from tensorflow.keras.models import load_model 
from tkinter import Tk
from tkinter import scrolledtext
from scipy import stats
import random
import pickle
import tkinter
import warnings
warnings.filterwarnings("ignore")

win= Tk()
win.geometry("1350x700+0+0")
win.title("SECURITY IN IOT USING BLOCKCHAIN")

def top_():
    root = Tk()  
    root.geometry("500x500+400+100")  
    root.title("SECURITY IN IOT USING BLOCKCHAIN")
    
    def open_():
        global e_text
        with open('Data.pkl', 'rb') as f:
            x = pickle.load(f)
        psw = list(x.keys())
        e_text=entry.get()
        if e_text in psw:
            from tkinter import messagebox
            messagebox.showinfo("showinfo", "Permission Granted")
            root.destroy()
        else:
            # messagebox.showinfo("Warning", "Not a valid Key.")
            root.destroy()
            # win.destroy()
     
    frame=tkinter.Frame(root, height=480, width=490, bg='white', highlightthickness=1, highlightbackground="black")
    frame.place(x=5, y=10)    
    heading = tkinter.Label(frame,text="SECURITY IN IOT USING BLOCKCHAIN",font=('Times New Roman bold', 17),fg="blue",bg = "white")
    heading.place(x=20,y=10)
    inputlabel = tkinter.Label(frame, bg = 'white',fg='black',  text="Enter the Key : ",font=('Times New Roman bold', 18))
    inputlabel.place(x=30, y=140)
    entry= tkinter.Entry(frame,font=('Century 12'),width=27)
    entry.place(x=200, y=140)
    button1=tkinter.Button(frame, text="Submit", fg = "white", bg = "blue", height= 1, width= 9, font=('Times New Roman bold', 15), command=open_)
    button1.place(x=185, y=275)
    root.mainloop() 
    
def disable_button():
   win.destroy()
 
def Inputfile():
    global i, file, y
    path = filedialog.askopenfilename(filetypes=())
    file = pd.read_csv(path, delimiter=',')
    file = file.drop(['0', 'udp', 'private', 'SF'], axis=1)
    print("\nInput Data : ")
    i = random.randint(0, len(file))
    print(file.iloc[i])
    y = file['normal.']
    text.insert("end", file.iloc[i])
    
def classify_():
    global y, i, file
    X = file.drop(['normal.'], axis=1)
    classes = np.unique(y)
    z_scores = stats.zscore(X.iloc[i])
    X = np.asarray(z_scores)
    X_test = X.reshape(1, len(X))
    model = load_model("Model")
    pred = model.predict(X_test)
    pred = np.argmax(pred)
    print("\nPredicted Class is : ", classes[pred])
    clstext.insert("end", classes[pred])

def result():
    import Result
    ac, pr, re, fs, sp, fpr, fnr = Result.plot()
    atext.insert("end", ac)
    ptext.insert("end", pr)
    rtext.insert("end", re)
    ftext.insert("end", fs)
    stext.insert("end", sp)
    fptext.insert("end", fpr)
    fntext.insert("end", fnr)
    from tkinter import messagebox
    messagebox.showinfo("showinfo", "Graphs and Images saved to Graphs_Images Directory.")
    
heading = tkinter.Label(win,text="SECURITY IN IOT USING BLOCKCHAIN",font=('Times New Roman bold', 25),fg="blue")
heading.place(x=350, y=10)

frame=tkinter.Frame(win, height=600, width=150, bg='white', highlightthickness=1, highlightbackground="black")
frame.place(x=20, y=70)

button1=tkinter.Button(frame, text="ENTER KEY", fg = "white", bg = "blue", height= 2, width= 11, font=('Times New Roman bold', 13), command=top_)
button1.place(x=15, y=80)

entry= tkinter.Entry(frame,font=('Century 12'),width=27)
entry.place(x=200, y=140)

button1=tkinter.Button(frame, text="Input Data", fg = "white", bg = "blue", height= 2, width= 11, font=('Times New Roman bold', 13), command=Inputfile)
button1.place(x=15, y=150)

button=tkinter.Button(frame, text="Classify", fg = "white", bg = "blue", height= 2, width= 11, font=('Times New Roman bold', 13), command=classify_)
button.place(x=15, y=220)

button=tkinter.Button(frame, text="Result", fg = "white", bg = "blue", height= 2, width= 11, font=('Times New Roman bold', 13), command=result)
button.place(x=15, y=290)

button=tkinter.Button(frame, text="Exit", fg = "white", bg = "blue", height= 2, width= 11, font=('Times New Roman bold', 13), command=disable_button)
button.place(x=15, y=360)

frame2=tkinter.Frame(win, height=600, width=780, bg='white', highlightthickness=1, highlightbackground="black")
frame2.place(x=200, y=70)

text = scrolledtext.ScrolledText(win, width = 65, height = 23, font = ("Times New Roman", 15)) 
text.place(x=240, y=150)

frame3=tkinter.Frame(win, height=600, width=330, bg='white', highlightthickness=1, highlightbackground="black")
frame3.place(x=1000, y=70)

inputecg = tkinter.Label(frame2, bg = 'white',fg='black',  text="Output Window",font=('Times New Roman bold', 20))
inputecg.place(x=35, y=40)

reslabel = tkinter.Label(frame3, bg = 'white', fg='black', text="Results",font=('Times New Roman bold', 20))
reslabel.place(x=25, y=40)

acclabel = tkinter.Label(frame3, bg = 'white', fg='blue', text="Accuracy",font=('Times New Roman bold', 15))
acclabel.place(x=25, y=110)

prelabel = tkinter.Label(frame3, bg = 'white', fg='blue', text="Precision",font=('Times New Roman bold', 15))
prelabel.place(x=25, y=170)

recalllabel = tkinter.Label(frame3, bg = 'white', fg='blue', text="Recall",font=('Times New Roman bold', 15))
recalllabel.place(x=25, y=230)

fscorelabel = tkinter.Label(frame3, bg = 'white', fg='blue', text="FMeasure",font=('Times New Roman bold', 15))
fscorelabel.place(x=25, y=290)

spelabel = tkinter.Label(frame3, bg = 'white', fg='blue', text="Specificity",font=('Times New Roman bold', 15))
spelabel.place(x=25, y=350)

fprlabel = tkinter.Label(frame3, bg = 'white', fg='blue', text="FPR",font=('Times New Roman bold', 15))
fprlabel.place(x=25, y=410)

fnrlabel = tkinter.Label(frame3, bg = 'white', fg='blue', text="FNR",font=('Times New Roman bold', 15))
fnrlabel.place(x=25, y=470)

clslabel = tkinter.Label(frame3, bg = 'blue', fg='white', text="Classified O/P",font=('Times New Roman bold', 16))
clslabel.place(x=25, y=530)

atext = tkinter.Text(frame3, height=1.4, width=17, highlightthickness=1, highlightbackground="black")
atext.place(x=170, y=110)

ptext = tkinter.Text(frame3, height=1.4, width=17, highlightthickness=1, highlightbackground="black")
ptext.place(x=170, y=170)

rtext = tkinter.Text(frame3, height=1.4, width=17, highlightthickness=1, highlightbackground="black")
rtext.place(x=170, y=230)

ftext = tkinter.Text(frame3, height=1.4, width=17, highlightthickness=1, highlightbackground="black")
ftext.place(x=170, y=290)

stext = tkinter.Text(frame3, height=1.4, width=17, highlightthickness=1, highlightbackground="black")
stext.place(x=170, y=350)

fptext = tkinter.Text(frame3, height=1.4, width=17, highlightthickness=1, highlightbackground="black")
fptext.place(x=170, y=410)

fntext = tkinter.Text(frame3, height=1.4, width=17, highlightthickness=1, highlightbackground="black")
fntext.place(x=170, y=470)

clstext = tkinter.Text(frame3, height=1.5, width=17, highlightthickness=1, highlightbackground="black")
clstext.place(x=170, y=530)

text.config()
win.mainloop()