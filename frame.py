import tkinter as tk
import tkinter.messagebox
import complmentary

def convert():
	input = entry.get()
	if (complmentary.dna_is_actg(input)):
		output = complmentary.reverse_complement(input)
	else:
		output = 'None'
	
	print(input)
	label = tk.Label(window, text=output)
	label.pack()
	
window = tk.Tk()

window.title('Bioinformatic tools')
window.geometry("600x500+250+150")

label = tk.Label(window, text='dna complmentary')
label.pack()

entry = tk.Entry(window, width=20)
entry.pack()

button = tk.Button(window, text='transfer', command=convert)
button.pack()

window.mainloop()
