from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
from tkinter import PhotoImage
from gtts import gTTS
from playsound import playsound
import os


# Function to perform translation
def change(text="type", src="English", dest="Hindi"):
    trans = Translator()
    trans1 = trans.translate(text, src=src, dest=dest)
    return trans1.text

# Function to handle translation on button click
def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = Sor_txt.get(1.0, END).strip()  # Strip to remove any extra newlines
    if masg:
        textget = change(text=masg, src=s, dest=d)
        dest_txt.delete(1.0, END)
        dest_txt.insert(END, textget)

# Creating the main window
root = Tk()
root.title("Smart Translator")
root.geometry("550x750")
root.config(bg="#f0f0f0")  # Light gray background

# Header Label
header_label = Label(root, text="Smart Translator", font=("Helvetica", 28, "bold"), bg="#0066cc", fg="white")
header_label.place(x=0, y=0, width=550, height=60)

# Source Text Label
lab_src_txt = Label(root, text="Source Text", font=("Helvetica", 16, "bold"), bg="#009999", fg="white")
lab_src_txt.place(x=20, y=80, height=40, width=200)

# Source Textbox
Sor_txt = Text(root, font=("Helvetica", 14), wrap=WORD, bd=2, relief=RIDGE)
Sor_txt.place(x=20, y=130, height=180, width=510)

# Language Selection for Source
comb_sor = ttk.Combobox(root, value=list(LANGUAGES.values()), font=("Helvetica", 12), state="readonly")
comb_sor.place(x=20, y=330, height=40, width=220)
comb_sor.set("English")  # Default language

# Language Selection for Destination
comb_dest = ttk.Combobox(root, value=list(LANGUAGES.values()), font=("Helvetica", 12), state="readonly")
comb_dest.place(x=290, y=330, height=40, width=220)
comb_dest.set("Hindi")  # Default language

# Translate Button
button_change = Button(root, text="Translate", font=("Helvetica", 14, "bold"), bg="#339966", fg="white", command=data, relief=RAISED, bd=4)
button_change.place(x=200, y=380, height=50, width=150)

# Destination Text Label
lab_dest_txt = Label(root, text="Translated Text", font=("Helvetica", 16, "bold"), bg="#ff6666", fg="white")
lab_dest_txt.place(x=20, y=450, height=40, width=200)

# Destination Textbox
dest_txt = Text(root, font=("Helvetica", 14), wrap=WORD, bd=2, relief=RIDGE)
dest_txt.place(x=20, y=500, height=180, width=510)

# Footer Label
footer_label = Label(root, text="Designed by Shrish And Raj Gupta", font=("Helvetica", 12,"bold"), bg="#0066cc", fg="white")
footer_label.place(x=0, y=670, width=550, height=30)

#####convert language name to language code

# Reverse the LANGUAGES dictionary (language name -> code)
reversed_languages = {name.lower(): code for code, name in LANGUAGES.items()}

### Function to get the source language code from the language name
def get_language_code1(language_name):
    return reversed_languages.get(language_name.lower())
# Example usage
language_name = comb_sor.get()# You can input any language name here


#### Function to get the dest language code from the language name
def get_language_code2(language_name):
    return reversed_languages.get(language_name.lower())
# Example usage
language_name = comb_dest.get()

####

# Function to convert text to speech
def text_to_speech(text, language_code):
    tts = gTTS(text=text, lang=language_code, slow=False)
    tts.save("output.mp3")
    playsound("output.mp3")# Play the saved audio file

    # Path to the file you want to delete
    filename = "output.mp3"
    os.remove(filename)
    
# SOURCE Input text and language code
def data2():
    text1 = Sor_txt.get(1.0, END).strip()
    if text1:
        language_code1 = get_language_code1(language_name)
        text_to_speech(text1, language_code1)

    # Dest Input text and language code
def data3():
    text2 = dest_txt.get(1.0, END).strip()
    if text2:
        language_code2 = get_language_code2(language_name)
        text_to_speech(text2, language_code2)


###Speak button
try:
    icon = PhotoImage(file="speak.png")
    icon = icon.subsample(12, 12)
except Exception as e:
    print(f"Error loading icon: {e}")
    icon = None
# Pronunciation icon source
button_icon1 = Button(root, compound=LEFT, image=icon, command=data2 ,bg="white", relief=RAISED, bd=4)
button_icon1.place(x=480, y=80, height=50, width=50)

# Pronunciation icon destination
button_icon2 = Button(root, compound=LEFT, image=icon, command=data3, bg="white", relief=RAISED, bd=4)
button_icon2.place(x=480, y=450, height=50, width=50)
    

# Main loop
root.mainloop()
