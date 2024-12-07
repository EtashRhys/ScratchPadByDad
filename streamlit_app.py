import streamlit as st

st.title(ScratchPadbyDad)
st.write(
    import tkinter as tk
from tkinter.colorchooser import askcolor

class ScratchPad(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Scratch Pad")
        self.geometry("800x600")

        self.canvas = tk.Canvas(self, bg="white", width=800, height=600)
        self.canvas.pack(fill="both", expand=True)

        self.pen_color = "black"
        self.pen_width = 5
        self.last_x, self.last_y = None, None  # Keeps track of last position for continuous drawing

        # Buttons
        self.color_button = tk.Button(self, text="Choose Pen Color", command=self.choose_pen_color)
        self.color_button.pack(side="left", padx=10)

        self.bg_button = tk.Button(self, text="Choose Background Color", command=self.choose_bg_color)
        self.bg_button.pack(side="left", padx=10)

        self.width_label = tk.Label(self, text="Pen Width:")
        self.width_label.pack(side="left", padx=10)

        # Slider for pen width (adjusted to 40)
        self.width_slider = tk.Scale(self, from_=1, to=40, orient="horizontal", command=self.update_pen_width)
        self.width_slider.set(self.pen_width)  # Set the initial value of the slider
        self.width_slider.pack(side="left", padx=10)

        # Clear Button
        self.clear_button = tk.Button(self, text="Clear", command=self.clear_canvas)
        self.clear_button.pack(side="left", padx=10)

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset_last_position)  # Reset position after mouse release

    def paint(self, event):
        if self.last_x and self.last_y:
            # Draw a line from the last position to the current position
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, width=self.pen_width, fill=self.pen_color, capstyle=tk.ROUND)
        
        # Update the last position to the current one
        self.last_x, self.last_y = event.x, event.y

    def reset_last_position(self, event):
        # Reset the position when mouse is released
        self.last_x, self.last_y = None, None

    def choose_pen_color(self):
        color = askcolor()[1]
        if color:
            self.pen_color = color

    def choose_bg_color(self):
        color = askcolor()[1]
        if color:
            self.canvas.config(bg=color)

    def update_pen_width(self, value):
        # Update the pen width with the slider's current value
        self.pen_width = int(value)

    def clear_canvas(self):
        # Clear the entire canvas
        self.canvas.delete("all")


if __name__ == "__main__":
    app = ScratchPad()  # Create an instance of the ScratchPad class
    app.mainloop()  # Start the application's main loop
)
