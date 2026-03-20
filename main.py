import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import speech_recognition as sr
from gtts import gTTS
import os

def calculate_result():
    selected_option = option_var.get()
    if selected_option == 1:
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                messagebox.showinfo("Speech Recognition", "Press OK to start")
                audio = r.listen(source)
                text = r.recognize_google(audio)
                messagebox.showinfo("Speech Recognition", "Recognised successfully")
                messagebox.showinfo("Speech Recognition Result", f"You said: {text}")
        except sr.UnknownValueError:
            messagebox.showinfo("Speech Recognition Result", "Sorry, could not recognize what you said")
        except sr.RequestError as e:
            messagebox.showinfo("Speech Recognition Result", f"Could not request results; {e}")
    elif selected_option == 2:
        user_input_text = input_text.get()
        if user_input_text:
            language = 'en'
            myobj = gTTS(text=user_input_text, lang=language, slow=False)
            myobj.save("output.mp3")
            os.system("output.mp3")
        else:
            messagebox.showinfo("Input Required", "Please enter text to convert to speech.")
    else:
        messagebox.showinfo("Invalid Option", "Please choose a valid option.")


root = tk.Tk()
root.title("PyValk")
root.configure(bg="#36393f")
label = tk.Label(root, text="Choose an option:", bg="#36393f", fg="white")
label.pack()
option_var = tk.IntVar()
style = ttk.Style()
style.configure("TRadiobutton", font=("Calibri", 12), background="#36393f", foreground="white")
option1 = ttk.Radiobutton(root, text="Option 1 (Speech Recognition)", variable=option_var,value=1,style="TRadiobutton")
option2 = ttk.Radiobutton(root, text="Option 2 (Text-to-Speech)", variable=option_var, value=2, style="TRadiobutton")
option1.pack()
option2.pack()
input_label = tk.Label(root, text="Enter text for speech conversion:", bg="#36393f", fg="white")
input_label.pack()
input_text = tk.Entry(root, bg="white", fg="black")
input_text.pack()
calculate_button = tk.Button(root, text="Run", command=calculate_result, bg="#363636", fg="White")
calculate_button.pack()
root.mainloop()
