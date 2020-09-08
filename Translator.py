from tkinter import *
from tkinter.ttk import Combobox
from googletrans import Translator
import tkinter.messagebox
from gtts import gTTS
from time import sleep
import threading
import os
import pyglet
from PyDictionary import *
from playsound import playsound

class translate:
    def __init__(self,root):
        self.root=root
        self.root.title("Translate")
        self.root.geometry("500x505")
        self.root.resizable(0,0)
        #self.root.iconbitmap("img.ico")

        to_TRANS_lan=StringVar()
        select=StringVar()
        TRANSl=StringVar()







        
        def on_enter1(e):
            but_tran['background']="black"
            but_tran['foreground']="cyan"
  
        def on_leave1(e):
            but_tran['background']="SystemButtonFace"
            but_tran['foreground']="SystemButtonText"


        def on_enter2(e):
            but_listen['background']="black"
            but_listen['foreground']="cyan"
  
        def on_leave2(e):
            but_listen['background']="SystemButtonFace"
            but_listen['foreground']="SystemButtonText"



            


        def trans():
            try:
                texttopaste1.delete('1.0',END)
                translator=Translator()
                translated=translator.translate(texttopaste.get("1.0","end"),dest=select.get())
                 #texttopaste.get("1.0","end")
                texttopaste1.insert(1.0,translated.text)
            except:
                tkinter.messagebox.askretrycancel("Internet Error","INTERNET CONNECTION MAY GONE OR LANGUAGE ERROR",icon="info")

        def speak():
            try:
                
                texts=texttopaste1.get("1.0","end")
                tts = gTTS(text=texts, lang=select.get())
                filename = 'C:\\TEMP\\temp.mp3'
                tts.save(filename)
                playsound('C:\\TEMP\\temp.mp3')
                os.remove(filename) #remove temperory file
                
            except:
                tkinter.messagebox.askretrycancel("Internet Error","INTERNET CONNECTION MAY GONE OR LANGUAGE ERROR",icon="info")


            

            #music = pyglet.media.load(filename, streaming=False)
            #music.play()

            #pyglet.app.run()

            #sleep(4)

            #music.pause()

            #print(player.time())
            #sleep(music.duration) #prevent from killing
            




        

#===================================================#
        
        Mainframe=LabelFrame(height=505,width=500,bd=3,text="Translate")
        Mainframe.place(x=1,y=0)

        frame1=Frame(Mainframe,width=493,height=200,bg="yellow")
        frame1.place(x=0,y=0)

        frame2=Frame(Mainframe,width=493,height=100,relief="ridge",bd=4,bg="cyan")
        frame2.place(x=0,y=202)

        frame3=Frame(Mainframe,width=493,height=180,bg="red")
        frame3.place(x=0,y=303)

#=========================================text/frame1=======================#
        Scol=Scrollbar(frame1,orient="vertical")
        Scol.grid(column=10,sticky="NS")
        
        texttopaste=Text(frame1,height=10,width=59,font=('times new roman',12,'bold'),yscrollcommand=Scol.set)
        texttopaste.grid(row=0,column=0)
        Scol.config(command=texttopaste.yview)


#-----------------------------------------------------------------
        but_tran=Button(frame2,text="Translate",width=13,font=('times new roman',11,'bold'),height=0,cursor="hand2",command=trans)
        but_tran.place(x=180,y=25)
        but_tran.bind("<Enter>",on_enter1)
        but_tran.bind("<Leave>",on_leave1)


        but_listen=Button(frame2,text="Listen",width=13,font=('times new roman',11,'bold'),height=0,cursor="hand2",command=speak)
        but_listen.place(x=350,y=25)
        but_listen.bind("<Enter>",on_enter2)
        but_listen.bind("<Leave>",on_leave2)


        


        Lang_list=["en","hi","ur","te","la","iw","kn","af","sq","am","ar","hy","az","eu","basque","be","bn","bs","bg","ca","ceb","ny","zh-cn","zh-tw","co","hr","cs","da","mr","nl","fr","ja","pt","ko","ru"]
        Lang_list_combo=Combobox(frame2,values=Lang_list,font=('arial',10),width=14,state="readonly",textvariable=select)
        Lang_list_combo.set("select language")
        Lang_list_combo.place(x=25,y=30)



        






#=======================================================================
        Scol1=Scrollbar(frame3,orient="vertical")
        Scol1.grid(column=10,sticky="NS")
        
        texttopaste1=Text(frame3,height=9,width=58,font=('times new roman',12,'bold'),yscrollcommand=Scol1.set,relief="sunken",bd=3)
        texttopaste1.grid(row=0,column=0)
        Scol1.config(command=texttopaste1.yview)


#=====================================================
        
        




        




if __name__ == "__main__":
    root=Tk()
    app=translate(root)
    root.mainloop()
