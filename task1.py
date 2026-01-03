import tkinter as tk 
from tkinter import * 
from tkinter import messagebox, ttk
from caesar import caesar_encrypt, caesar_decrypt 
from affine import affine_encrypt, affine_decrypt 
from playfair import playMatrix, playfair_encrypt, playfair_decrypt
from hill import hillMatrix, hill_encrypt, hill_decrypt


class CryptoTool(tk.Tk): 
	def __init__(self):

		# Main setup
		super().__init__()			# Initialize the parent class (tk.Tk)
		self.title("Encryption/Decryption Tool")
		self.iconbitmap('linux.ico')
		w, h = 650, 500
		screen_width = self.winfo_screenwidth()
		screen_height = self.winfo_screenheight()
		x = (screen_width / 2) - (w / 2)
		y = (screen_height / 2) - (h / 2)
		self.geometry(f"{w}x{h}+{int(x)}+{int(y)}")

		self.label = tk.Label(self, text="Greetings, fellow Cypherpunk!", font=("Montserrat", 16))
		self.label.pack(padx=20, pady=20)

		# State variables
		self.selectedCipher = tk.IntVar()
		self.selectedAction = tk.IntVar()

		# Widgets
		self.phase_one = phaseOne(self) 
		self.phase_one.pack()

		self.phase_two = phaseTwo(self) 



class phaseOne(ttk.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		self.app = parent

		self.create_widgets()
		

	def OnClick_Submit(self):
		# global cipher, op
		self.app.cipher = self.app.selectedCipher.get()
		self.app.action = self.app.selectedAction.get()
		# messagebox.showinfo("Selection", f"You selected option {op}")

		self.app.label.destroy()
		self.pack_forget() # Switch to phase two
		self.app.phase_two.displays()

 
	def create_widgets(self):

		# Cipher buttons
		buttonFrame = tk.Frame(self)
		buttonFrame.grid_columnconfigure(0, weight=1)
		buttonFrame.grid_columnconfigure(1, weight=1)
		# self.selectedCipher = tk.IntVar()
		self.app.selectedCipher.set(1)
                
		btn1 = tk.Radiobutton(buttonFrame, text="Caeser Cipher", font=("Montserrat", 16), variable = self.app.selectedCipher, value = 1, padx=60, pady=10) 
		btn1.grid(row=0, column=0, sticky=tk.W) 
		
		btn2 = tk.Radiobutton(buttonFrame, text="Affine Cipher", font=("Montserrat", 16), variable = self.app.selectedCipher, value = 2, padx=60, pady=10) 
		btn2.grid(row=0, column=1, sticky=tk.W) 

		btn3 = tk.Radiobutton(buttonFrame, text="Playfair Cipher", font=("Montserrat", 16), variable = self.app.selectedCipher, value = 3, padx=60, pady=10) 
		btn3.grid(row=1, column=0, sticky=tk.W) 
		
		btn4 = tk.Radiobutton(buttonFrame, text="Hill Cipher", font=("Montserrat", 16), variable = self.app.selectedCipher, value = 4, padx=60, pady=10) 
		btn4.grid(row=1, column=1, sticky=tk.W) 

		buttonFrame.pack()

		# Encrypt/Decrypt buttons
		buttonFrame2 = tk.Frame(self)
		buttonFrame2.columnconfigure(0, weight=1)
		# self.selectedAction = tk.IntVar()
		self.app.selectedAction.set(5)

		btn5 = tk.Radiobutton(buttonFrame2, text="Encryption", font=("Montserrat", 16), variable=self.app.selectedAction, value=5)
		btn5.grid(row=0, column=0, sticky=tk.NS)

		btn6 = tk.Radiobutton(buttonFrame2, text="Decryption", font=("Montserrat", 16), variable=self.app.selectedAction, value=6)
		btn6.grid(row=1, column=0, sticky=tk.NSEW)

		buttonFrame2.pack()

		# Submit
		submitButton = tk.Button(self, text='Submit', font=("Montserrat", 16), command=self.OnClick_Submit)
		submitButton.pack(anchor="center", pady=20)


class phaseTwo(ttk.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		self.app = parent


	def hint(self):
		cipher = self.app.cipher
		if cipher == 1:
			messagebox.showinfo("Hint", "Key should be an integer.")
		elif cipher == 2:
			messagebox.showinfo("Hint", "Enter two keys - alpha and beta. Ensure gcd(alpha, 26) = 1.")
		elif cipher == 3:
			messagebox.showinfo("Hint", "Key is any secret word. Example - 'monarchy'")
		else:
			messagebox.showinfo("Hint", "Enter the values of the 2x2 matrix separated by spaces. Example: 5 8 17 3")


	def run(self):
		cipher, action = self.app.cipher, self.app.action
		input, key = self.text_input.get(), self.key.get()
		# print(key)
		result = StringVar()

		if cipher == 1: # Caesar Cipher
			if action == 5: 
				result = caesar_encrypt(input, int(key))
			else: 
				result = caesar_decrypt(input, int(key))

		elif cipher == 2: # Affine Cipher
			alpha, beta = key.split()
			print(alpha, type(alpha))
			if action == 5: 
				result = affine_encrypt(input, int(alpha), int(beta))
			else: 
				result = affine_decrypt(input, int(alpha), int(beta))

		elif cipher == 3: # Playfair Cipher
			matrix = playMatrix(key)
			if action == 5: 
				result = playfair_encrypt(input, matrix)
			else:
				result = playfair_decrypt(input, matrix)
		
		else: # Hill Cipher
			matrix = hillMatrix(key)
			if action == 5: 
				result = hill_encrypt(input, matrix)
			else: 
				result = hill_decrypt(input, matrix)

		output_display = Text(self, wrap=tk.WORD, width=40, height=4, font=("Montserrat", 14))
		output_display.insert(tk.END, result)
		output_display.grid(row=6, padx=10, pady=10, columnspan=2)

 
	def displays(self):
		cipher, action = self.app.cipher, self.app.action

		# Message or Ciphertext input
		if action == 5: act = "message"
		else: act = "ciphertext"
			
		text_label = Label(self, text="Enter your " + act + ":", font=("Montserrat", 16))
		text_label.grid(row=0, padx=10, pady=10)

		self.text_input = Entry(self, width=80)
		self.text_input.grid(row=1, padx=10, pady=10)

		# Key input
		key_label = Label(self, text="Enter your key:", font=("Montserrat", 16))
		key_label.grid(row=2, padx=10, pady=10)

		self.key = Entry(self, width=40)
		self.key.grid(row=3, padx=10, pady=10)

		self.pack()
		self.create_widgets()

	def create_widgets(self):
		submit_btn = Button(self, text='Show Output', font=("Montserrat", 16), command=self.run)
		submit_btn.grid(row=4, padx=10, pady=10)

		hint_btn = Button(self, text="Hint", font=("Montserrat", 16), command=self.hint)
		hint_btn.grid(row=5, padx=10, pady=10)

		

App = CryptoTool()
App.mainloop()