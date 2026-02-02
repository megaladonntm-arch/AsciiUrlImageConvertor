import tkinter as tk
from tkinter import messagebox

from tkinterdnd2 import TkinterDnD, DND_FILES
from M_Alghoritms import image_to_ascii




BG_COLOR = "#0b0b0b"
FG_COLOR = "#d0d0d0"
ACCENT_COLOR = "#1e1e1e"

class ASCIIArtApp(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()

        self.title("ASCII IMAGE RENDERER")
        self.geometry("1000x720")
        self.configure(bg=BG_COLOR)

        self.header = tk.Label(
            self,
            text="DROP IMAGE HERE",
            bg=BG_COLOR,
            fg="#555555",
            font=("Consolas", 14)
        )
        self.header.pack(pady=8)

        self.text = tk.Text(
            self,
            bg=ACCENT_COLOR,
            fg=FG_COLOR,
            insertbackground=FG_COLOR,
            wrap="none",
            font=("Consolas", 6),
            bd=0,
            padx=10,
            pady=10
        )
        self.text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.text.configure(state=tk.DISABLED)

        self.drop_target_register(DND_FILES)
        self.dnd_bind("<<Drop>>", self.drop)

    def drop(self, event):
        path = event.data.strip("{}")

        if not path.lower().endswith((".png", ".jpg", ".jpeg")):
            messagebox.showerror("ERROR", "ONLY IMAGE FILES")
            return

        try:
            ascii_art = self.image_to_ascii(path)
            self.text.configure(state=tk.NORMAL)
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, ascii_art)
            self.text.configure(state=tk.DISABLED)
            self.header.config(text="RENDER COMPLETE", fg="#888888")
        except Exception as e:
            messagebox.showerror("ERROR", str(e))
        

    def image_to_ascii(self, image_path, width=180):
        return image_to_ascii(self, image_path, width)

    