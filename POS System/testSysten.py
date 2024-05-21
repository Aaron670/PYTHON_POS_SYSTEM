import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class POSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("POS System")
        
        # Create a list of items (you can load this from a database)
        self.items = [
            {"name": "Item 1", "price": 10.0, "image": "item1.jpg"},
            {"name": "Item 2", "price": 15.0, "image": "item2.jpg"},
            # Add more items here
        ]
        
        # Create a dictionary to store item images
        self.item_images = {}
        for item in self.items:
            img_path = f"item_images/{item['image']}"
            self.item_images[item["name"]] = ImageTk.PhotoImage(Image.open("./Settings/ImageLinks/file.png"))
        
        # Create widgets
        self.item_label = ttk.Label(root, text="Select an item:")
        self.item_combobox = ttk.Combobox(root, values=[item["name"] for item in self.items])
        self.item_image_label = ttk.Label(root)
        self.price_label = ttk.Label(root, text="Price:")
        self.total_label = ttk.Label(root, text="Total: $0.00")
        
        # Layout widgets
        self.item_label.grid(row=0, column=0)
        self.item_combobox.grid(row=0, column=1)
        self.item_image_label.grid(row=1, column=0, columnspan=2)
        self.price_label.grid(row=2, column=0)
        self.total_label.grid(row=2, column=1)
        
        # Bind combobox selection
        self.item_combobox.bind("<<ComboboxSelected>>", self.update_item_image)
        
    def update_item_image(self, event):
        selected_item = self.item_combobox.get()
        if selected_item in self.item_images:
            self.item_image_label.config(image=self.item_images[selected_item])
            # Update price label and total
            for item in self.items:
                if item["name"] == selected_item:
                    self.price_label.config(text=f"Price: ${item['price']:.2f}")
                    break

if __name__ == "__main__":
    root = tk.Tk()
    app = POSApp(root)
    root.mainloop()