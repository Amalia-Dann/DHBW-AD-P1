import tkinter as tk

class MeinProgramm:
    def __init__(self, root):
        self.root = root
        self.root.title("3x3 Felder")
        self.root.configure(bg="white")

        self.root.geometry("600x600+100+100")

        outer_frame = tk.Frame(self.root, bg="white")
        outer_frame.place(relx=0.5, rely=0.5, anchor="center")

        for i in range(3):
            for j in range(3):
                cell_number = i * 3 + j + 1

                frame = tk.Frame(outer_frame, width=150, height=150, borderwidth=2, relief="solid", bg="lightblue")

                label = tk.Label(frame, text=str(cell_number), font=("Arial", 16), bg="lightblue")
                label.place(relx=0.5, rely=0.5, anchor="center")

                frame.grid(row=i, column=j, padx=3, pady=3)

root = tk.Tk()
programm = MeinProgramm(root)
root.mainloop()
