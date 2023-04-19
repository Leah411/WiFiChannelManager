import csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *

# Create CSV file with 3 headers
headers1 = ['SSID', 'RSSI','channel_no']
# data1 = [['neta', '30','13'], ['netb', '40','10'], ['netc', '20','10']]

data=[]
with open('output_data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append((row['SSID'], int(row['RSSI']), int(row['channel'])))

# Sort data by ssid
data.sort(key=lambda x: x[0])

#creat a graph

# Plot the data as a bar graph
fig, ax = plt.subplots()
for ssid in sorted(set(d[1] for d in data)):
    y = [d[0] for d in data if d[1] == ssid]
    x = [d[2] for d in data if d[1] == ssid]
    ax.barh(y, x, label=ssid)

ax.set_xlabel('channel')
ax.set_ylabel('RSSI')
ax.legend()

# Create a new Tkinter window
root = Tk()
root.title('SSID by channel_no')
root.geometry('800x600')
root.configure(bg="black")

# Add the matplotlib graph to the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side='top', fill='both', expand=True)

# Show the Tkinter window
root.mainloop()


















#
# # Create new screen for displaying graph
# root = tk.Tk()
# root.geometry("600x400")
#
# # Create canvas for displaying graph
# canvas = tk.Canvas(root)
# canvas.pack(fill='both', expand=True)
#
# #creat figure for the graph
# fig = plt.figure(figsize=(6,4), dpi=100)
# plt.bar(x, y)
# plt.xlabel('channel')
# plt.ylabel('RSSI')
# plt.title('RSSI over channel')
#
# # Convert figure to tkinter canvas and add to the screen
# canvas = fig.canvas
# canvas.get_tk_widget().pack(side='top', fill='both', expand=1)
#
#
# # Start main loop for displaying the screen
# root.mainloop()