from itertools import cycle
from PIL import Image, ImageDraw
from time import sleep
import tkinter as tk

root=tk.Tk()
root.title("Slide Show")


image_paths = [
    r"C:\Users\sarim\OneDrive\Desktop\Sarim important\hairstyle1.jpg",
    r"C:\Users\sarim\OneDrive\Desktop\Sarim important\IMG-20240922-WA0004.jpg",
    r"C:\Users\sarim\OneDrive\Desktop\Sarim important\IMG-20240922-WA0001.jpg",
    r"C:\Users\sarim\OneDrive\Desktop\Sarim important\IMG-20240922-WA0007.jpg"
    r"C:\Users\sarim\OneDrive\Desktop\Sarim important\IMG-20240922-WA0006.jpg"
]


image_sizes=(1080,1080)
images=[Image.open(path). resize(image_sizes) for path in image_paths]
