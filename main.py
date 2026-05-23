import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import messagebox

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


data = pd.read_csv("Housing.csv")


x = data[['area', 'bedrooms', 'bathrooms']]
y = data['price']

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)



model = LinearRegression()
model.fit(x_train, y_train)


def predict_price():

    try:

        area = int(area_entry.get())
        bedrooms = int(bedroom_entry.get())
        bathrooms = int(bathroom_entry.get())

        prediction = model.predict(
            [[area, bedrooms, bathrooms]]
        )

        result_label.config(
            text=f"Predicted Price: ₹ {int(prediction[0])}"
        )

    except:

        messagebox.showerror(
            "Error",
            "Please enter valid numbers"
        )


root = tk.Tk()

root.title("House Price Prediction System")

root.geometry("500x400")

title_label = tk.Label(
    root,
    text="House Price Prediction",
    font=("Arial", 20, "bold")
)

title_label.pack(pady=20)


area_label = tk.Label(
    root,
    text="Enter Area (sq.ft)"
)

area_label.pack()

area_entry = tk.Entry(root)
area_entry.pack(pady=5)

bedroom_label = tk.Label(
    root,
    text="Enter Bedrooms"
)

bedroom_label.pack()

bedroom_entry = tk.Entry(root)
bedroom_entry.pack(pady=5)


bathroom_label = tk.Label(
    root,
    text="Enter Bathrooms"
)

bathroom_label.pack()

bathroom_entry = tk.Entry(root)
bathroom_entry.pack(pady=5)


predict_button = tk.Button(
    root,
    text="Predict Price",
    command=predict_price,
    bg="green",
    fg="white",
    font=("Arial", 12, "bold")
)

predict_button.pack(pady=20)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 16, "bold")
)

result_label.pack(pady=20)


root.mainloop()