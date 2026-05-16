import tkinter as tk
from PIL import Image, ImageDraw, ImageOps
import numpy as np
from tensorflow.keras.models import load_model

# Load trained model
model = load_model("digit_model.h5")

# Create window
root = tk.Tk()
root.title("Digit Recognition App")

# Canvas
canvas = tk.Canvas(root, width=280, height=280, bg='white')
canvas.pack()

# Image setup
image = Image.new("L", (280, 280), color=255)
draw = ImageDraw.Draw(image)

# Draw function
def paint(event):
    x1, y1 = (event.x - 8), (event.y - 8)
    x2, y2 = (event.x + 8), (event.y + 8)

    canvas.create_oval(x1, y1, x2, y2, fill='black')
    draw.ellipse([x1, y1, x2, y2], fill='black')

canvas.bind("<B1-Motion>", paint)

# Predict function
def predict_digit():

    # Resize image
    img = image.resize((28, 28))

    # Invert colors
    img = ImageOps.invert(img)

    # Convert to array
    img = np.array(img) / 255.0

    # Reshape
    img = img.reshape(1, 28, 28)

    # Prediction
    prediction = model.predict(img)

    digit = np.argmax(prediction)

    label.config(text=f"Prediction: {digit}")

# Clear function
def clear_canvas():
    canvas.delete("all")
    draw.rectangle([0, 0, 280, 280], fill='white')
    label.config(text="Draw a Digit")

# Buttons
predict_btn = tk.Button(root, text="Predict", command=predict_digit)
predict_btn.pack()

clear_btn = tk.Button(root, text="Clear", command=clear_canvas)
clear_btn.pack()

# Label
label = tk.Label(root, text="Draw a Digit", font=("Arial", 18))
label.pack()

# Run app
root.mainloop()