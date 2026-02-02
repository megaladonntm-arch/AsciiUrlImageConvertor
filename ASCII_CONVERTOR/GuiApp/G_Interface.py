



import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

ASCII_CHARS = "@%#*+=-:. "
class ASCIIArtApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ASCII Art Generator")
        self.root.geometry("900x700")

        self.text = tk.Text(root, wrap="none", font=("Courier New", 6))
        self.text.pack(fill=tk.BOTH, expand=True)

        menu = tk.Menu(root)
        root.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open Image", command=self.open_image)
        file_menu.add_command(label="Save ASCII", command=self.save_ascii)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)

    def open_image(self):
        path = filedialog.askopenfilename(
            filetypes=[("Images", "*.png *.jpg *.jpeg")]
        )
        if not path:
            return

        try:
            ascii_art = self.image_to_ascii(path)
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, ascii_art)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def save_ascii(self):
        ascii_text = self.text.get("1.0", tk.END)
        if not ascii_text.strip():
            messagebox.showwarning("Warning", "Nothing to save")
            return

        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text file", "*.txt")]
        )
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(ascii_text)

    def image_to_ascii(self, image_path, width=150):
        image = Image.open(image_path).convert("L")

        aspect_ratio = image.height / image.width
        height = int(width * aspect_ratio * 0.55)

        image = image.resize((width, height))

        pixels = image.getdata()
        ascii_str = ""

        for i, pixel in enumerate(pixels):
            ascii_str += ASCII_CHARS[pixel * len(ASCII_CHARS) // 256]
            if (i + 1) % width == 0:
                ascii_str += "\n"

        return ascii_str
