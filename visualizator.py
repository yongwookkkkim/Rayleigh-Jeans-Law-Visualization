from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox

root = Tk()
root.title("Rayleigh Jeans Approximation Visualizor")
root.iconbitmap('logopic.ico')

#constants
k = 1.38064852e-23
c = 299792458
h=6.62607004e-34

#Boltzmann Constant
boltzmannLabel = Label(root, text="Boltzmann Constant (k) = 1.38064852e-23 J/K")
boltzmannLabel.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

#speed of light
speedOfLightLabel = Label(root, text="Speed of Light (c) = 299792458 m/s")
speedOfLightLabel.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

#Planck's Constant
planckLabel = Label(root, text="Planck's Constant (h) = 6.62607004e-34 J s")
planckLabel.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

#temperature
temperatureLabel = Label(root, text="Temperature (\u2103)")
temperatureLabel.grid(row=3, column=0)

temperatureInput = Entry(root, width=50, borderwidth=5)
temperatureInput.grid(row=3, column=1)

#run button
def myClick():
    try:
        frequencies=np.linspace(1, 3*c*(float(temperatureInput.get())+273)/(2.898e-3), 1000)
        plt.figure(figsize=(10, 6))
        rayleigh = (2 * frequencies**2 * k * (float(temperatureInput.get())+273)) / (c**2)
        planck = (2 * h * frequencies**3 / c**2) / (np.exp((h * frequencies) / (k * (float(temperatureInput.get())+273))) - 1)
        plt.plot(frequencies*1e-12, rayleigh*1e9, label="Rayleigh-Jeans")
        plt.plot(frequencies*1e-12, planck*1e9, label="Planck")
        plt.legend()
        plt.grid()
        plt.ylim(0, 1.5*max(planck)*1e9)
        plt.xlabel("Frequency (THz)")
        plt.ylabel("Intensity (W/sr m\u00b2 nm)")
        plt.title(f"Comparison of the Rayleigh-Jeans Approximation and the Planck's Law for {float(temperatureInput.get())+273}K black body\n(Infrared: 0.3THz ~ 400THz ; Visible: 400THz ~ 800THz ; Ultraviolet: 800THz ~ 30,000THz)")
        temperatureInput.delete(0, END)
        plt.show()
    except:
        messagebox.showerror("Error", "Please enter a valid temperature.")

runButton = Button(root, text="Show me the result!", command=myClick)
runButton.grid(row=4, column=0, columnspan=2, pady=10, padx=10)

root.mainloop()
