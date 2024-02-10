import tkinter as tk

class MeinProgramm:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI mit Kästchen")
        self.root.configure(bg="white")

        for i in range(3):
            for j in range(3):
                frame = tk.Frame(self.root, width=100, height=100, borderwidth=2, relief="solid", bg="white")
                frame.grid(row=i, column=j)

if __name__ == "__main__":
    root = tk.Tk()
    programm = MeinProgramm(root)
    root.mainloop()
