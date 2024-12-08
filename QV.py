import os
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo
import requests
import random
import html

def shutdown():
    os.system('shutdown /s /t 1')

try :
    opentdb = (requests.get("https://opentdb.com/api.php?amount=1&type=multiple").json()['results'])[0]
except :
    showerror('Connecting Problems!', "There is no Internet, Micosoft Windows11 is not able to load complitply\nlütfen İntenet'ten yemin olun, Windows11 sıkıntı var")
    for i in range(0, 100):
        try :
            opentdb = (requests.get("https://opentdb.com/api.php?amount=1&type=multiple").json()['results'])[0]
            break
        except :
            print(f'test num {i}.')
    shutdown()

    

root = tk.Tk()

root.overrideredirect(True)
root.attributes("-fullscreen", True)
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")

style = ttk.Style() 
width = root.winfo_screenwidth() 
height = root.winfo_screenheight() 

print(width, height)
font_size = int(max(10, min(width, height) // 40))

style.configure(
    "Custom.TButton",
    font=("Arial", font_size, "bold"),
    foreground="#ffffff",
    background="#0078D7",
    padding=10
)

soru = html.unescape(opentdb['question'])
label = tk.Label(root, text=soru, font=("Arial", font_size))
print(soru)
label.pack(pady=50)

awnsers = []
correct_awnser = opentdb['correct_answer']
awnsers += opentdb['incorrect_answers']
awnsers.append(correct_awnser)
random.shuffle(awnsers)

def checking_awnser(your_awnser):
    global correct_awnser
    if your_awnser == correct_awnser :
        root.destroy()
    else :
        shutdown()

for awnser in awnsers:
    print(awnser)
    close_button = ttk.Button(
        root,
        text=html.unescape(awnser),
        style="Custom.TButton",
        command=lambda awnser=awnser: checking_awnser(awnser))
    close_button.pack(pady=20)

root.mainloop()
