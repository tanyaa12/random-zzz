from tkinter import *
from tkinter import ttk
from googletrans import Translator , LANGUAGES

root = Tk()
root.geometry('980x500')
root.resizable(0,0)
root.title("Spell It")
root.config(bg = 'black')
#root.title(bg ='white')

#Spell It
Label(root, text = "Spell It", font = "arial 20 bold", fg='white', bg='#1A1A1A').pack()
Label(root,text ="Meaning:", font = 'arial 20 bold', fg='black', bg='white' , height = '2', width = '10').pack(side = 'bottom')


#INPUT AND OUTPUT TEXT
#Label(root,text ="Enter Text", font = 'arial 13 bold', bg ='white smoke').place(x=200,y=60)
Input_text = Text(root,font = 'arial 14', height = 11, fg= 'white smoke', bg='#181818', wrap = WORD, padx=5, pady=5, width = 30)
Input_text.place(x=50,y = 100)

#BOX SIZE
#Label(root,text ="", font = 'arial 13 bold', bg ='white smoke').place(x=200,y=60)
Output_text = Text(root,font = 'arial 14', height = 11, fg= 'white smoke', bg='#1B1B1B', wrap = WORD, padx=3, pady=3, width = 30)
Output_text.place(x = 600 , y = 100)
 

language = list(LANGUAGES.values())

src_lang = ttk.Combobox(root, values= language, width =22)
src_lang.place(x=20,y=60)
src_lang.set('Choose Input Language')

dest_lang = ttk.Combobox(root, values= language, width =22)
dest_lang.place(x=810,y=60)
dest_lang.set('Choose Output Language')

#TranslateButton
def Translate():
    translator = Translator()
    translated=translator.translate(text= Input_text.get(1.0, END) , src = src_lang.get(), dest = dest_lang.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)
   

#Translate Button
trans_btn = Button(root, text = 'Translate',font = 'arial 12 bold',pady = 5,command = Translate ,fg='white', bg = '#2C3335', activebackground = 'white')
trans_btn.place(x = 455, y = 180)


root.mainloop()
