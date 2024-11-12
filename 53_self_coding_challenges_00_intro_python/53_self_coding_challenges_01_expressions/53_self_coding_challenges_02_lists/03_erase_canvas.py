# Implement an 'eraser' on a canvas.

# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.
from tkinter import Tk, Canvas

# Initialize the main window
root = Tk()
root.title("Canvas Eraser Example")

# Canvas dimensions
canvas_width = 400
canvas_height = 400
cell_size = 20  # Size of each grid cell

# Create a canvas widget
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Create a 2D grid of blue cells (rectangles)
cells = []
for row in range(0, canvas_width, cell_size):
    row_cells = []
    for col in range(0, canvas_height, cell_size):
        cell = canvas.create_rectangle(col, row, col + cell_size, row + cell_size, fill="blue", outline="lightgrey")
        row_cells.append(cell)
    cells.append(row_cells)

# Create an eraser rectangle (invisible at first)
eraser_size = cell_size * 2
eraser = canvas.create_rectangle(0, 0, eraser_size, eraser_size, outline="black", fill="white", stipple="gray25")

# Update eraser position and erase cells under it
def move_eraser(event):
    # Update the eraser's position to follow the mouse
    x1, y1 = (event.x - eraser_size // 2), (event.y - eraser_size // 2)
    x2, y2 = (event.x + eraser_size // 2), (event.y + eraser_size // 2)
    canvas.coords(eraser, x1, y1, x2, y2)

    # Check for overlapping cells and erase (set to white)
    overlapping_items = canvas.find_overlapping(x1, y1, x2, y2)
    for item in overlapping_items:
        if item != eraser:  # Avoid erasing the eraser itself
            canvas.itemconfig(item, fill="white")

# Bind mouse motion to the eraser movement
canvas.bind("<B1-Motion>", move_eraser)

# Run the Tkinter event loop
root.mainloop()
