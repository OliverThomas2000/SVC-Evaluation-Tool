import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from MFCC import *

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("SVC Evaluation Tool")
        self.root.config(bg='white')

        self.main_frame = tk.Frame(self.root, width=1000, height=400, bg='white')
        self.main_frame.grid(row=0, column=0, padx=20, pady=10)

        self.target_frame = tk.Frame(self.main_frame, width=450, height=400, bg='white')
        self.target_frame.grid(row=0,column=0,padx=50,pady=0)

        self.converted_frame = tk.Frame(self.main_frame, width=450, height=400, bg='white')
        self.converted_frame.grid(row=0,column=1,padx=50,pady=0)

        size = (5,5)
        self.fig1 = plt.figure(figsize=size)
        self.ax1 = self.fig1.add_subplot(111)

        self.fig2 = plt.figure(figsize=size)
        self.ax2 = self.fig2.add_subplot(111)

        self.target_canvas = FigureCanvasTkAgg(self.fig1, master=self.target_frame)
        self.converted_canvas = FigureCanvasTkAgg(self.fig2, master=self.converted_frame)

        self.target_canvas.draw()
        self.converted_canvas.draw()

        self.target_canvas.get_tk_widget().pack()
        self.converted_canvas.get_tk_widget().pack()

        self.upload_target = tk.Button(self.target_frame, text="Upload Target Audio", 
            command=lambda: self.upload_audio("target"))
        self.upload_converted = tk.Button(self.converted_frame, text="Upload Model Output", 
            command=lambda: self.upload_audio("converted"))

        self.upload_target.pack()
        self.upload_converted.pack()

        self.options_frame = tk.Frame(self.root, width=200, height=500, bg='white')
        self.options_frame.grid(row=0, column=1, padx=20, pady=10)

        self.calculate_difference_button = tk.Button(self.options_frame, text="Calculate Euclidean difference", command=self.calculate_difference)
        self.calculate_difference_button.pack()

        self.difference = tk.StringVar(self.options_frame, value= 'Difference: 0.00000')
        self.difference_label = tk.Label(self.options_frame, textvariable=self.difference, font=('Arial', 25), bg='white')
        self.difference_label.pack()

    def upload_audio(self, button):
        file_path = filedialog.askopenfilename(filetypes=[("WAV file", ".wav")])
        if not file_path:
            return
        try:
            mfcc_data = MFCC(file_path).calculate()
        except:
            tk.messagebox.showerror("Error", "Couldn't open/find the file")
            return
        if button == "target":
            ax = self.ax1
            canvas = self.target_canvas
        else:
            ax = self.ax2
            canvas = self.converted_canvas
        ax.imshow(mfcc_data, origin='lower', extent=[-1, 1, -1, 1], cmap='jet',interpolation='nearest')
        canvas.draw()
        
    def calculate_difference(self):
        try:
            mfcc1 = self.ax1.images[-1].get_array()
            mfcc2 = self.ax2.images[-1].get_array()
        except:
            tk.messagebox.showerror("Error", "Please upload target and model output audio first")
            return
        difference = mfcc_difference(mfcc1,mfcc2)
        print(f"Difference: {difference:.5f}")
        self.difference.set(f"Difference: {round(difference, 5)}")

if __name__=="__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()