from tkinter import *
from PIL import Image, ImageTk
import speech_to_text
import action

# Initialize the main window
root = Tk()
root.title("AI Assistant")
root.geometry("500x675")
root.resizable(False, False)
root.config(bg="#F5F5DC")

# Define callback functions for buttons
def ask():
    ask_value = speech_to_text.recognize_speech()
    if ask_value is not None:
        bot_value = action.action(ask_value)
        text.insert(END, 'User--->' + ask_value + "\n")
        if bot_value is not None:
            text.insert(END, "BOT<---" + str(bot_value) + "\n")
        if bot_value == "yes":
            root.destroy()
    else:
        text.insert(END, "BOT<--- Sorry, I didn't catch that.\n")

def delete():
    text.delete('1.0', "end")

def send():
    send = entry.get()
    if send:
        bot = action.action(send)
        text.insert(END, 'User--->' + send + "\n")
        if bot is not None:
            text.insert(END, "BOT<---" + str(bot) + "\n")
        if bot == "yes":
            root.destroy()

# Create frame
frame = LabelFrame(root, padx=20, pady=20, borderwidth=3, relief="sunken", bg="#f8ac9a")
frame.grid(row=0, column=0, padx=30, pady=10, sticky="nsew")

# Add text label
text_label = Label(frame, text="AI Assistant", font=("Comic Sans MS", 14, "bold"), bg="#acf8e7")
text_label.grid(row=0, column=0, padx=20, pady=10)

# Add image
try:
    image_path = r"F:\project\AI_Desktop\kalai_AI.jpg" 
    image = ImageTk.PhotoImage(Image.open(image_path))
    image_label = Label(frame, image=image, bg="#f8ac9a")  # Match background color of the frame
    image_label.grid(row=1, column=0, pady=20, padx=10, sticky="nsew")  # Centered in column 0
except Exception as e:
    print(f"Error loading image: {e}")

# Add text widget
text = Text(root, font=("Courier 10 bold"), bg="#f8ac9a", height=25, width=50)
text.grid(row=1, column=0, padx=30, pady=(10, 20), sticky="nsew")

# Add entry widget
entry = Entry(root, justify="center")
entry.grid(row=2, column=0, padx=30, pady=10, sticky="ew")

# Add buttons using grid for consistency
button_frame = Frame(root, bg="#F5F5DC")
button_frame.grid(row=3, column=0, pady=10, sticky="nsew")

Button1 = Button(button_frame, text='ASK', bg="#d3d3d3", pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask)
Button1.grid(row=0, column=0, padx=10)

Button2 = Button(button_frame, text='DELETE', bg="#d3d3d3", pady=16, padx=40, borderwidth=3, relief=SOLID, command=delete)
Button2.grid(row=0, column=1, padx=10)

Button3 = Button(button_frame, text='SEND', bg="#d3d3d3", pady=16, padx=40, borderwidth=3, relief=SOLID, command=send)
Button3.grid(row=0, column=2, padx=10)

# Configure grid weights to make widgets expand properly
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)
button_frame.grid_columnconfigure(2, weight=1)

# Start the main loop
root.mainloop()
