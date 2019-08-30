import tkinter as tk

HEIGHT = 700
WIDTH = 1200

root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root, bg = 'lightgrey')
frame.place(relwidth=1, relheight=1)

button = tk.Button(frame, text = "test")
button.pack(side = 'bottom')

label = tk.Label(frame, text = "TSP Solver", bg = 'grey')
label.pack()

root.mainloop()