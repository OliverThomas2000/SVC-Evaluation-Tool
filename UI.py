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
    mfccs = MFCC(file_path).calculate()

    # Clear the current plot and plot the MFCCs
    ax.clear()
    ax.plot(mfccs)
    canvas.draw()

def calculate_difference():
    mfcc1 = ax1.lines[0].getydata()
    mfcc2 = ax2.lines[0].getydata()

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


fig1 = plt.figure(figsize=(5,3))
ax1 = fig1.add_subplot(111)

fig2 = plt.figure(figsize=(5,3))
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