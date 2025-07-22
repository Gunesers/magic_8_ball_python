
import tkinter as tk
import random
pencere=tk.Tk()
pencere.title("magic8ball")
pencere.geometry("400x400+20+20")
pencere.config(bg="pink")

soru=tk.Entry(pencere,width=30,font=16)
soru.pack(pady=20)



cevaplar=[
    "Kesinlikle evet",
    "Emin olamadım",
    "Hayır",
    "Olabilir",
    "Sanmıyorum",
    "Asla" ,
    "Başka bir zaman bu soruyu yeniden sor",
    "Tekrar dene"
]

def yanıtla():
    sec=random.choice(cevaplar)
    etiket.config(text=sec)


buton=tk.Button(pencere,command=yanıtla,text="Buraya bas",bg="#C574A6",width=20,height=3)
buton.pack()


etiket=tk.Label(pencere,width=40,height=30,bg="plum",font=18)
etiket.pack(pady=20)




pencere. mainloop()







