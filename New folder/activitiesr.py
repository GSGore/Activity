import tkinter as tk
from tkinter import ttk
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load dataset
data = {
    "Level": [5, 4, 3, 2, 1],
    "BMI": [18, 23, 25, 30, 40],
    "Walk Slowly": [54, 60, 67, 75, 82],
    "Walk Quickly": [27, 30, 34, 37, 41],
    "Run Slowly": [22, 24, 27, 30, 33],
    "Run Quickly": [17, 19, 21, 24, 26],
    "ARE+ADA": [282.5, 312.5, 352.5, 392.5, 432.5],
    "Category": ["Normal", "Over Weight", "Obese", "Super Obese", "Hyper Obese"]
}

df = pd.DataFrame(data)

# Train a RandomForestClassifier
X = df[['BMI']]
y = df['Category']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Create GUI
def calculate_bmi(age, weight, height):
    # Convert height from cm to meters
    height_m = height / 100  
    # Formula to calculate BMI: weight (kg) / (height (m) ** 2)
    bmi = weight / (height_m ** 2)
    return bmi

def recommend_activity():
    age = float(age_entry.get())
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    
    bmi = calculate_bmi(age, weight, height)
    BMI_label.config(text=f"BMI: {bmi:.2f}")  # Update BMI label
    
    category = model.predict([[bmi]])[0]
    if category == 'Obese':
        recommendation = "(Overweight)-You can try walking slowly."
    elif category == 'Super Obese' or category == 'Hyper Obese':
        recommendation = "(Obesity)-You can try walking slowly or swimming."
    else:
        recommendation = "(Healthy)-You can engage in various physical activities."
    recommendation_label.config(text=recommendation)

root = tk.Tk()
root.title("Activity Recommendation based on BMI")

age_label = ttk.Label(root, text="Enter your age:")
age_label.grid(row=0, column=0, padx=5, pady=5)

age_entry = ttk.Entry(root)
age_entry.grid(row=0, column=1, padx=5, pady=5)

weight_label = ttk.Label(root, text="Enter your weight (kg):")
weight_label.grid(row=1, column=0, padx=5, pady=5)

weight_entry = ttk.Entry(root)
weight_entry.grid(row=1, column=1, padx=5, pady=5)

height_label = ttk.Label(root, text="Enter your height (cm):")
height_label.grid(row=2, column=0, padx=5, pady=5)

height_entry = ttk.Entry(root)
height_entry.grid(row=2, column=1, padx=5, pady=5)

recommend_button = ttk.Button(root, text="Recommend Activity", command=recommend_activity)
recommend_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

recommendation_label = ttk.Label(root, text="")
recommendation_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

BMI_label = ttk.Label(root, text="")
BMI_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
