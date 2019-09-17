from tkinter import *
from tsp import *

# canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
# canvas.pack()

# frame = tk.Frame(root, bg = 'lightgrey')
# frame.place(relwidth=1, relheight=1)

# buttonBar = tk.Frame(frame, bg = 'grey')
# buttonBar.place(relwidth = 1, relheight = .25, rely = .75)

# bfButton = tk.Button(buttonBar, text = "Brute Force")
# bfButton.place(relwidth = .2, relheight = .175, relx = .05, rely = .5)

# nnButton = tk.Button(buttonBar, text = "Nearest Neighbor")
# nnButton.place(relwidth = .2, relheight = .175, relx = .3, rely = .5)

# fiButton = tk.Button(buttonBar, text = "Farthest Insertion")
# fiButton.place(relwidth = .2, relheight = .175, relx = .55, rely = .5)

# label = tk.Label(frame, text = "TSP Solver", bg = 'grey')
# label.pack()

root = Tk()

canvas_width = 1200
canvas_height = 800

root.title("Euclidean TSP Solver")
w = Canvas(root,
           width=canvas_width,
           height=canvas_height)
w.pack(expand=YES, fill=BOTH)

for pair in coordPairs:
  w.create_oval((pair[0], pair[1], pair[0] + 5, pair[1] + 5), fill = "red")

w.create_oval((100, 100, 110, 110), fill = "red",)

message = Label(root, text="Example Text")
message.pack(side=BOTTOM)

root.mainloop()

# References:
# https://stackoverflow.com/questions/39888580/how-can-i-draw-a-point-with-canvas-in-tkinter
# https://tkdocs.com/tutorial/canvas.html#creating