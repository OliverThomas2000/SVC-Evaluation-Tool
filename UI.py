from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from MFCC import *


def upload_audio(canvas, ax):
    # Create a file selection dialog
    file_path = filedialog.askopenfilename(
        filetypes=[
        ("WAV file", ".wav")
    ])
    if not file_path:
        return

    # Load the audio data and extract the MFCCs
    mfcc_data = MFCC(file_path).calculate()

    # Clear the current plot and plot the MFCCs
    mfcc_data = mfcc_data / (np.max(np.abs(mfcc_data)) + 1e-8)

    # Use the imshow function to display the MFCC data
    ax.imshow(mfcc_data, origin='lower', extent=[-1, 1, -1, 1], cmap='jet',interpolation='nearest')
    canvas.draw()

def calculate_difference():
    mfcc1 = ax1.images[-1].get_array()
    mfcc2 = ax2.images[-1].get_array()

    difference = mfcc_difference(mfcc1,mfcc2)


root = Tk()
root.title("SVC Evaluation Tool")
root.config(bg='black')


main_frame = Frame(root, width=1000, height=400, bg='white')
main_frame.grid(row=0, column=0, padx=20, pady=10)

target_frame = Frame(main_frame, width=450, height=400, bg='grey')
target_frame.grid(row=0,column=0,padx=50,pady=0)

converted_frame = Frame(main_frame, width=450, height=400, bg='grey')
converted_frame.grid(row=0,column=1,padx=50,pady=0)

size = (5,5)
fig1 = plt.figure(figsize=size)
ax1 = fig1.add_subplot(111)

fig2 = plt.figure(figsize=size)
ax2 = fig2.add_subplot(111)

target_canvas = FigureCanvasTkAgg(fig1, master=target_frame)
converted_canvas = FigureCanvasTkAgg(fig2, master=converted_frame)

target_canvas.draw()
converted_canvas.draw()

target_canvas.get_tk_widget().pack()
converted_canvas.get_tk_widget().pack()

upload_target = Button(target_frame, text="Upload Target Audio", command=lambda: upload_audio(target_canvas, ax1))
upload_converted = Button(converted_frame, text="Upload Converted Audio", command=lambda: upload_audio(converted_canvas, ax2))

upload_target.pack()
upload_converted.pack()

options_frame = Frame(root, width=200, height=500, bg='white')
options_frame.grid(row=0, column=1, padx=20, pady=10)

calculate_difference_button = Button(options_frame, text="Calculate Euclidean difference", command=calculate_difference)
calculate_difference_button.pack()

root.mainloop()