import tkinter as tk
import webbrowser

def create_second_window():
    second_window = tk.Toplevel(root)
    second_window.geometry("200x200")
    second_button = tk.Button(second_window, text="AUF KEINEN FALL DRÜCKEN!!!!!!", bg="red", command=play_video, height=75,width= 75)
    second_button.pack()

def play_video():
    youtube_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    webbrowser.open(youtube_url)


root = tk.Tk()
root.geometry("200x200")


first_button = tk.Button(root, text="NICHT DRÜCKEN!!", bg="red", command=create_second_window, height=75,width= 75)
first_button.pack()


root.mainloop()
