import tkinter as tk
from PIL import Image, ImageTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import json
import random
import datetime
import matplotlib.pyplot as plt

def get_water_temperature():

# Read data from the JSON file
    with open("water_temp.json", "r") as infile:
        data = json.load(infile)

# Extract dates and values from the data
    dates = [item["date"] for item in data]
    values = [item["value"] for item in data]

# Create a line plot of the data
    plt.plot(dates, values)
    plt.title("Water Temperature")
    plt.xlabel("Date")
    plt.ylabel("Temperature (C)")
    plt.show()


# Generate 20 measurements for "Water Temperature" metric
data = []
for i in range(20):
    temperature = round(random.uniform(15, 25), 2)
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    measurement = {"date": date, "value": temperature}
    data.append(measurement)

# Write data to a JSON file
with open("water_temp.json", "w") as outfile:
    json.dump(data, outfile)


# Define the GUI window
root = tk.Tk()
root.title("Smart Dog House")
root.geometry("1200x550")
root.resizable(False, False)
root.configure(bg="white")  # Change background color to white

# Load the image
image_path = r"C:\Users\Liron\Desktop\Smart DogHouse\EEfinal_rasp\Picture\del_pic.jpg"
image = Image.open(image_path)

# Resize the image to fit the GUI
image = image.resize((1200, 900), Image.ANTIALIAS)

# Convert the image to a Tkinter PhotoImage and set it as the background
photo = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)



# Define styles for labels and buttons
label_style = {"font": ("Arial", 16, "bold"), "fg": "black", "bg": "white"}  # Change label color to black and background color to white
button_style = {"font": ("Arial", 12), "fg": "white", "bg": "#0074D9"}  # Change button color to blue
label_style2 = {"font": ("Arial", 16, "bold"), "fg": "black"} 
# Define the labels and buttons
temp_humid_label = tk.Label(root, text="DogHouse Temperature & Humidity", **label_style)
temp_humid_label.pack(pady=10)
temp_humid_button = tk.Button(root, text="Check", command=lambda: print("Currently DogHouse Temperature & Humidity"), **button_style)
temp_humid_button.pack()

water_temp_label = tk.Label(root, text="Water Temperature", **label_style)
water_temp_label.pack(pady=10)
water_temp_button = tk.Button(root, text="Check", command=lambda: print("Currently Water Temperature"), **button_style)
water_temp_button.pack()

food_weight_label = tk.Label(root, text="Food Weight", **label_style)
food_weight_label.pack(pady=10)
food_weight_button = tk.Button(root, text="Check", command=lambda: print("Food Weight"), **button_style)
food_weight_button.pack()



dog_weight_label = tk.Label(root, text="Dog Weight", **label_style)
dog_weight_label.pack(pady=10)
dog_weight_button = tk.Button(root, text="Check", command=lambda: print("Dog Weight"), **button_style)
dog_weight_button.pack()



plot_label = tk.Label(root, text="Graphs",**label_style2)
plot_label.pack(pady=20)
plot_label.place(x=460, y=370)

weight_graph_button = tk.Button(root, text="Dog Weight Graph", command=lambda: print("Weight Graph"), **button_style)
weight_graph_button.pack(side='left', padx=5, pady=0)

temp_graph_button = tk.Button(root, text="DogHouse Temperature Graph", command=lambda: print("Temperature Graph"), **button_style)
temp_graph_button.pack(side='left', padx=5, pady=0)


temp_graph_button = tk.Button(root, text="DogHouse Humidity Graph", command=lambda: print("Temperature Graph"), **button_style)
temp_graph_button.pack(side='left', padx=5, pady=0)

temp_graph_button = tk.Button(root, text="Water Temperature Graph", command=lambda: get_water_temperature() , **button_style)
temp_graph_button.pack(side='left', padx=5, pady=0)

water_graph_button = tk.Button(root, text="Water Consuming Graph", command=lambda: print("I LOVE TO DRINK"), **button_style)
water_graph_button.pack(side='left', padx=5, pady=0)

food_graph_button = tk.Button(root, text="Food Consuming Graph", command=lambda: print("I LOVE TO EAT"), **button_style)
food_graph_button.pack(side='left', padx=5, pady=0)

# Define the plot window for the graphs
fig = Figure(figsize=(6, 4), dpi=100)
plot_window = FigureCanvasTkAgg(fig, root)
plot_window.get_tk_widget().pack(padx=20, pady=10, side=tk.BOTTOM, fill=tk.BOTH, expand=1)

root.mainloop()